# AccessoryDataProvider

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol for an extension that receives iOS system notifications and curates their data for your accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
protocol AccessoryDataProvider : AppExtension, Sendable where Self.Configuration : AccessoryDataProviderConfiguration
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Overview

Implement this protocol in an extension with an `EXExtensionPointIdentifier` value of `com.apple.accessory-data-provider` to receive notification data for eventual forwarding to an accessory that you develop. The extension runs in a sandboxed environment and communicates with the system through the extension’s configuration object ([`AccessoryDataProviderConfiguration`](accessorydataproviderconfiguration.md)).

> ❗ **Important**: The system requires your app extension to have the [`com.apple.developer.accessory-data-provider`](https://developer.apple.com/documentation/BundleResources/Entitlements/com.apple.developer.accessory-data-provider) entitlement to use this protocol.

#### Add the Necessary Target Configuration

In your extension’s target properties, include the `EXCapabilities` key with the value `AccessoryNotifications.NotificationsForwarding`:

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
            </array>
        </dict>
    </dict>
</plist>
```

#### Implement the Extension Point

In your extension’s Swift code, implement the protocol and declare the capability with your [`NotificationsForwarding.AccessoryNotificationsHandler`](https://developer.apple.com/documentation/AccessoryNotifications/NotificationsForwarding/AccessoryNotificationsHandler) implementation:

```swift
struct DataProvider: AccessoryDataProvider {
    var extensionPoint: AppExtensionPoint {
        Identifier("com.apple.accessory-data-provider")
        Implementing {
            NotificationsForwarding {
                MyNotificationsHandler()
            }
        }
    }
}

class MyNotificationsHandler: AccessoryNotificationsHandler {
    // Your extension's implementation.
}
```

#### Share Data Between the App and the Extension

Configure a shared app group so your companion app can provide information to the extension. The extension has read-only access to the shared container. Use the shared container to store:

- Authentication tokens for your private servers
- Accessory-specific preferences (max payload size, content filtering)
- Device-specific configuration

```swift
// In the companion app, write to the shared container.
let sharedDefaults = UserDefaults(suiteName: "group.com.yourcompany.accessoryapp")
sharedDefaults?.set(authToken, forKey: "ServerAuthToken")

// In the extension, read from the shared container.
let sharedDefaults = UserDefaults(suiteName: "group.com.yourcompany.accessoryapp")
let authToken = sharedDefaults?.string(forKey: "ServerAuthToken")
```

For more information, see [`Receiving iOS notifications on an accessory`](receiving-ios-notifications-on-an-accessory.md).

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage iOS system notifications for your accessory.
- [protocol AccessoryDataProviderConfiguration](accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurity](accessorytransportsecurity.md)
  A protocol for an extension that handles cryptographic key exchange with your accessory.
- [protocol AccessoryTransportSecurityConfiguration](accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorydataprovider)*