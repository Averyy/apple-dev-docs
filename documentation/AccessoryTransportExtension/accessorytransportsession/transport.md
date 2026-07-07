# transport

**Framework**: Accessory Transport Extension  
**Kind**: property

A transport method that the session uses to communicate with the accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
var transport: AccessoryTransport?
```

#### Discussion

Use this property to determine which transport the current instance handles, and customize your message delivery accordingly. The system may launch your extension in separate processes for different transports.

> **Note**: The system automatically selects transports in this order: Bluetooth (if connected), local network (if available), then internet (if available). The system notifies your extension of the transport method it selects. Customize payload contents based on the selected type.

## See Also

- [var transportStateRestoreIdentifier: String?](accessorytransportsession/transportstaterestoreidentifier.md)
  An optional identifier for restoring transport state across sessions.
- [var pushToken: Data?](accessorytransportsession/pushtoken.md)
  A token that identifies the iOS device to the Apple Push Notification service for routing accessory responses over the internet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/transport)*