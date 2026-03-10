# AccessoryTransportSecurity

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol for an extension that handles the cryptography of messages to your accessory.

**Availability**:
- iOS 26.4+ (Beta)
- iPadOS 26.4+ (Beta)
- Mac Catalyst 26.4+ (Beta)

## Declaration

```swift
protocol AccessoryTransportSecurity : AppExtension
```

#### Overview

Implement this protocol in an extension with an `EXExtensionPointIdentifier` value of `com.apple.accessory-transport-security` to manage the key exchange process that underpins the encryption of communication to your accessory. The extension runs in a separate process for security and communicates with the system through the extension’s configuration object ([`AccessoryTransportSecurityConfiguration`](accessorytransportsecurityconfiguration.md)).

> ❗ **Important**: This protocol currently builds only for development or Ad Hoc testing. The API will support App Store submission, TestFlight, and alternative distribution at a later time.

#### Add the Necessary Target Configuration

In your extension’s target properties, specify the extension point identifier:

```xml
<plist>
    <dict>
        <key>EXAppExtensionAttributes</key>
        <dict>
            <key>EXExtensionPointIdentifier</key>
            <string>com.apple.accessory-transport-security</string>
        </dict>
    </dict>
</plist>
```

#### Implement the Extension Point

In your extension’s Swift code, implement the protocol and provide an event handler that responds to key exchange events:

```swift
@main
struct TransportSecurity: AccessoryTransportSecurity {
    @AppExtensionPoint.Bind
    static var boundExtensionPoint: AppExtensionPoint {
        Identifier("com.apple.accessory-transport-security")
    }
    
    func accept(sessionRequest: AccessorySecuritySession.Request) -> AccessorySecuritySession.Request.Decision {
        return sessionRequest.accept {
            MySecurityEventHandler(session: sessionRequest.session)
        }
    }
}

class MySecurityEventHandler: AccessorySecuritySession.EventHandler {
    // Your implementation.
}
```

For more information, see [`Receiving iOS notifications on an accessory`](https://developer.apple.com/documentation/AccessoryNotifications/receiving-ios-notifications-on-an-accessory).

## Topics

### Accepting session requests
- [func accept(sessionRequest: AccessorySecuritySession.Request) -> AccessorySecuritySession.Request.Decision](accessorytransportsecurity/accept(sessionrequest:).md)
  Evaluates incoming security session requests for an accessory.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [Receiving iOS notifications on an accessory](../AccessoryNotifications/receiving-ios-notifications-on-an-accessory.md)
  Create custom app extensions that manage notifications for your accessory.
- [protocol AccessoryDataProvider](accessorydataprovider.md)
  A protocol for an extension that receives iOS system notifications and curates their data for your accessory.
- [protocol AccessoryDataProviderConfiguration](accessorydataproviderconfiguration.md)
  A protocol that configures and manages communication between the extension and the system.
- [protocol AccessoryTransportSecurityConfiguration](accessorytransportsecurityconfiguration.md)
  A protocol that configures and manages communication between your security extension and the system.
- [Accessory Notifications](../AccessoryNotifications/AccessoryNotifications.md)
  Receive forwarded iOS system notifications on an accessory that you develop.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsecurity)*