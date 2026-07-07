# messageReceived(_:completion:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Required**: Yes

Handles incoming messages for transmission to the accessory.

**Availability**:
- iOS 26.5+
- iPadOS 26.5+

## Declaration

```swift
func messageReceived(_ message: TransportMessage, completion: @escaping @Sendable (AccessoryMessage.Result) -> Void)
```

## Mentions

- [Receiving iOS notifications on an accessory](receiving-ios-notifications-on-an-accessory.md)

#### Discussion

The system calls this method to deliver encrypted notification data for transmission to your accessory. Relay the message’s data to your accessory over Bluetooth or another transport. Call the completion handler with [`AccessoryMessage.Result.success`](accessorymessage/result/success.md) if transmission succeeds, [`AccessoryMessage.Result.failure(_:)`](accessorymessage/result/failure(_:).md) with [`AccessoryMessage.Error.transportFailed`](accessorymessage/error/transportfailed.md) if the transport fails but may recover, or [`AccessoryMessage.Error.transportUnavailable`](accessorymessage/error/transportunavailable.md) if the transport is unavailable.

If you don’t call the completion handler, the system assumes successful delivery and won’t retry the message.

## Parameters

- `message`: A transport message containing data to send to the accessory.
- `completion`: A closure to call when message transmission completes.

## See Also

- [func dataEventHandler(event: AccessoryTransportSession.DataEvent)](accessorytransportsession/eventhandler/dataeventhandler(event:).md)
  Handles events that address incoming data destined for the accessory.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/eventhandler/messagereceived(_:completion:))*