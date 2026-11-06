# send(data:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Sends data to the transport extension within a session.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
final func send(data: Data) async throws
```

## Discussion

The Accessory Transport Extension framework doesn’t add additional encryption to the data, so take steps to protect sensitive data before you send it.

## Parameters

- `data`: The data to send.

## See Also

### Sending data
- [func send(message: AccessoryMessage) async throws](./send%28message%29.md)
  Sends a message to the transport extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorygpuworker/session/send(data:))*