# send(message:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Sends a message to the transport extension.

**Availability**:
- iOS 26.5+

## Declaration

```swift
func send(message: AccessoryMessage) async throws
```

## Discussion

Create the message with [`AccessoryMessage`](../accessorymessage.md). The system encrypts the message before delivering it to the transport extension.

> **Note**: [`AccessoryWorker.Session`](../accessoryworker/session.md) and [`AccessoryGPUWorker.Session`](../accessorygpuworker/session.md) don’t support this method and throw [`AccessoryTransportSession.Error.unsupported`](../accessorytransportsession/error/unsupported.md); call [`send(data:)`](../accessoryworker/session/send%28data%29.md) or [`send(data:)`](../accessorygpuworker/session/send%28data%29.md) instead.

## Parameters

- `message`: An accessory message to send.

## Default Implementations

### AccessoryFeatureSession Implementations
- [func send(message: AccessoryMessage) async throws](./send%28message%29-79qrl.md)
  Sends a message to the transport extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession/send(message:))*