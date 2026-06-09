# transportStateRestoreIdentifier

**Framework**: Accessory Transport Extension  
**Kind**: property

An optional identifier for restoring transport state across sessions.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+
- Mac Catalyst 26.5+

## Declaration

```swift
var transportStateRestoreIdentifier: String?
```

#### Discussion

Use this identifier to restore connection state if your transport extension needs to relaunch.

## See Also

- [var transport: AccessoryTransport?](accessorytransportsession/transport.md)
  A transport method that the session uses to communicate with the accessory.
- [var pushToken: Data?](accessorytransportsession/pushtoken.md)
  A token that identifies the iOS device to the Apple Push Notification service for routing accessory responses over the internet.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/transportstaterestoreidentifier)*