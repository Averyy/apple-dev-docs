# Receiving Live Activity updates and alerts on an accessory

**Framework**: Accessory Live Activities

Enable your accessory to receive forwarded Live Activities by updating your data provider extension.

#### Overview

To receive forwarded Live Activities on your accessory and alert people about Live Activity updates, you use an extension model that handles secure communication between iPhone and your accessory. Before adding support for Live Activity forwarding, you need to adopt iOS system notification forwarding and implement the extensions that handle communication between iPhone and your accessory. For more information, see [`Receiving iOS notifications on an accessory`](https://developer.apple.com/documentation/AccessoryNotifications/receiving-ios-notifications-on-an-accessory).

> **Note**: Your accessory’s companion app doesn’t have access to forwarded Live Activities and notifications. To keep Live Activity and notification content secure, only the extensions that manage the secure connection between iPhone and your accessory can access it.

In the [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension you create when you add support for receiving notifications on your accessory:

1. Add the capability to receive forwarded Live Activities.
2. Add a [`LiveActivityForwarding.AccessoryLiveActivitiesHandler`](liveactivityforwarding/accessoryliveactivitieshandler.md) implementation  to the extension to receive forwarded Live Activities and prepare them for transmission.
3. Add code to check if the person authorized Live Activity forwarding.

#### Add the Capability

Your app receives and handles Live Activity alert updates in the [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) extension you created when you implemented iOS system notification forwarding. In the extension’s target properties, update the extension point identifier `com.apple.accessory-data-provider` and add an entry to the `EXCapabilities` array for `AccessoryLiveActivities.LiveActivityForwarding`:

```xml
<plist>
    <dict>
        <key>EXAppExtensionAttributes</key>
        <dict>
            <key>EXExtensionPointIdentifier</key>
            <string>com.apple.accessory-data-provider</string>
            <key>EXCapabilities</key>
            <array>
                <string>AccessoryNotifications.NotificationsForwarding</string>
                <string>AccessoryLiveActivities.LiveActivityForwarding</string>
            </array>
        </dict>
    </dict>
</plist>
```

#### Implement a Handler in Your Data Provider Extension

Update the [`AccessoryDataProvider`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryDataProvider) protocol to include [`LiveActivityForwarding`](liveactivityforwarding.md) and provide a handler that conforms to [`LiveActivityForwarding.AccessoryLiveActivitiesHandler`](liveactivityforwarding/accessoryliveactivitieshandler.md). The following code shows the `AccessoryDataProvider` struct conformance:

```swift
@main
struct DataProvider: AccessoryDataProvider {
    var extensionPoint: AppExtensionPoint {
        Identifier("com.apple.accessory-data-provider")
        Implementing {
            LiveActivityForwarding {
                LiveActivitiesHandler()
            }
        }
    }
}
```

Implement your handler class by conforming to [`LiveActivityForwarding.AccessoryLiveActivitiesHandler`](liveactivityforwarding/accessoryliveactivitieshandler.md). At minimum, implement [`activate(for:)`](liveactivityforwarding/accessoryliveactivitieshandler/activate(for:).md) to store the session and [`sessionInvalidated()`](liveactivityforwarding/accessoryliveactivitieshandler/sessioninvalidated().md) to clean up when the session ends:

```swift
/// Respond to Live Activity alert updates from the system.
final class LiveActivitiesHandler: LiveActivityForwarding.AccessoryLiveActivitiesHandler {
    private var session: LiveActivityForwarding.Session?

    func activate(for session: LiveActivityForwarding.Session) {
        self.session = session
        // Load existing Live Activities as described in the next section.
    }

    func sessionInvalidated() {
        session = nil
        // Clean up display state on the accessory.
    }

    // Implement remaining protocol methods.
}
```

#### Load Existing Activities When a Session Starts

When a Live Activity starts, the system calls your handler’s [`activate(for:)`](liveactivityforwarding/accessoryliveactivitieshandler/activate(for:).md) function. Store its [`LiveActivityForwarding.Session`](liveactivityforwarding/session.md) object and use it to read the current set of Live Activities and to send [`AccessoryMessage`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryMessage) payloads to the accessory.

When the system activates the session, use [`liveActivities`](liveactivityforwarding/session/liveactivities.md) to fetch a snapshot of all active Live Activities and synchronize the accessory’s display before new updates arrive:

```swift
func activate(for session: LiveActivityForwarding.Session) {
    self.session = session
    Task {
        do {
            let activities = try await session.liveActivities
            for activity in activities {
                // Send Live Activity information to your accessory.
            }
        } catch {
            // Handle the error appropriately.
        }
    }
}
```

> **Note**: [`liveActivities`](liveactivityforwarding/session/liveactivities.md) returns a snapshot of activities that were active when the session opened. Subsequent additions and updates arrive through [`activityUpdated(_:)`](liveactivityforwarding/accessoryliveactivitieshandler/activityupdated(_:).md) and [`activityUpdatedForAlert(_:)`](liveactivityforwarding/accessoryliveactivitieshandler/activityupdatedforalert(_:).md).

#### Process Live Activity Updates and Forward Them to Your Accessory

When the system forwards a Live Activity update to your data provider extension, it provides your handler with an [`AccessoryLiveActivity`](accessoryliveactivity.md) object you use to update the accessory’s display. Use [`activityUpdated(_:)`](liveactivityforwarding/accessoryliveactivitieshandler/activityupdated(_:).md) to update your accessory to reflect the current Live Activity state. When the update includes an alert, the system calls [`activityUpdatedForAlert(_:)`](liveactivityforwarding/accessoryliveactivitieshandler/activityupdatedforalert(_:).md) instead. Return a `Bool` indicating whether your accessory displayed the alert so the system coordinates alert delivery across devices.

If the callback’s activity’s [`state`](accessoryliveactivity/state.md) property equals [`ActivityState.dismissed`](https://developer.apple.com/documentation/ActivityKit/ActivityState/dismissed), remove the Live Activity from the accessory’s display.

To send forwarded Live Activities from your data provider extension to your accessory, use the extension model and code you added to support iOS system notifications. For more information, see [`Receiving iOS notifications on an accessory`](https://developer.apple.com/documentation/AccessoryNotifications/receiving-ios-notifications-on-an-accessory).

#### Avoid Duplicated Alerts Across Devices

When a Live Activity update includes an alert, the system ensures the person receives the alert without duplication across devices. To coordinate between your accessory or iPhone and determine whether to display an alert, the system calls [`activityUpdatedForAlert(_:)`](liveactivityforwarding/accessoryliveactivitieshandler/activityupdatedforalert(_:).md) and waits for your `Bool` return value before determining where to display the alert. Returning `true` tells the system to suppress the alert on iPhone — your accessory is responsible for notifying the person. The return value is a commitment. Only return `true` from [`activityUpdatedForAlert(_:)`](liveactivityforwarding/accessoryliveactivitieshandler/activityupdatedforalert(_:).md) after confirming the accessory displays the alert. If the accessory can’t confirm it displayed the alert — for example, if the accessory is out of range — return `false` to let iPhone display the alert.

#### Display the Source App Icon

A person might have multiple active Live Activities. To help people keep track of multiple Live Activities, visually distinguish them by loading the app icon of the app that started the Live Activity. Use [`sourceBundleIcon`](accessoryliveactivity/sourcebundleicon.md) to load the source app icon.

If the icon is available, immediately read it by using the [`url`](accessoryliveactivity/iconfile/url.md) as shown in the following example. The URL is ephemeral. Don’t store it for later access.

```swift
func loadIcon(from iconFile: AccessoryLiveActivity.IconFile) async throws -> Data {
    let url = try await iconFile.url
    return try Data(contentsOf: url)
}
```

#### Send Forwarded Live Activities to Your Accessory Securely

To send forwarded Live Activities to your accessory, use the [`AccessoryTransportSecurity`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportSecurity) and [`AccessoryTransportAppExtension`](https://developer.apple.com/documentation/AccessoryTransportExtension/AccessoryTransportAppExtension) extensions you create when you add support for receiving forwarded iOS system notifications. For more information about securely sending Live Activity and notification content to your accessory, see [`Receiving iOS notifications on an accessory`](https://developer.apple.com/documentation/AccessoryNotifications/receiving-ios-notifications-on-an-accessory).

#### Check for Permission

The initial authorization to allow Live Activity forwarding happens in a unified system prompt that allows people to set permissions for iOS system notification and Live Activity forwarding when they configure the accessory. However, people can change permissions at any time in Settings, or choose to deny Live Activity forwarding during initial setup. Additionally, authorization is per physical accessory. As a result, check whether someone authorized Live Activity forwarding for your accessory before you perform any additional logic. For example, check for authorization before indicating in your UI that Live Activity forwarding is active.

Call [`authorization(forAccessory:)`](liveactivityforwarding/authorization(foraccessory:).md) to check the current authorization state. The method returns an [`AccessoryAuthorizationResult`](accessoryauthorizationresult.md), which specifies if the authorization is allowed, limited to some apps, or denied. If the authorization result is `.undetermined`, the person hasn’t seen the system UI for authorizing notification and Live Activity forwarding. Use the [`Accessory Notifications`](https://developer.apple.com/documentation/AccessoryNotifications) framework and  [`requestForwarding(for:)`](https://developer.apple.com/documentation/AccessoryNotifications/AccessoryNotificationCenter/requestForwarding(for:)) to register for notification and activity forwarding and display the system UI.

If someone denies authorization — dismissing the system UI counts as denying forwarding — or only allows a limited scope, you can ask them to update their choice by calling [`presentAuthorizationSheet(forAccessory:)`](liveactivityforwarding/presentauthorizationsheet(foraccessory:).md) to display the system authorization UI. Pass the accessory’s corresponding [`ASAccessory`](https://developer.apple.com/documentation/AccessorySetupKit/ASAccessory) instance from [`AccessorySetupKit`](https://developer.apple.com/documentation/AccessorySetupKit) each time — authorization is per accessory and isn’t cached globally.

The following code checks the current authorization state:

```swift
func checkAuthorization(for accessory: ASAccessory) async throws {
    let result = try await LiveActivityForwarding.authorization(
        forAccessory: accessory
    )
    switch result {
    case .allow, .limited:
        // Add code specific to your app that's related to Live Activity forwarding.
        // For example, you might set a flag that helps the
        // companion app display UI that indicates Live Activity forwarding.
    case .deny:
        // Present the system UI that lets the person update their Live Activity forwarding authorization.
        let updatedAuthorization = try await LiveActivityForwarding
            .presentAuthorizationSheet(forAccessory: accessory)
        if updatedAuthorization == .allow || updatedAuthorization == .limited {
            // Add code specific to your app that's related to Live Activity forwarding.
            // For example, you might set a flag that helps the
            // companion app display UI that indicates Live Activity forwarding.
        }
    case .undetermined:
        // Prompt for permission to opt into notification and activity forwarding.
        let center = AccessoryNotificationCenter()
        try await center.requestForwarding(for: accessory)
    }
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessoryliveactivities/receiving-live-activities-on-an-accessory)*