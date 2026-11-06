# send(message:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Sends a message to the transport extension.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
final func send(message: AccessoryMessage) async throws
```

## Discussion

This method conforms to [`AccessoryFeatureSession`](../../accessoryfeaturesession.md) but always throws [`AccessoryTransportSession.Error.unsupported`](../../accessorytransportsession/error/unsupported.md); call [`send(data:)`](./send%28data%29.md) instead to send data to the transport extension.

## Parameters

- `message`: An accessory message.

## See Also

### Sending data
- [func send(data: Data) async throws](./send%28data%29.md)
  Sends data to the transport extension within a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryworker/session/send(message:))*