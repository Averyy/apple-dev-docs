# pushToken

**Framework**: Accessory Transport Extension  
**Kind**: property

A token that identifies the iOS device to the Apple Push Notification service for routing accessory responses over the internet.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
var pushToken: Data?
```

#### Discussion

This property contains a value when the session uses internet transport. Convert the token to a hex-encoded string before including it in the JSON payload your accessory sends to your server. Your server uses the token to contact APNs and route the accessory’s encrypted response to the correct device; include the [`sessionID`](transportmessage/sessionid.md) in the same payload so the system delivers the response to the correct data provider extension.

## See Also

- [var transport: AccessoryTransport?](accessorytransportsession/transport.md)
  A transport method that the session uses to communicate with the accessory.
- [var transportStateRestoreIdentifier: String?](accessorytransportsession/transportstaterestoreidentifier.md)
  An optional identifier for restoring transport state across sessions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/pushtoken)*