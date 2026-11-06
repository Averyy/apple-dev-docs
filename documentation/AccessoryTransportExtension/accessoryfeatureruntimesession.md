# AccessoryFeatureRuntimeSession

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol that represents a feature session’s transport extension.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
protocol AccessoryFeatureRuntimeSession : AnyObject, Sendable
```

## Overview

A feature runtime session is a counterpart to the data provider’s [`AccessoryFeatureSession`](./accessoryfeaturesession.md) for worker features ([`AccessoryWorker`](./accessoryworker.md) and [`AccessoryGPUWorker`](./accessorygpuworker.md)).

The framework supplies the types that conform to this protocol. Once your transport extension activates a session, the system delivers the session’s events to the [`AccessoryFeatureRuntimeSessionHandler`](./accessoryfeatureruntimesessionhandler.md) you provide. Create a session with [`makeFeatureSession(_:)`](./accessorytransportsession/makefeaturesession%28_%29.md) and then call [`activate()`](./accessoryfeatureruntimesession/activate%28%29.md) to start it.

## Topics

### Managing the session life cycle
- [func activate() async throws](./accessoryfeatureruntimesession/activate%28%29.md)
  Registers the session and requests that the system start it.
- [func invalidate()](./accessoryfeatureruntimesession/invalidate%28%29.md)
  Unregisters the session.
### Sending data
- [func send(data: Data) async throws](./accessoryfeatureruntimesession/send%28data%29.md)
  Sends data to the data provider extension.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [AccessoryGPUWorker.FeatureSession](./accessorygpuworker/featuresession.md)
- [AccessoryWorker.FeatureSession](./accessoryworker/featuresession.md)

## See Also

### Managing feature sessions
- [protocol AccessoryFeatureSession](./accessoryfeaturesession.md)
  A protocol that represents the session’s data provider.
- [protocol AccessoryFeatureSessionHandler](./accessoryfeaturesessionhandler.md)
  A protocol that receives events from a data provider extension’s feature session.
- [protocol AccessoryFeatureRuntimeSessionHandler](./accessoryfeatureruntimesessionhandler.md)
  A protocol that receives events from a transport extension’s feature session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeatureruntimesession)*