# AccessoryTransportAppExtension

**Framework**: Accessory Transport Extension  
**Kind**: protocol

A protocol for an extension that transmits data to an accessory you develop.

**Availability**:
- iOS 26.2+
- iPadOS 26.2+

## Declaration

```swift
protocol AccessoryTransportAppExtension : AppExtension
```

#### Overview

Implement this protocol in an extension with an `EXExtensionPointIdentifier` value of `com.apple.accessory-transport-extension` to relay data to your accessory. The extension supports sharing Wi-Fi networks and forwarding iOS system notifications.

#### Wi Fi Network Sharing

Use this extension with [`Wi-Fi Infrastructure`](https://developer.apple.com/documentation/WiFiInfrastructure) to share a Wi-Fi network with your accessory. The system calls your extension’s [`accept(sessionRequest:)`](accessorytransportappextension/accept(sessionrequest:).md) method when it needs to establish a transport session for Wi-Fi sharing.

In your extension’s target properties, specify the extension point identifier:

```xml
<plist>
    <dict>
        <key>EXAppExtensionAttributes</key>
        <dict>
            <key>EXExtensionPointIdentifier</key>
            <string>com.apple.accessory-transport-extension</string>
        </dict>
    </dict>
</plist>
```

In your extension’s Swift code, implement the protocol and provide an event handler:

```swift
@main
struct TransportExtension: AccessoryTransportAppExtension {
    func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision {
        return sessionRequest.accept {
            MyTransportEventHandler(session: sessionRequest.session)
        }
    }
}

class MyTransportEventHandler: AccessoryTransportSession.EventHandler {
    func invalidationHandler(error: AccessoryTransportSession.Error?) {
        // Clean up when the session ends.
    }
}
```

After accepting a session, your extension connects directly to the accessory using [`ASAccessorySession`](https://developer.apple.com/documentation/AccessorySetupKit/ASAccessorySession) and delivers Wi-Fi network data using [`WINetworkSharingProvider`](https://developer.apple.com/documentation/WiFiInfrastructure/WINetworkSharingProvider).

#### Notification Forwarding

For notification forwarding, set up your extension the same way as for Wi-Fi network sharing. The system invokes your extension to relay encrypted notification data from your app’s [`AccessoryDataProvider`](accessorydataprovider.md) extension to your accessory.

Implement `AccessoryTransportSession/EventHandler/dataEventHandler(event:)` in your event handler to receive and transmit data:

```swift
class MyTransportEventHandler: AccessoryTransportSession.EventHandler {
    func dataEventHandler(event: AccessoryTransportSession.DataEvent) {
        switch event {
        case .ciphertext(let data, let featureID):
            // Transmit encrypted notification data to accessory over Bluetooth.
            sendToAccessory(data)
        case .plaintext(let data, let featureID):
            // Transmit plaintext data to accessory.
            sendToAccessory(data)
        }
    }
    
    func invalidationHandler(error: AccessoryTransportSession.Error?) {
        // Clean up when the session ends.
    }
}
```

The system encrypts data using keys through your app’s [`AccessoryTransportSecurity`](accessorytransportsecurity.md) (ATS) extension and then delivers the encrypted data as `ciphertext` to your handler. Your extension transmits the encrypted data to the accessory, which decrypts the data using shared encryption keys.

> **Note**: Call [`cancel(error:)`](accessorytransportsession/cancel(error:).md) on the session if your extension encounters an error that requires terminating the session.

## Topics

### Accepting session requests
- [func accept(sessionRequest: AccessoryTransportSession.Request) -> AccessoryTransportSession.Request.Decision](accessorytransportappextension/accept(sessionrequest:).md)
  Handles a new session request for the accessory.
- [AccessoryTransportSession.Request.Decision](accessorytransportsession/request/decision.md)
  An opaque type returned from the incoming session handler of an event listener.
### Handling session events
- [AccessoryTransportSession.EventHandler](accessorytransportsession/eventhandler.md)
  A protocol that defines methods for handling transport session events.
### Managing sessions
- [class AccessoryTransportSession](accessorytransportsession.md)
  A class that manages a transport session between the extension and the system.

## Relationships

### Inherits From
- [AppExtension](../ExtensionFoundation/AppExtension.md)

## See Also

- [protocol AccessoryTransportExtensionConfiguration](accessorytransportextensionconfiguration.md)
  An interface that enables you to configure and manage communication between your extension and the system.
- [class AccessoryTransportSession](accessorytransportsession.md)
  A class that manages a transport session between the extension and the system.
- [Wi-Fi Infrastructure](../WiFiInfrastructure/WiFiInfrastructure.md)
  Share Wi-Fi network credentials securely between devices and connected accessories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportappextension)*