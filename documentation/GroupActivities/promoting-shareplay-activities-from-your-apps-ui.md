# Presenting SharePlay activities from your app’s UI

**Framework**: Group Activities

Make it easy for people to start activities from your app’s UI, from the system share sheet, or using AirPlay over AirDrop.

#### Overview

After you define one or more SharePlay activities for your app, make them easy for people to discover in your UI. Include buttons, menus items, and other elements to start activities, present activities in system interfaces like the share sheet, and update your activities to take advantage of other system behaviors.

Starting an activity requires an active FaceTime call or Messages conversation. When a conversation is active, you can start an activity right away from your UI. If no conversation is active, the Group Activities framework facilitates starting a conversation as part of starting your activity. Some system features also help you start conversations.

For guidance about the best ways to add SharePlay support to your app’s UI, see [`SharePlay`](https://developer.apple.com/design/Human-Interface-Guidelines/shareplay).

##### Add a Shareplay Button to Your Ui

The most direct way to start activities is to provide controls in your UI. Because you control the placement of buttons and other controls in your UI, you can put them where people are most likely to find them. Provide a label or additional context to let someone know that your UI element starts an activity. For example, update your button’s label to include the `shareplay` symbol from the SF Symbols library.

![An illustration of a button with the SharePlay logo and the title Start Activity.](https://docs-assets.developer.apple.com/published/5553739ef9075e1c1f6430a4e9cd418d/shareplay-start-activity-button%402x.png)

The following example shows a SwiftUI button with both a text label and the SharePlay icon:

```swift
Button {
    // Start the activity.
} label: {
    Label("Start Activity", systemImage: "shareplay")
}
.buttonStyle(.borderedProminent)
```

In iOS, the preceding example creates a button with a prominent appearance as shown below. When creating buttons in your app, use a style that makes sense for the current platform and your app’s design.

![An illustration of an app on iPhone displaying a button with the SharePlay logo and the label Start Activity in the app's UI.](https://docs-assets.developer.apple.com/published/15a0ca6da3969598c486b839d4842393/group-activities-shareplay-button%402x.png)

When someone interacts with your app’s custom buttons, start the corresponding activity immediately if there is an active FaceTime call or Messages conversation. To determine if a conversation is active, check the [`isEligibleForGroupSession`](groupstateobserver/iseligibleforgroupsession.md) property of [`GroupStateObserver`](groupstateobserver.md). If the value of that property is true, call the [`prepareForActivation()`](groupactivity/prepareforactivation().md) or [`activate()`](groupactivity/activate().md) method of your [`GroupActivity`](groupactivity.md) type to start the activity. If the value of the property is `false`, present a `GroupActivitySharingController`, which prompts the person to invite friends to join the activity.

##### Share Activities in Swiftui Using a Share Link

To surface SharePlay activities using the system share sheet in SwiftUI, configure a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view with items that have an associated activity. A [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view adds a standard share button to your UI, and you can customize the appearance of that button using the [`buttonStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/buttonStyle(_:)-7qx1) modifier. Tapping or clicking the button displays the system share sheet for the provided items. A person can then use the sheet to copy the items to the pasteboard or send them to a different process.

To surface your SharePlay activities from a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view, include a representation that contains your [`GroupActivity`](groupactivity.md) type. The share sheet in SwiftUI requires items to support the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol. Adopt this protocol in your custom data types and implement the [`transferRepresentation`](https://developer.apple.com/documentation/CoreTransferable/Transferable/transferRepresentation) property. Use that property to supply the representations of your data, and add a [`GroupActivityTransferRepresentation`](groupactivitytransferrepresentation.md) type to specify the [`GroupActivity`](groupactivity.md) for that data.

The following example shows the implementation of a movie data type and its [`transferRepresentation`](https://developer.apple.com/documentation/CoreTransferable/Transferable/transferRepresentation) property. The property returns two representations: one for the movie’s URL and one for the movie-watching activity. The closure for the [`GroupActivityTransferRepresentation`](groupactivitytransferrepresentation.md) creates the `WatchMovieTogether` activity and initializes it with the selected movie.

```swift
struct Movie : Transferable {
    var title : String
    var url: URL

    static var transferRepresentation: some TransferRepresentation {
        // Export the movie as a URL.
        ProxyRepresentation(exporting: \.url) 
        
        // Specify the associated SharePlay activity.
        GroupActivityTransferRepresentation { movie in
            WatchMovieTogether(from: movie)
        }
    }
}
```

The following example creates a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) to share a movie associated with the current view. When someone displays the share sheet and clicks the SharePlay link, the system initializes the app’s `WatchMovieTogether` activity with the specified movie and starts the activity.

```swift
ShareLink(item: movie,
          preview: .init("Play the movie together"))
```

##### Add Activities to the System Share Sheet in Uikit or Appkit

When displaying a share sheet using UIKit or AppKit, specify any SharePlay activities using [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects. When you configure the UIKit or AppKit share sheets, you specify one or more [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects with the data you want to share. If you have an activity you want to share for that item, create an instance of the appropriate [`GroupActivity`](groupactivity.md) type and pass it to the item provider’s [`registerGroupActivity(_:)`](https://developer.apple.com/documentation/foundation/nsitemprovider/3920459-registergroupactivity) method. When an item provider has a registered activity, the share sheet displays a SharePlay button to start the associated activity.

The following example creates a `WatchMovieTogether` activity to allow friends to watch a movie over SharePlay. After it creates an item provider for the movie, it registers the activity with that item provider and displays the share sheet. When someone clicks the SharePlay button in the share sheet, the system starts the movie-watching activity.

```swift
let activity = WatchMovieTogether(movie: movie)
        
// Create an item provider for the activity.
if let itemProvider = NSItemProvider(contentsOf: movie.url) {
    itemProvider.registerGroupActivity(activity)
            
    // Create and present the share sheet.
    let shareSheet = UIActivityViewController(activityItems: [itemProvider], applicationActivities: nil)
    shareSheet.allowsProminentActivity = true
            
    present(shareSheet, animated: true)
}
```

In AppKit, display the share sheet using an [`NSSharingServicePicker`](https://developer.apple.com/documentation/AppKit/NSSharingServicePicker) object. When creating the picker object, specify your [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects as the items you want to share.

##### Share Activities Using Shareplay Over Airdrop

SharePlay over AirDrop lets one person initiate an activity on their iPhone and share that activity with people in close proximity. The initiator opens an app on their iPhone and navigates to a page with the activity they want to start. When their iPhone comes in close proximity to other people’s iPhone devices, the initiator’s phone prompts them to start the activity. After they start the activity, the system prompts the other people to join and creates a Messages conversation for the group. Anyone in the group can then invite others to join the conversation and activity, including people who aren’t nearby.

In a SwiftUI app, the system enables SharePlay over AirDrop when the UI contains a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) with an appropriate activity. The activity you include in the link must adopt the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol and provide a [`GroupActivityTransferRepresentation`](groupactivitytransferrepresentation.md) type in its set of representations.

To support SharePlay over AirDrop in a UIKit app, assign activities to objects in the responder chain of your app’s UI. Typically, you add activities to your app’s view controllers, but you can add activities to any responder. When devices are nearby, the system searches the responder chain for a responder that contains an activity in its [`activityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfigurationProviding/activityItemsConfiguration) property. If an activity is available, the system displays UI to start that activity on the initiator’s device. The [`activityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfigurationProviding/activityItemsConfiguration) property stores one or more [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects, which you configure with activities by calling the [`registerGroupActivity(_:)`](https://developer.apple.com/documentation/foundation/nsitemprovider/3920459-registergroupactivity) method.

##### Display Activities in the Share Menu in Visionos

In a visionOS app, the system displays a Share menu above windows and volumes to indicate when sharing is active. The system populates this control with activities the current scene supports.

Specify activities in any of the following ways:

- Include a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view with a properly configured activity, as described in [`Share activities using SharePlay over AirDrop`](promoting-shareplay-activities-from-your-apps-ui#Share-activities-using-SharePlay-over-AirDrop.md).
- Configure the [`activityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfigurationProviding/activityItemsConfiguration) property of a UIKit responder object with an activity object.
- Associate an activity with the scene. See [`Adding spatial Persona support to an activity`](adding-spatial-persona-support-to-an-activity.md).

## See Also

- [class GroupActivitySharingController](groupactivitysharingcontroller-4gtfk.md)
  A macOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.
- [class GroupActivitySharingController](groupactivitysharingcontroller-ybcy.md)
  An iOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/promoting-shareplay-activities-from-your-apps-ui)*