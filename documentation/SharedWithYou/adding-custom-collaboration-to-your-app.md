# Adding custom collaboration to your app

**Framework**: Sharedwithyou

Integrate your custom collaboration app with Messages.

#### Overview

If your app uses iCloud to store shared content, you can use the steps in [`Adding shared content collaboration to your app`](adding-shared-content-collaboration-to-your-app.md) to add collaboration. To share content without using iCloud, the Shared with You framework provides an [`SWCollaborationMetadata`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata) object wrapped in [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) to implement a custom collaboration infrastructure.

Before you can use this collaboration infrastructure, your app needs to support universal links to share content with other apps. For more details about implementing universal links, see [`Making your app content shareable`](making-your-app-content-shareable.md).

![An illustration of a horizontal iPhone labeled Sending Device. At the top center of the device screen is an app icon with an arrow labeled Share pointing right to a rectangle labeled Collaboration Metadata. An arrow points down from that rectangle to a rectangle labeled Share Sheet/Drag & Drop. From there, an arrow points left to a Messages app icon. The app icon at the top also has a line pointing left and down to two stacked rectangles. The top rectangle is labeled Universal Link and the bottom one is labeled Identifier. The bottom rectangle has an arrow pointing down and right to the Messages app icon. An arrow points up from the Messages app icon to a square with a ? in it. That square has an arrow pointing up to the app icon. The app icon has an arrow pointing up to a square with a ? in it that sits above the device. The square above the device has an arrow pointing right to a Server icon.](https://docs-assets.developer.apple.com/published/3901cbcbc6321c17cec79fa745082f0f/media-4110288%402x.png)

> **Note**:  Session 10093: [`Integrate your custom collaboration app with Messages`](https://developer.apple.comhttps://developer.apple.com/wwdc22/10093)

##### Create the Metadata Object

When a user decides to share a collaboration from your app through the Messages app, you first create metadata to represent the content. The metadata includes share options the user can configure prior to sending the message, and many other properties you can customize. Next, you provide that metadata to the share sheet, or to drag and drop using the steps below in the “Present a collaboration view” section.

The string you pass to [`SWLocalCollaborationIdentifier`](https://developer.apple.com/documentation/sharedwithyoucore/swlocalcollaborationidentifier) doesn’t need to be unique across devices, it’s only for your app to use locally. Similarly, the system displays the initiator’s account handle and name that your app retrieves from [`personNameComponents(from:)`](https://developer.apple.com/documentation/foundation/personnamecomponentsformatter/1642979-personnamecomponents) locally so the collaborator can confirm their account.

```swift
// Configure the SWCollaborationMetadata.

let localIdentifier = SWLocalCollaborationIdentifier(rawValue: "identifier")
let metadata = SWCollaborationMetadata(localIdentifier: localIdentifier)
metadata.title = "Content Title"
metadata.initiatorHandle = "user@example.com"

let formatter = PersonNameComponentsFormatter()
if let components = formatter.personNameComponents(from: "Devin") {
    metadata.initiatorNameComponents = components
}
```

After your app sets the identifier and initiator for the metadata, configure [`SWCollaborationShareOptions`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationshareoptions). Share options are the settings a person configures on the collaboration in Messages or the share sheet. Options represent individual switches, or mutually exclusive values for a setting. Options have a title and an identifier, and are either in a selected or an unselected state.

There are two classes to represent a group of options: [`SWCollaborationOptionsGroup`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoptionsgroup) and [`SWCollaborationOptionsPickerGroup`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationoptionspickergroup). Use `SWCollaborationOptionsGroup` to represent a collection of switches, and use `SWCollaborationOptionsPickerGroup` to represent mutually exclusive values for a setting.

In the example below, a person can choose either the “Can make changes” or the “Read only” option. The collaborator can choose “Allow mentions” and the “Allow comments” options independent of each other. The app then passes both the option groups to `SWCollaborationShareOptions` to initialize the [`defaultShareOptions`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata/defaultshareoptions).

```swift
// Configure the SWCollaborationShareOptions.

let permission = SWCollaborationOptionsPickerGroup(identifier: UUID().uuidString, 
                                                   options: [
    SWCollaborationOption(title: "Can make changes", identifier: UUID().uuidString),
    SWCollaborationOption(title: "Read only", identifier: UUID().uuidString)
])
permission.options[0].isSelected = true
permission.title = "Permission"

let additionalOptions = SWCollaborationOptionsGroup(identifier: UUID().uuidString, 
                                                    options: [
    SWCollaborationOption(title: "Allow mentions", identifier: UUID().uuidString),
    SWCollaborationOption(title: "Allow comments", identifier: UUID().uuidString)
])
additionalOptions.title = "Additional Settings"
let optionsGroups = [permission, additionalOptions]
metadata.defaultShareOptions = SWCollaborationShareOptions(optionsGroups: optionsGroups)
```

##### Present a Collaboration View

If your app uses SwiftUI, [`SWCollaborationMetadata`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata) is compatible with the [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable) protocol and the [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view. In the example below, the app defines a `Transferable` model object and creates a [`ProxyRepresentation`](https://developer.apple.com/documentation/CoreTransferable/ProxyRepresentation) to return a collaboration metadata instance. Then, the app passes that model object to a `ShareLink` instance in the view.

```swift
// Configure the SwiftUI TransferRepresentation object.

struct CustomCollaboration: Transferable {
    var name: String

    static var transferRepresentation: some TransferRepresentation {
        ProxyRepresentation { customCollaboration in
            SWCollaborationMetadata(
                localIdentifier: .init(rawValue: "com.example.customcollaboration"),
                title: customCollaboration.name,
                defaultShareOptions: nil,
                initiatorHandle: "johnappleseed@apple.com",
                initiatorNameComponents: nil
            )
        }
    }
}

// Initialize ShareLink with the custom collaboration model object.

struct ContentView: View {
    var body: some View {
        ShareLink(item: CustomCollaboration(name: "Example"), preview: .init("Example"))
    }
}
```

It’s good practice to register multiple representations of the content to support sharing through as many channels as possible. For example, Messages automatically offers an option to send the content as a copy if you provide a file representation.

For UIKit and AppKit apps, use [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) to support content sharing. `SWCollaborationMetadata` conforms to the [`NSItemProviderReading`](https://developer.apple.com/documentation/Foundation/NSItemProviderReading) and [`NSItemProviderWriting`](https://developer.apple.com/documentation/Foundation/NSItemProviderWriting) protocols, so you can register a metadata instance with an item provider to support collaboration. Use `NSItemProvider` with [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController) and [`UIDragItem`](https://developer.apple.com/documentation/UIKit/UIDragItem) in iOS and iPadOS, and [`NSSharingServicePicker`](https://developer.apple.com/documentation/AppKit/NSSharingServicePicker) in macOS.

In the example code below, the app registers the collaboration metadata in an `NSItemProvider` instance. Then the app creates a [`UIActivityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfiguration) object with the item provider object and passes that to the `UIActivityViewController`. Finally, the app presents the share sheet.

```swift
// Present the iOS share sheet.

func presentActivityViewController(metadata: SWCollaborationMetadata) {
    let itemProvider = NSItemProvider()
    itemProvider.registerObject(metadata, visibility: .all)
    let activityConfig = UIActivityItemsConfiguration(itemProviders: [itemProvider])
    let shareSheet = UIActivityViewController(activityItemsConfiguration: activityConfig)
    present(shareSheet, animated: true)
}
```

To support drag and drop in iOS, initialize `NSItemProvider` and register the metadata the same way as in the previous code example, then create a [`UIDragItem`](https://developer.apple.com/documentation/UIKit/UIDragItem) with the item provider.

```swift
// Support iOS drag and drop.

func createDragItem(metadata: SWCollaborationMetadata) -> UIDragItem {
    let itemProvider = NSItemProvider()
    itemProvider.registerObject(metadata, visibility: .all)
    return UIDragItem(itemProvider: itemProvider)
}
```

The API is similar in macOS for the sharing popover. Use the item provider to initialize an [`NSSharingServicePicker`](https://developer.apple.com/documentation/AppKit/NSSharingServicePicker) object and show the picker relative to a target view.

```swift
// Show the macOS sharing popover.

func showSharingServicePicker(view: NSView, metadata: SWCollaborationMetadata) {
    let itemProvider = NSItemProvider()
    itemProvider.registerObject(metadata, visibility: .all)
    let picker = NSSharingServicePicker(items: [itemProvider])
    picker.show(relativeTo: view.bounds, of: view, preferredEdge: .minY)
}
```

To support drag and drop in macOS, use [`NSPasteboardItem`](https://developer.apple.com/documentation/AppKit/NSPasteboardItem) instead of `NSItemProvider`. Assign the collaboration metadata to [`collaborationMetadata`](https://developer.apple.com/documentation/AppKit/NSPasteboardItem/collaborationMetadata) on a new `NSPasteboardItem` instance.

```swift
// Support macOS drag and drop.

func createPasteboardItem(metadata: SWCollaborationMetadata) -> NSPasteboardItem {
    let pasteboardItem = NSPasteboardItem()
    pasteboardItem.collaborationMetadata = metadata
    return pasteboardItem
}
```

The system stages a draft of your collaborative content in Messages. After a person taps the Send button, the system coordinates with your app to create the share.

##### Prepare the Collaboration Coordinator

`SWCollaborationCoordinator` is a singleton, meaning there’s a global shared instance that your app uses to respond to action requests. Your app defines an action handler that conforms to the [`SWCollaborationActionHandler`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationactionhandler) protocol. Because the collaboration coordinator runs in the background and can send requests for actions to your app at any time, define your action handler early in the launch process. The app in the example below registers the handler in the [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)) method:

```swift
// Assign your action handler to the SWCollaborationCoordinator.

private let collaborationCoordinator = SWCollaborationCoordinator.shared

func application(_ application: UIApplication, didFinishLaunchingWithOptions launchOptions: [UIApplication.LaunchOptionsKey : Any]?) -> Bool {
    // Conform to the SWCollaborationActionHandler protocol.
    collaborationCoordinator.actionHandler = self
}

```

Your action handler is responsible for responding to [`SWAction`](https://developer.apple.com/documentation/sharedwithyoucore/swaction) requests from the system. An `SWAction` represents work your app needs to handle during a collaboration. Your app calls [`fulfill()`](https://developer.apple.com/documentation/sharedwithyoucore/swaction/fulfill()) after it completes a request. If your app can’t complete an action, it responds with [`fail()`](https://developer.apple.com/documentation/sharedwithyoucore/swaction/fail()). It’s important to respond to `SWAction` requests quickly to avoid a system timeout.

The example code below retrieves the [`localIdentifier`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata/localidentifier) and [`userSelectedShareOptions`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata/userselectedshareoptions) from the [`SWCollaborationMetadata`](https://developer.apple.com/documentation/sharedwithyoucore/swcollaborationmetadata) in the action. The `APIRequest` object in this example is the API for processing collaboration requests on a web server.

```swift
// Handle a system request for an SWStartCollaborationAction.

func collaborationCoordinator(_ coordinator: SWCollaborationCoordinator, 
                              handle action: SWStartCollaborationAction) {
    let localID = action.collaborationMetadata.localIdentifier.rawValue
    let selectedOptions = action.collaborationMetadata.userSelectedShareOptions
    let prepareRequest = APIRequest.PrepareCollaboration(localID: localID, selectedOptions)
    Task {
        do {            
            let response = try await apiController.send(request: prepareRequest)
            let identifier = response.deviceIndependentIdentifier
            action.fulfill(using: response.url, collaborationIdentifier: identifier)
        } catch {
            Log.error("Caught an error while preparing the collaboration: \(error)")
            action.fail() // Cancels the message.
        }
    }
}

```

If the [`SWStartCollaborationAction`](https://developer.apple.com/documentation/sharedwithyoucore/swstartcollaborationaction) is successful, the system sends your app a second action to update the collaboration participants. Before you can add or remove participants, your app needs to have a way to verify participants.

##### Verify Participant Access

The [`SWUpdateCollaborationParticipantsAction`](https://developer.apple.com/documentation/sharedwithyoucore/swupdatecollaborationparticipantsaction) contains the cryptographic identities for the participants. The system derives the identities from the collaboration identifier that `SWStartCollaborationAction` provides. Your shared content server is responsible for identity storage and verification of recipient devices.

To verify a participant, use the [`SWPerson.Identity`](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identity) [`rootHash`](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identity/roothash) property. A root hash is a secure value your app sends to your server to uniquely identify a participant on their devices. To perform a verification, your server needs to compute a root hash.

When the system sends a collaboration message for a participant, it actually sends individual messages to each device for that participant. The Messages app identifies each device using a cryptographic public key. Because the goal is to allow access only on this participant’s set of devices, the system derives the root hash from the set of public keys registered to each recipient.

The root hash is the root node of a data structure called a . A Merkle tree is a binary tree that the system builds by performing a sequence of hashing operations. To derive an identity for the participant based on their public keys, the system uses the keys as the  of this tree. The hashing algorithm that the system uses in the Merkle tree ensures that the system can only compute the root node from that set of keys.

In the example below, the user has three devices and three public keys. The keys are unique for each collaboration identifier that your app provides, using a process called key diversification. To prevent tracking the number of devices registered to a user, the system pads the set with random keys up to a fixed size. Your server hashes the padded set of diversified keys to create the leaf nodes of the tree with a SHA-256 algorithm.

![A tree diagram of rectangles and connecting lines that represent nodes and their relationships. The node at the top is labeled with a hexidecimal hash number and has two nodes below it labeled H10 and H11. The H10 node on the left has two nodes below it labeled H7 and H8. Node H7 has two nodes below it labeled H1 and H2. H1 has a dimmed rectangle below it labeled P1. H2 has a dimmed rectangle below it labeled P2. Node H8 has two nodes below it labeled H3 and H4. H3 has a dimmed rectangle below it labeled P3. H4 has a dimmed rectangle below it labeled R1. Node H11 has a node below it labeled H9. Node H9 has two nodes below it labeled H5 and H6. H5 has a dimmed rectangle below it labeled R2. H6 has a dimmed rectangle below it labeled R3.](https://docs-assets.developer.apple.com/published/a23d8777e31365b9627c4cdba003556b/media-4110140%402x.png)

Your server then concatenates and hashes each pair of leaf nodes to derive their predecessor nodes. Repeat this process with the predecessor nodes until a single root node remains. This is the root hash that the system uses to uniquely represent this recipient’s identity across their devices.

The figure below shows that it’s possible to generate a root hash using a subset of the nodes from a complete Merkle tree. Your server can use the hashes H4, H7, and H11, along with the diversified public key P3, to reproduce the root hash in this tree. First, hash the public key to get the missing leaf node H3. Then use H3 and H4 to generate H8. Next, use the given H7 node with H8 to generate H10. Finally, use H10 and H11 to produce the root hash.

![A tree diagram of rectangles and connecting lines that represent nodes and their relationships. Green nodes represent a known device. Orange represents a calculated node. Unknown devices are dimmed. The node at the top is orange and labeled with a hexidecimal hash number and has two nodes below it labeled H10 and H11. The H10 node on the left is orange and has two nodes below it labeled H7 and H8. Node H7 is green and has two dimmed nodes below it labeled H1 and H2. H1 has a dimmed rectangle below it labeled P1. H2 has a dimmed rectangle below it labeled P2. H3 has a dimmed rectangle below it labeled P3. H4 has a dimmed rectangle below it labeled R1. The H8 node is orange and has two nodes below it labeled H3 and H4. H3 is orange and has a green rectangle below it labeled P3. H4 has a dimmed rectangle below it labeled R1. The H11 node is green and has a node below it labeled H9. The H9 node is dimmed and has two dimmed nodes below it labeled H5 and H6. H5 has a dimmed rectangle below it labeled R2. H6 has a dimmed rectangle below it labeled R3.](https://docs-assets.developer.apple.com/published/b91b4a58d6e501c0632c863326585769/media-4110141%402x.png)

It’s important to note that you can prove the system uses the public key P3 to generate a given root hash, without needing to reconstruct the entire tree. The subset of nodes necessary to do this is a proof of inclusion. Verification begins when your app opens a universal link. To do this, you first need to check that the link is collaborative.

##### Verify a Collaboration Link

[`SWCollaborationHighlight`](swcollaborationhighlight.md) represents a collaborative link that your app retrieves from [`SWHighlightCenter`](swhighlightcenter.md). Use that collaboration highlight to generate the proof of inclusion. To represent a proof of inclusion, use [`SWPerson.IdentityProof`](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identityproof). To perform verification, first generate this object along with a cryptographic signature to send to your server. Retrieve the proof using the [`getSignedIdentityProof(for:using:completionHandler:)`](swhighlightcenter/getsignedidentityproof(for:using:completionhandler:).md) method on `SWHighlightCenter`.

Use the signature to ensure that a bad actor can’t send the request to gain access to your collaboration. The data can be a challenge you request from your server, or a nonce that the device generates. The example below uses the challenge approach.

The system passes the URL, which is the universal link associated with a collaboration, to [`application(_:didFinishLaunchingWithOptions:)`](https://developer.apple.com/documentation/UIKit/UIApplicationDelegate/application(_:didFinishLaunchingWithOptions:)). Use this URL to fetch the associated `SWCollaborationHighlight` from the `SWHighlightCenter`.

Request the challenge from the server, and pass the returned data to the `getSignedIdentityProof` method on `SWHighlightCenter`, along with the highlight. This method returns a signed identity proof that the app sends to the server for verification.

The app sends the proof to the server, along with the public key and the signed data. Your app signs the data using the Elliptic Curve Digital Signature Algorithm over the P-256 elliptic curve. Verify the signature on the data using the public key in the identity proof. You can do this with most common encryption libraries.

```swift
// Retrieve a signed identity proof for a highlight.

func application(_ app: UIApplication, open url: URL, 
               options: [UIApplication.OpenURLOptionsKey : Any] = [:]) -> Bool {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let challengeRequest = APIRequest.GetChallengeData()
    Task {
        do {
            let highlight = try highlightCenter.collaborationHighlight(for: url)
            let challenge = try await apiController.send(request: challengeRequest)
            let proof = try await highlightCenter.getSignedIdentityProof(for: highlight, 
                                                                       using: challenge.data)
    let proofOfInclusionRequest = APIRequest.SubmitProofOfInclusion(for: proof)
            let result = try await apiController.send(request: proofOfInclusionRequest)
            documentController.update(currentDocument, with: result)
        } catch {
            Log.error("Caught an error while generating the proof of inclusion: \(error)")
        }
    }
}
```

After you verify the signature, you can trust that the identity proof the system sends is from the device associated with that public key. Next, use the identity proof to recompute the root hash. A recursive algorithm works well with tree data structures, as in the code example below:

```swift
// Recursive code for root hash generation.

func generateRootHashFromArray(localHash: SHA256Digest, inclusionHashes: [SHA256Digest], 
                       publicKeyIndex: Int) -> SHA256Digest {
    guard let firstHash = inclusionHashes.first else { return localHash }
    // Check whether the node is the left or the right successor.
    let isLeft = publicKeyIndex.isMultiple(of: 2)
    // Calculate the combined hash.
    var rootHash: SHA256Digest
    if isLeft {
        rootHash = hash(concatenate([localHash, firstHash]), using: .sha256)
    } else {
        rootHash = hash(concatenate([firstHash, localHash]), using: .sha256)
    }
    // Recursively pass in elements and move up the Merkle tree.
    let newInclusionHashes = inclusionHashes.dropFirst()
    rootHash = generateRootHashFromArray(
        localHash: rootHash,
        inclusionHashes: Array(newInclusionHashes),
        publicKeyIndex: (publicKeyIndex / 2)
    )
    return rootHash
}
```

On the initial invocation, pass in the hash of the public key, the set of inclusion hashes, and the public key index. Next, remove the first inclusion hash. Check the public key index to see whether the key is on the left or the right of its sibling. Concatenate and hash the selected hashes in the correct order. Next, remove the consumed node in the `inclusionHashes` array, and pass the rest to a recursive call to this same function. The public key index then updates so that it’s ready for the next node in the tree.

With this simple function, you can quickly compute a root hash given an identity proof. The server can check that this generated root hash is in the list of root hashes the owner of the document uploads during sending. The hash is present in the list of known hashes, so the server can grant access to the document.

Next, sign some data and retrieve the proof of inclusion. Send the signed data and proof to your server. Verify the signature on the data. Using the proof of inclusion, generate the root hash. Finally, compare the root hash to the list of known identities associated with that content.

##### Add a Participant

The example below shows how to handle the update participants action. First, retrieve the collaboration identifier from the action’s metadata — this is the identifier you supply to the [`fulfill()`](https://developer.apple.com/documentation/sharedwithyoucore/swaction/fulfill()) method while handling `SWStartCollaborationAction`.

Next, use the action’s [`addedIdentities`](https://developer.apple.com/documentation/sharedwithyoucore/swupdatecollaborationparticipantsaction/addedidentities) property to retrieve the participant data to store on your content server. Each identity has a [`rootHash`](https://developer.apple.com/documentation/sharedwithyoucore/swperson/identity/roothash) property, which is the data you store on your server to validate participants during the collaboration process.

After you retrieve this data, create another server request to add the participants to the collaboration with the target identifier. Then, send the request to your server, and fulfill or fail the action. This time, the fulfill method doesn’t take any parameters. After you set up the collaboration, your app has everything it needs to grant immediate access to the recipients of the message.

```swift
// Add a participant.

func collaborationCoordinator(_ coordinator: SWCollaborationCoordinator, 
                              handle action: SWUpdateCollaborationParticipantsAction) {
    let identifier = action.collaborationMetadata.collaborationIdentifier
    let participants: [Data] = action.addedIdentities.compactMap { $0.rootHash }
    let addParticipants = APIRequest.AddParticipants(identifier: identifier, participants)
    Task {
        do {            
            try await apiController.send(request: addParticipants)
            action.fulfill() // Sends the URL that the start action provides.
        } catch {
            Log.error("Caught an error while adding participants to the collaboration: \(error)")
            action.fail() // Cancels the message.
        }
    }
}
```

##### Remove a Participant

To remove a participant, look up any account associated with a removed identity and revoke their access. If your app doesn’t have any associated accounts for this collaboration, delete the root hash from your database. The example code below uses the [`removedIdentities`](https://developer.apple.com/documentation/sharedwithyoucore/swupdatecollaborationparticipantsaction/removedidentities) property on the action and passes it to a similar removal API request:

```swift
// Remove a participant.

func collaborationCoordinator(_ coordinator: SWCollaborationCoordinator, 
                              handle action: SWUpdateCollaborationParticipantsAction) {
    // This is an example of removing participants only. Handle the added identities here too.
    let identifier = action.collaborationMetadata.collaborationIdentifier
    let removed: [Data] = action.removedIdentities.compactMap { $0.rootHash }
    let removeParticipants = APIRequest.RemoveParticipants(identifier: identifier, removed)
    Task {
        do {            
            try await apiController.send(request: removeParticipants)
            action.fulfill()
        } catch {
            log.error("Caught an error while adding participants to the collaboration: \(error)")
            action.fail()
        }
    }
}
```

##### Post a Change Event Notice

When a participant makes changes to a collaboration, your app posts notices about those changes. The system displays those notices in Messages as a banner in the shared conversation. The banner includes a description of the changes, as well as the name of the person who makes each change.

Your app posts a change event for content updates or comments, and it posts a membership event when a participant joins or leaves. When a person mentions another person in a collaboration, post a mention event. Post a persistence event when a collaborator moves or deletes content. The example code below shows how to post a change event for an edit to a collaboration:

```swift
// Post a change event notice.

func postContentEditEvent(identifier: SWCollaborationIdentifier) throws {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let editEvent = SWHighlightChangeEvent(highlight: highlight, trigger: .edit)

    highlightCenter.postNotice(for: editEvent)
}
```

##### Post a Membership Event Notice

For participant changes, your app posts a membership event and passes either the [`SWHighlightMembershipEventTrigger.addedCollaborator`](swhighlightmembershipeventtrigger/addedcollaborator.md) or [`SWHighlightMembershipEventTrigger.removedCollaborator`](swhighlightmembershipeventtrigger/removedcollaborator.md) trigger type.

```swift
// Post a membership event notice.

func postMembershipEvent(identifier: SWCollaborationIdentifier) throws {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let membershipEvent = SWHighlightMembershipEvent(highlight: highlight, trigger: .addCollaborator)

    highlightCenter.postNotice(for: membershipEvent)
}
```

##### Post a Mention Event Notice

If your app supports user mentions, you can post a mention event. Initialize a person identity with the root hash of the mentioned user. Next, pass the mentioned identity to [`SWHighlightMentionEvent`](swhighlightmentionevent.md) and post the mention event.

The system shows this notice only to the mentioned user in the Messages app.

```swift
// Post a mention event notice.

func postMentionEvent(identifier: SWCollaborationIdentifier, mentionedRootHash: Data) throws {
    let mentionedIdentity = SWPerson.Identity(rootHash: mentionedRootHash)

    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let mentionEvent = SWHighlightMentionEvent(highlight: highlight,
                                               mentionedPersonIdentity: mentionedIdentity)
    highlightCenter.postNotice(for: mentionEvent)
}
```

##### Post a Persistence Event Notice

Your app posts the persistence event type when a participant moves, renames, or deletes content. In the example below, the app uses [`SWHighlightPersistenceEventTrigger.renamed`](swhighlightpersistenceeventtrigger/renamed.md) to indicate that the participant changed the name of the content:

```swift
// Post a persistent event notice.

func postContentRenamedEvent(identifier: SWCollaborationIdentifier) throws {
    let highlightCenter: SWHighlightCenter = self.highlightCenter
    let highlight = try highlightCenter.collaborationHighlight(forIdentifier: identifier)

    let renamedEvent = SWHighlightPersistenceEvent(highlight: highlight, trigger: .renamed)
    highlightCenter.postNotice(for: renamedEvent)
}
```

## See Also

- [Adding shared content collaboration to your app](adding-shared-content-collaboration-to-your-app.md)
  Manage shared content collaboration in your app using CloudKit and iCloud Drive.
- [Collaboration views](collaboration-views.md)
  Create and customize a collaboration view to manage the shared content actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/SharedWithYou/adding-custom-collaboration-to-your-app)*