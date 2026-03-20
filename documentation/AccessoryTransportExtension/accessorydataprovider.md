# AccessoryDataProvider

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol for an extension that receives iOS system notifications and curates their data for your accessory.

**Availability**:
- iOS 26.4+
- iPadOS 26.4+
- Mac Catalyst 26.4+

## Declaration

```swift
protocol AccessoryDataProvider : AppExtension, Sendable where Self.Configuration : AccessoryDataProviderConfiguration
```

#### Overview

Implement this protocol in an extension with an `EXExtensionPointIdentifier` value of `com.apple.accessory-data-provider` to receive notification data for eventual forwarding to an accessory that you develop. The extension runs in a sandboxed environment and communicates with the system through the extension’s configuration object ([`AccessoryDataProviderConfiguration`](accessorydataproviderconfiguration.md)).

> ❗ **Important**: This protocol currently builds only for development or Ad Hoc testing. The API will support App Store submission, TestFlight, and alternative distribution at a later time.

#### Add the Necessary Target Configuration

In your extension’s target properties, include the `_EXExtensionCapabilities` key with the value `AccessoryNotifications.NotificationsForwarding`:

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
    // Your implementation.
}
```

For more information, see [`Receiving iOS notifications on an accessory`](https://developer.apple.com/documentation/AccessoryNotifications/receiving-ios-notifications-on-an-accessory).

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Receiving iOS notifications on an accessory](../AccessoryNotifications/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage notifications for your accessory.
- [protocol AccessoryDataProviderConfiguration](accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurity](accessorytransportsecurity.md)
  A protocol for an extension that handles the cryptography of messages to your accessory.
- [protocol AccessoryTransportSecurityConfiguration](accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorydataprovider)*