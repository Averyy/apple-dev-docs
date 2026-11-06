# AccessoryFeatureSessionHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol that receives events from a data provider extension’s feature session.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
protocol AccessoryFeatureSessionHandler<Session> : Sendable
```

## Overview

Conform to this protocol in your data provider extension to respond to the [`AccessoryFeatureSession`](./accessoryfeaturesession.md) life cycle and incoming data. The system creates an instance of your type from the handler factory closure you provide when you declare the feature. Pass the closure to [`init(_:)`](./accessoryworker/init%28_%29.md) once for each session that starts.

A handler that serves one feature can’t serve another because each feature pins the `Session` associated type through its own `Handler` type alias (for example, [`AccessoryWorker.Handler`](./accessoryworker/handler.md)).

Implement [`sessionStarted(_:)`](./accessoryfeaturesessionhandler/sessionstarted%28_%29.md) to hold the session weakly, and implement [`dataReceived(_:)`](./accessoryfeaturesessionhandler/datareceived%28_%29.md) to process data that the transport extension sends.

## Topics

### Handling the session life cycle
- [func sessionStarted(Self.Session)](./accessoryfeaturesessionhandler/sessionstarted%28_%29.md)
  Notifies the handler when its feature session starts.
- [func sessionInvalidated(error: (any Error)?)](./accessoryfeaturesessionhandler/sessioninvalidated%28error%29.md)
  Notifies the handler when its feature session ends.
### Receiving data
- [func dataReceived(Data) async throws](./accessoryfeaturesessionhandler/datareceived%28_%29.md)
  Handles data that the transport extension sends.
### Associated Types
- [associatedtype Session : AccessoryFeatureSession](./accessoryfeaturesessionhandler/session.md)
  A session type that the handler serves.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing feature sessions
- [protocol AccessoryFeatureSession](./accessoryfeaturesession.md)
  A protocol that represents the session’s data provider.
- [protocol AccessoryFeatureRuntimeSession](./accessoryfeatureruntimesession.md)
  A protocol that represents a feature session’s transport extension.
- [protocol AccessoryFeatureRuntimeSessionHandler](./accessoryfeatureruntimesessionhandler.md)
  A protocol that receives events from a transport extension’s feature session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesessionhandler)*