# AccessoryFeatureRuntimeSessionHandler

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol that receives events from a transport extension’s feature session.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
protocol AccessoryFeatureRuntimeSessionHandler<Session> : Sendable
```

## Overview

Conform to this protocol in your transport extension to respond to the [`AccessoryFeatureRuntimeSession`](./accessoryfeatureruntimesession.md) life cycle and incoming data. The system creates an instance of your type from the handler factory closure that you pass to [`makeFeatureSession(_:)`](./accessorytransportsession/makefeaturesession%28_%29.md).

A handler that serves one feature can’t serve another because each feature pins the `Session` associated type through its own `Handler` type alias (for example, [`AccessoryWorker.FeatureSession.Handler`](./accessoryworker/featuresession/handler.md)).

Implement the only required method, [`sessionStarted(_:)`](./accessoryfeatureruntimesessionhandler/sessionstarted%28_%29.md), to send data.

## Topics

### Handling the session life cycle
- [func sessionStarted(Self.Session)](./accessoryfeatureruntimesessionhandler/sessionstarted%28_%29.md)
  Notifies the handler when its feature session starts.
- [func sessionInvalidated(error: (any Error)?)](./accessoryfeatureruntimesessionhandler/sessioninvalidated%28error%29.md)
  Notifies the handler when its feature session ends.
### Receiving data
- [func dataReceived(Data) async throws](./accessoryfeatureruntimesessionhandler/datareceived%28_%29.md)
  Handles data that the data provider extension sends.
### Associated Types
- [associatedtype Session : AccessoryFeatureRuntimeSession](./accessoryfeatureruntimesessionhandler/session.md)
  A session type that the handler serves.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Managing feature sessions
- [protocol AccessoryFeatureSession](./accessoryfeaturesession.md)
  A protocol that represents the session’s data provider.
- [protocol AccessoryFeatureSessionHandler](./accessoryfeaturesessionhandler.md)
  A protocol that receives events from a data provider extension’s feature session.
- [protocol AccessoryFeatureRuntimeSession](./accessoryfeatureruntimesession.md)
  A protocol that represents a feature session’s transport extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureruntimesessionhandler)*