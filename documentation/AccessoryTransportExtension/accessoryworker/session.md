# AccessoryWorker.Session

**Framework**: Accessory Transport Extension  
**Kind**: class  
**Role**: Class

A class that represents the data provider within a session.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
final class Session
```

## Mentions

- [Sending data to an accessory in the background](../sending-data-to-an-accessory-in-the-background.md)

## Overview

The system creates an instance of this class when the transport extension’s [`AccessoryWorker.FeatureSession`](./featuresession.md) starts, and passes it to your handler’s [`sessionStarted(_:)`](../accessoryfeaturesessionhandler/sessionstarted%28_%29.md) method. Hold the session weakly in your handler, and call [`send(data:)`](./session/send%28data%29.md) to send data to the transport extension.

## Topics

### Sending data
- [func send(data: Data) async throws](./session/send%28data%29.md)
  Sends data to the transport extension within a session.
- [func send(message: AccessoryMessage) async throws](./session/send%28message%29.md)
  Sends a message to the transport extension.

## Relationships

### Conforms To
- [AccessoryFeatureSession](../accessoryfeaturesession.md)
- [Copyable](../../Swift/copyable.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling data-provider sessions
- [AccessoryWorker.Handler](./handler.md)
  A handler type for the session’s data provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryworker/session)*