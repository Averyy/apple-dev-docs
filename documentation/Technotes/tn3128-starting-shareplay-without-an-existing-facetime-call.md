# TN3128: Starting SharePlay without an existing FaceTime call

**Framework**: Technotes

Use the share sheet or group activity sharing controller to start SharePlay directly from your app without an existing FaceTime call.

#### Overview

With the [`Group Activities`](https://developer.apple.com/documentation/GroupActivities) framework in iOS 15.4 and iPadOS 15.4 and later, you can use the share sheet to start SharePlay experiences directly from your app without an existing FaceTime call.

You can make this same SharePlay experience even better by registering a group activity on an item provider and passing the item provider to the share sheet. Then when you select SharePlay the FaceTime call starts with an activity.

If you don’t use the share sheet, you can implement a custom user interface to bring up the [`GroupActivitySharingController`](https://developer.apple.com/documentation/GroupActivities/GroupActivitySharingController-ybcy) and start SharePlay directly from your app without a FaceTime call.

#### Display the Shareplay Button in the Share Sheet

An app doesn’t need to adopt any special APIs to display the SharePlay button in the share sheet. If the app has the [`com.apple.developer.group-session`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.group-session) entitlement, the share sheet displays the SharePlay button automatically. Simply present the share sheet as follows:

```swift
let shareSheet = UIActivityViewController(activityItemsConfiguration: configuration)
// Present the share sheet.
present(shareSheet, animated: true)
```

For example:

![A screenshot of an app that displays the SharePlay button in the share sheet.](https://docs-assets.developer.apple.com/published/fbedfdd155ed9dc3885a86583274631f/tn3128-share_sheet%402x.png)

Tap the SharePlay button, and select a person in the people-picker. Then tap the FaceTime button to start a FaceTime call with SharePlay directly from within the app.

#### Improve the Shareplay Experience in the Share Sheet

Displaying the SharePlay button in the share sheet as just described allows you to initiate a FaceTime call without an activity to start. You must interact with the app again to pick the content to SharePlay.

You can improve this same SharePlay experience by using  [`registerGroupActivity(_:)`](https://developer.apple.com/documentation/Foundation/NSItemProvider/registerGroupActivity(_:)) to register a group activity on the item provider, provide the item provider to the share sheet, and present the share sheet. That way, the FaceTime call starts with an activity.

```swift
// Register your group activity.
let itemProvider = NSItemProvider()
itemProvider.registerGroupActivity(WatchTogether())

// Provide the item provider to the share sheet.
let configuration = UIActivityItemsConfiguration(itemProviders:[itemProvider])

// Present the share sheet.
let shareSheet = UIActivityViewController(activityItemsConfiguration:configuration)
present(shareSheet, animated: true)
```

Here’s an example implementation:

![A screenshot of an app that displays a group activity and the SharePlay button in the share sheet.](https://docs-assets.developer.apple.com/published/bb1be328149c63734d7665c294abaf82/tn3128-share_sheet_improved%402x.png)

#### Display the Shareplay Button Less Prominently

Tune the presentation behavior of the SharePlay button in the share sheet using the [`allowsProminentActivity`](https://developer.apple.com/documentation/UIKit/UIActivityViewController/allowsProminentActivity) property of the  [`UIActivityViewController`](https://developer.apple.com/documentation/UIKit/UIActivityViewController). Just set `allowsProminentActivity` to `false` to display the SharePlay button less prominently in the share sheet actions list.

```swift
let shareSheet = UIActivityViewController(activityItemsConfiguration: configuration)

// Show the SharePlay button less prominently in the share sheet.
shareSheet.allowsProminentActivity = false
```

Here’s how it looks in the share sheet:

![A screenshot of an app that displays the SharePlay button less prominently in the share sheet.](https://docs-assets.developer.apple.com/published/c501f3cd12734c3c4af57a2fcf9a7036/tn3128-share_sheet_less_prominent%402x.png)

#### Hide the Shareplay Button in the Share Sheet

If you have some content that isn’t integrated with SharePlay, hide the SharePlay button in the share sheet. Set the [`excludedActivityTypes`](https://developer.apple.com/documentation/UIKit/UIActivityViewController/excludedActivityTypes) property on the `UIActivityViewController` to exclude the SharePlay activity type.

```swift
let shareSheet = UIActivityViewController(activityItemsConfiguration: configuration)

// Exclude the SharePlay activity in the share sheet.
shareSheet.excludedActivityTypes = [.sharePlay]
```

#### Start Shareplay Directly From Your Apps Custom User Interface

The `GroupActivitySharingController` presents a view in an app that allows users to start a SharePlay session with selected contacts for a given group activity. For example, a button in an app’s custom user interface can initiate a SharePlay session using the `GroupActivitySharingController`. When the user presses the button, instantiate a `GroupActivitySharingController` with a group activity, then present it. The activity starts automatically with the FaceTime call.

```swift
// Create a sharing controller for your group activity.
let controller = GroupActivitySharingController(MyActivity())

// Present the sharing controller.
present(controller, animated: true)
```

Once the user initiates the in-app experience, and starts a FaceTime or SharePlay session, they can activate the staged group activity. Once activated, the app receives the group session.

#### Revision History

- **2022-09-20** First published.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technotes/tn3128-starting-shareplay-without-an-existing-facetime-call)*