# Adding shared content collaboration to your app

**Framework**: Shared with You

Manage shared content collaboration in your app using CloudKit and iCloud Drive.

#### Overview

Your app can create collaborations and share content in a Messages conversation by leveraging [`CloudKit`](https://developer.apple.com/documentation/CloudKit) and iCloud Drive to create and store content on the server. Collaborators add a document to conversations by sharing content using Messages. The system displays collaboration activity in Messages conversations and in active FaceTime calls.

This collaboration process builds on existing technologies, like drag and drop and the system share sheet. If your app doesn’t use [`iCloud`](https://developer.apple.com/documentation/Foundation/icloud) for shared content, the [`Shared with You`](SharedWithYou.md) framework provides an [`SWCollaborationMetadata`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata) object wrapped in [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) to implement a custom collaboration infrastructure.

##### Create a Collaboration Object

If your app is sharing a file URL using iCloud Drive, that URL is your collaboration object. To manage a CloudKit collaboration, your app uses [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) to register a [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) container and create a collaboration object. The system transports your app’s data to other processes using the `CKShare` container.

Your app gives an existing `CKShare` to the collaboration object or provides a preparation handler to create a `CKShare` when collaboration starts. In the example below, your app starts a new collaboration and creates the `CKShare` container.

```swift
// Create a new collaboration object.

let itemProvider = NSItemProvider()
itemProvider.registerCKShare(container: container, allowedSharingOptions: CKAllowedSharingOptions.standard, preparationHandler: {
    // Create your share and save to the server or throw an error.
    return savedShare
})
```

For an existing collaboration, your app retrieves the existing collaboration object from the server.

```swift
// Retrieve an existing collaboration object.

let itemProvider = NSItemProvider()
itemProvider.registerCKShare(share, container: container, allowedSharingOptions: CKAllowedSharingOptions.standard)
```

##### Present Collaboration Controls

A collaborator can modify the share options from the share sheet. To add the collaboration controls to the header of a share sheet, your app provides the collaboration object that it created or retrieved from the server.

![iPhone with most of the screen dimmed. The center section is an undimmed collaboration panel with a Pages icon. To the right is a Photo Shoot title, and below that is a Collaborate pop-up button. Below that is a disclosure text button with the text, Everyone can make changes.](https://docs-assets.developer.apple.com/published/3bec1b6b2db1b7fe1414ab81d379365b/media-4085564%402x.png)

```swift
// Present a share sheet in iOS.

let activityViewController = UIActivityViewController(activityItems: [collaborationObject], applicationActivities: nil)

presentingViewController.present(activityViewController, animated: true)
```

In macOS, a share popover offers similar options to the iOS share sheet.

![A popover with a Pages icon. To the right is a Photo Shoot title, and below that is subtitle text, Pages Document - 729 KB. Below that is a horizontal row of four round Messages profile icons labeled Lauren Kerr, Camera Crew, Virgil Scott, and Kim Kilgo. Below that is a vertical list of four share icons for AirDrop, Mail, Messages, and Invite with Link. Below that is an Edit Actions menu item.](https://docs-assets.developer.apple.com/published/526c4b429a4ed3c62c4ea19608bc3620/media-4085595%402x.png)

```swift
// Present a share popover in macOS.

let sharingServicePicker = NSSharingServicePicker(items: [collaborationObject])

sharingServicePicker.show(relativeTo: view.bounds, of: view, preferredEdge: .minY)
```

##### Provide a Title and Image for the Collaboration Header

If your app provides a file as shared data, the system automatically populates a title and image for the collaboration header in the share sheet. Otherwise, if your app uses CloudKit data as shared content, or if you’d like to override the default title and image, you can provide a title and image for the collaboration header.

In iOS, create a [`UIActivityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfiguration) with a title and image that your app passes to a [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController).

```swift
// Provide CloudKit metadata in iOS.

let configuration = UIActivityItemsConfiguration(itemProviders: [collaborationItemProvider])
configuration.perItemMetadataProvider = { (_, key) in
    switch key {
    case .linkPresentationMetadata:
        // Create LPLinkMetadata with the title and imageProvider.
        return metadata
    default:
        return nil
    }
}

let activityViewController = UIActivityViewController(activityItemsConfiguration: configuration)
```

In macOS, create an [`NSPreviewRepresentingActivityItem`](https://developer.apple.com/documentation/AppKit/NSPreviewRepresentingActivityItem) with a title, image, and icon that your app passes to an [`NSSharingServicePicker`](https://developer.apple.com/documentation/AppKit/NSSharingServicePicker). The image represents the shared content, and the icon represents the source of the shared content.

```swift
// Provide CloudKit metadata in macOS.

let title = “Shared Item”
let image = NSImage(contentsOfFile: “Shared_Item_Preview_Image.png”)
let icon = NSImage(contentsOfFile: “App_Icon.png”)

let previewRepresentingItem = NSPreviewRepresentingActivityItem(item: collaborationItemProvider, title: title, image: image, icon: icon)

let picker = NSSharingServicePicker(items: [previewRepresentingItem])
```

##### Create a Swiftui Transferable Object for Collaboration Through Sharelink

In SwiftUI, use [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) to support collaboration mode in the share sheet. The object your app shares must adopt [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable), a protocol for sharing and data transfer.

In the example below, a structure provides a [`CKShareTransferRepresentation`](https://developer.apple.com/documentation/CloudKit/CKShareTransferRepresentation) by either returning an existing [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) or creating a new one.

```swift
// Create a SwiftUI Transferable object.

struct Note: Transferable {
    var share: CKShare?
    func saveCKShareToServer() async throws -> CKShare { … }

    static var transferRepresentation: some TransferRepresentation {
        CKShareTransferRepresentation { note in
            if let share = note.share {
                return .existing(share, container: container, options: options)
            } else {
                return .prepareShare(container: container, options: options) {
                    return try await note.saveCKShareToServer()
                }
            }
        }
    }
}
```

If your app is sharing a file URL using iCloud Drive, that URL is the `Transferable` object shared through `ShareLink`.

Once your app creates a `Transferable` object, pass it to `ShareLink`. When your app shares a URL or string, the system automatically creates a preview. Optionally, your app can include a [`SharePreview`](https://developer.apple.com/documentation/SwiftUI/SharePreview) object, which the system uses to display the title and image for the preview.

```swift
// Adopt a SwiftUI ShareLink.

struct ContentView: View {
    // SharedPhoto() returns an object that conforms to the Transferable protocol.
    @State let photo = SharedPhoto()

    var body: some View {
        ShareLink(item: photo, preview: SharePreview(photo.title, image: photo.image))
    }
}
```

##### Initialize the Collaboration View

A collaborator accesses the [`SWCollaborationView`](swcollaborationview.md) using an icon in the navigation bar. This icon shows the app that manages the shared content and the number of collaborators associated with the collaboration.

![An icon with the number 2 is above a popover that points to it. The top of the popover has an icon with three faces. To the right is a Photo Shoot title, below that is a subtitle With Greg, Kim & Virgil as the text. Below that are three round buttons for message, audio, and video. Below that are Current Participants Greg Crane and Virgil Scott. Below that is a Participant Cursors checkbox. Below that is a Manage Shared File menu item.](https://docs-assets.developer.apple.com/published/37a1de41a21e6a4dd18b77c1355d36b7/media-4085597%402x.png)

The system handles the layout and formatting of the collaboration view. Your app is responsible for providing the `itemProvider(_:)` and the [`activeParticipantCount`](swcollaborationview/activeparticipantcount.md). The [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) contains the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) for CloudKit-based apps, the file URL for iCloud Drive-based apps, or the `/SharedWithYouCore/SWCollaborationMetadata/Representation` for custom collaboration infrastructures.

```swift
// Initialize the collaboration view.

let collaborationView = SWCollaborationView(itemProvider: itemProvider)

collaborationView.activeParticipantCount = myModel.activePeople.count
```

To add a completely customized view on the collaboration view, your app creates a view and assigns it to the `contentView`.

```swift
collaborationView.contentView = MyView(model: myModel)
```

For CloudKit and iCloud Drive adopters, the collaboration view includes a manage button. The button brings up the manage user interface, where collaborators can add and remove participants or change the share settings. Your app can also assign a custom title to the [`manageButtonTitle`](swcollaborationview/managebuttontitle.md). The title defaults to “Manage Share” if your app doesn’t customize it.

```swift
collaborationView.manageButtonTitle = "Custom Manage Button"
```

If your app uses a custom collaboration infrastructure, you must provide your own manage button.

##### Observe When a Server Saves a Share

Since your app needs to manage active content sharing, it’s critical to know when a share starts or stops. If your app uses CloudKit or iCloud Drive, Shared with You provides a [`CKSystemSharingUIObserver`](https://developer.apple.com/documentation/CloudKit/CKSystemSharingUIObserver) protocol that your app uses to observe and handle updates to collaborations.

First, your app passes a [`CKContainer`](https://developer.apple.com/documentation/CloudKit/CKContainer) to `CKSystemSharingUIObserver` to create an observer.

```swift
let observer = CKSystemSharingUIObserver(container: container)
```

Then use the [`systemSharingUIDidSaveShareBlock`](https://developer.apple.com/documentation/CloudKit/CKSystemSharingUIObserver/systemSharingUIDidSaveShareBlock-39zlv) in that observer to capture and react to the result of the server-side save of the share.

```swift
observer.systemSharingUIDidSaveShareBlock = { _, result in
    switch result {
    case .success(let share):
        // Handle the successful save of a share.
    case .failure(let error):
        // Handle the error for an unsuccessful save.
    }
}
```

Use the [`systemSharingUIDidStopSharingBlock`](https://developer.apple.com/documentation/CloudKit/CKSystemSharingUIObserver/systemSharingUIDidStopSharingBlock-4g5bn) in that same observer to handle when a share stops.

```swift
observer.systemSharingUIDidStopSharingBlock = { _, result in
    switch result {
    case .success(let share):
        // Handle the successful share deletion.
    case .failure(let error):
        // Handle the error when a deletion fails.
    }
}
```

##### Post Notices for Shared Content Collaboration

Your app can post notices to summarize updates to a collaboration. These notices appear at the top of the related Messages thread. These updates include changes to the shared content, new mentions, server-side changes, and updates to the collaborators.

To post a notice, retrieve the [`SWCollaborationHighlight`](swcollaborationhighlight.md) and use it to create an [`SWHighlightEvent`](swhighlightevent.md) that matches the type of update.

Use [`SWHighlightChangeEvent`](swhighlightchangeevent.md) to post a notice about content updates or comments. Use [`SWHighlightCenter`](swhighlightcenter.md) to retrieve a collaboration highlight with the URL of the [`CKShare`](https://developer.apple.com/documentation/CloudKit/CKShare) your app used to initiate the collaboration.

```swift
// Retrieve the collaboration highlight from the highlight center.

let highlightCenter: SWHighlightCenter = self.highlightCenter

let highlight = try highlightCenter.collaborationHighlight(forURL: ckShareURL, error: &error)
```

Next, create an `SWHighlightChangeEvent` instance. The initializer takes an [`SWHighlight`](swhighlight.md) object and an [`SWHighlightChangeEventTrigger`](swhighlightchangeeventtrigger.md) value. In this case, the app sets the trigger type to [`SWHighlightChangeEventTrigger.edit`](swhighlightchangeeventtrigger/edit.md). Lastly, post the notice for that event to the highlight center.

```swift
// Post a change event notice.

let editEvent = SWHighlightChangeEvent(highlight: highlight, trigger: .edit)

highlightCenter.postNotice(for: editEvent)
```

##### Post a Persistence Event Notice

Use the [`SWHighlightPersistenceEvent`](swhighlightpersistenceevent.md) to post a notice when your app moves, renames, or deletes content on the server. In the example below, the [`SWHighlightPersistenceEventTrigger.renamed`](swhighlightpersistenceeventtrigger/renamed.md) trigger type signifies the document name has changed.

```swift
// Post a persistence event notice that shows your app renamed a document.

let renamedEvent = SWHighlightPersistenceEvent(highlight: highlight, trigger: .renamed)

highlightCenter.postNotice(for: renamedEvent)
```

##### Post a Membership Event Notice

When your app alters the membership for a collaboration and triggers a membership event, the system posts an update to the collaborators.

After your app retrieves the highlight, create the membership event by passing in the retrieved highlight. Use either [`SWHighlightMembershipEventTrigger.addedCollaborator`](swhighlightmembershipeventtrigger/addedcollaborator.md) or [`SWHighlightMembershipEventTrigger.removedCollaborator`](swhighlightmembershipeventtrigger/removedcollaborator.md) as the trigger for the [`SWHighlightMembershipEvent`](swhighlightmembershipevent.md).

```swift
// Post a membership event notice that shows your app added a collaborator.

let membershipEvent = SWHighlightMembershipEvent(highlight: highlight, trigger: .addedCollaborator)

highlightCenter.postNotice(for: membershipEvent)
```

If the membership of a Messages group changes, Shared with You keeps collaborators on your shared documents in sync. For CloudKit and iCloud Drive, your app doesn’t have to do anything.

![Two iPhones side by side both showing Messages conversations. The left iPhone has a notification with a profile icon and two lines of text to the right that say, Add Lauren to your 3 shared documents. To the right of the text is an oval Add button and a cancel x button. The right iPhone has a notification with a profile icon and two lines of text to the right that say Remove Chris from your 3 shared documents. To the right of the text is an oval “Remove” button and a cancel x button.](https://docs-assets.developer.apple.com/published/28ce0875b2762facf49404b2e0e34500/media-4085670%402x.png)

When a person adds someone new to a Messages conversation for a collaboration, the system prompts the document owner in Messages to add them to the share. When a person removes someone from a Messages conversation, the system prompts the document owner in Messages to remove them from the share.

## See Also

- [Adding custom collaboration to your app](adding-custom-collaboration-to-your-app.md)
  Integrate your custom collaboration app with Messages.
- [Collaboration views](collaboration-views.md)
  Create and customize a collaboration view to manage the shared content actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sharedwithyou/adding-shared-content-collaboration-to-your-app)*