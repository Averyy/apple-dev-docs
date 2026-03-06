# Presenting SharePlay activities from your app’s UI

**Framework**: Group Activities

Make it easy for people to start activities from your app’s UI, from the system share sheet, or using AirPlay over AirDrop.

#### Overview

After defining one or more SharePlay activities for your app, make them easy for people to discover in your UI. Include buttons, menu items, and other elements to start activities, present activities in system interfaces like the share sheet, and update your activities to take advantage of other system behaviors.

Starting an activity requires an active FaceTime call or Messages conversation. When a conversation is active, you can start an activity right away from your UI. If no conversation is active, the Group Activities framework facilitates starting a conversation as part of starting your activity. Some system features, like the share sheet, also help you start conversations. On visionOS, you can also share with people who are nearby. For more information, see [`Configure your visionOS app for sharing with people nearby`](configure-your-app-for-sharing-with-people-nearby.md).

For design guidance for adding SharePlay support to your app’s UI, see [`SharePlay`](https://developer.apple.com/design/Human-Interface-Guidelines/shareplay).

#### Add a Shareplay Button to Your Ui

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

When someone interacts with your app’s custom buttons, start the corresponding activity immediately if there is an active FaceTime call or Messages conversation. To determine if a conversation is active, check the [`isEligibleForGroupSession`](groupstateobserver/iseligibleforgroupsession.md) property of [`GroupStateObserver`](groupstateobserver.md). If the value of that property is `true`, call the [`prepareForActivation()`](groupactivity/prepareforactivation().md) or [`activate()`](groupactivity/activate().md) method of your [`GroupActivity`](groupactivity.md) type to start the activity. If the value of the property is `false`, present a `GroupActivitySharingController`, which prompts the person to invite friends to join the activity.

If the activity only makes sense in a group setting and you’re on an active FaceTime call or are sharing with people who are nearby on visionOS, you can directly start an activity by calling `activate()` on it:

```swift
struct BoardGameApp: App {
    let boardGame = BoardGame.chess

    var body: some View {
        BoardGameView()
        Button("Start activity") {
            Task { @concurrent in
                _ = try await BoardGameActivity(boardGame: boardGame).activate()
            }
        }
    }
}
```

#### Share Activities in Swiftui Using a Share Link

To surface SharePlay activities using the system share sheet in SwiftUI, configure a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view with items that have an associated activity. A [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view adds a standard share button to your UI, and you can customize the appearance of that button using the [`buttonStyle(_:)`](https://developer.apple.com/documentation/SwiftUI/View/buttonStyle(_:)-7qx1) modifier. Tapping or clicking the button displays the system share sheet for the provided items. A person can then use the sheet to copy the items to the pasteboard or send them to a different process.

To surface your SharePlay activities from a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view, ensure your [`GroupActivity`](groupactivity.md) type conforms to [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable). The share sheet in SwiftUI requires items to support the `Transferable` protocol.

For information on setting up the custom [`GroupActivity`](groupactivity.md) type, see [`Defining your app’s SharePlay activities`](defining-your-apps-shareplay-activities.md).

The following example creates a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) to share a board game activity. If someone is in a FaceTime call or sharing with nearby people on visionOS, tapping the `ShareLink` starts the `BoardGameActivity`. Otherwise, tapping the `ShareLink` displays the share sheet.

```swift
ShareLink(item: BoardGameActivity(boardGame: .chess), preview: SharePreview("Play Together"))
```

When your custom data types conform to `Transferable`, you can start an activity with an instance of your data type as well. The following example creates a `ShareLink` to share a game associated with the current view. When someone displays the share sheet and clicks the SharePlay link, the system initializes the app’s `BoardGameActivity` activity with the specified game and starts the activity.

```swift
let game = BoardGame.chess
// ...
ShareLink(item: game, preview: SharePreview("Play Together"))
```

#### Add Activities to the System Share Sheet in Appkit or Uikit

When displaying a share sheet using AppKit or UIKit, specify any SharePlay activities using [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects. When you configure the AppKit or UIKit share sheets, you specify one or more [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects with the data you want to share. If you have an activity you want to share for that item, create an instance of the appropriate [`GroupActivity`](groupactivity.md) type and pass it to the item provider’s [`registerGroupActivity(_:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/registerGroupActivity(_:)) method. When an item provider has a registered activity, the share sheet displays a SharePlay button to start the associated activity.

The following example creates a `BoardGameActivity` activity to allow friends to play a game together over SharePlay. After it creates an item provider for the game, it registers the activity with that item provider and displays the share sheet. When someone clicks the SharePlay button in the share sheet, the system starts the board game activity.

```swift
let activity = BoardGameActivity(boardGame: BoardGame.chess)
        
// Create an item provider for the activity.
let itemProvider = NSItemProvider() 
itemProvider.registerGroupActivity(activity)
        
// Create and present the share sheet.
let shareSheet = UIActivityViewController(activityItems: [itemProvider], applicationActivities: nil)
shareSheet.allowsProminentActivity = true
        
present(shareSheet, animated: true)
```

In AppKit, display the share sheet using an [`NSSharingServicePicker`](https://developer.apple.com/documentation/AppKit/NSSharingServicePicker) object. When creating the picker object, specify your [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects as the items you want to share.

#### Share Activities Using Shareplay Over Airdrop

SharePlay over AirDrop lets one person initiate an activity on their iPhone and share that activity with people in close proximity. The initiator opens an app on their iPhone and navigates to a page with the activity they want to start. When their iPhone comes in close proximity to other people’s iPhone devices, the initiator’s phone prompts them to start the activity. After they start the activity, the system prompts the other people to join and creates a Messages conversation for the group. Anyone in the group can then invite others to join the conversation and activity, including people who aren’t nearby.

In a SwiftUI app, the system enables SharePlay over AirDrop when the UI contains a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) with an appropriate activity. The activity you include in the link must conform to [`Transferable`](https://developer.apple.com/documentation/CoreTransferable/Transferable).

To support SharePlay over AirDrop in a UIKit app, assign activities to objects in the responder chain of your app’s UI. Typically, you add activities to your app’s view controllers, but you can add activities to any responder. When devices are nearby, the system searches the responder chain for a responder that contains an activity in its [`activityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfigurationProviding/activityItemsConfiguration) property. If an activity is available, the system displays UI to start that activity on the initiator’s device. The [`activityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfigurationProviding/activityItemsConfiguration) property stores one or more [`NSItemProvider`](https://developer.apple.com/documentation/Foundation/NSItemProvider) objects, which you configure with activities by calling the [`registerGroupActivity(_:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/registerGroupActivity(_:)) method.

#### Display Activities in the Share Menu in Visionos

In a visionOS app, the system displays a Share Window menu in the window bar to indicate when sharing is active. The system populates this control with activities the current scene supports. Immersive spaces don’t have a system UI by default to start an activity. You can add a window to your immersive space or create custom UI to start an activity. For an example, see [`Implementing SharePlay for immersive spaces in visionOS`](https://developer.apple.com/documentation/visionOS/implementing-shareplay-for-immersive-spaces-in-visionos).

**Not sharing**:

![An illustration of a window with a Share Window menu. The menu indicates that sharing is inactive.](https://docs-assets.developer.apple.com/published/287f847bc7983ce1cc94c4772172b74f/visionos-shareplay-status-idle%402x.png)

The Share Window menu is in the idle state, and sharing is not active for the window.

**Select an activity**:

![An illustration of a window with a Share Window menu. The person tapped the Share menu, which now shows the list of activities the person can start.](https://docs-assets.developer.apple.com/published/8ab9442f367dca0ac2566e97c246ff73/visionos-shareplay-share-action%402x.png)

The person chooses an activity from the Share Window menu.

**Sharing started**:

![An illustration of a window with a Share Window menu. The menu indicates that sharing is active.](https://docs-assets.developer.apple.com/published/d64c1d419186bcc7cc408020f3f7d773/visionos-shareplay-status-sharing%402x.png)

The Share Window menu is in the active state, and an activity is in progress.

Specify activities in any of the following ways:

- Include a [`ShareLink`](https://developer.apple.com/documentation/SwiftUI/ShareLink) view with a properly configured activity, as described in [`Share activities using SharePlay over AirDrop`](promoting-shareplay-activities-from-your-apps-ui#Share-activities-using-SharePlay-over-AirDrop.md). Apply [`hidden()`](https://developer.apple.com/documentation/SwiftUI/View/hidden()) to the `ShareLink` to hide the button from the view while showing the activity in the Share Window menu.
- Configure the [`activityItemsConfiguration`](https://developer.apple.com/documentation/UIKit/UIActivityItemsConfigurationProviding/activityItemsConfiguration) property of a UIKit responder object with an activity object.
- Associate an activity with the scene. For more information, see [`Adding spatial Persona support to an activity`](adding-spatial-persona-support-to-an-activity.md) and watch the WWDC25 session [`Share visionOS experiences with nearby people`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2025/318).

## See Also

- [class GroupActivitySharingController](groupactivitysharingcontroller-4gtfk.md)
  A macOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.
- [class GroupActivitySharingController](groupactivitysharingcontroller-ybcy.md)
  An iOS view controller that displays the system interface for starting an activity, and optionally starts a FaceTime call for that activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/groupactivities/promoting-shareplay-activities-from-your-apps-ui)*