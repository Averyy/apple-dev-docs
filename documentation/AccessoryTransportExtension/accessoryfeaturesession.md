# AccessoryFeatureSession

**Framework**: Accessory Transport Extension  
**Kind**: protocol  
**Role**: Protocol

A protocol that represents the session’s data provider.

**Availability**:
- iOS 26.5+

## Declaration

```swift
protocol AccessoryFeatureSession : Sendable
```

## Overview

A feature session is an object that your data provider extension’s handler sends data through. The object is a counterpart to the transport extension’s [`AccessoryFeatureRuntimeSession`](./accessoryfeatureruntimesession.md).

The system creates the session and passes it to your handler’s [`sessionStarted(_:)`](./accessoryfeaturesessionhandler/sessionstarted%28_%29.md) method when a session starts for a feature. Each feature has a conforming session type, for example [`AccessoryWorker.Session`](./accessoryworker/session.md), and the framework supplies the sessions, so you don’t adopt this protocol yourself.

Hold the session weakly in your handler and use it to send data to the transport extension. For more information, see [Accessory features](./accessory-features.md).

## Topics

### Accessing the session
- [var accessory: ASAccessory](./accessoryfeaturesession/accessory.md)
  A reference to the accessory to which the session communicates.
- [var sessionID: UUID](./accessoryfeaturesession/sessionid.md)
  A unique identifier for a feature on the paired accessory.
### Sending data
- [func send(message: AccessoryMessage) async throws](./accessoryfeaturesession/send%28message%29.md)
  Sends a message to the transport extension.

## Relationships

### Inherits From
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
### Conforming Types
- [AccessoryGPUWorker.Session](./accessorygpuworker/session.md)
- [AccessoryWorker.Session](./accessoryworker/session.md)

## See Also

### Managing feature sessions
- [protocol AccessoryFeatureSessionHandler](./accessoryfeaturesessionhandler.md)
  A protocol that receives events from a data provider extension’s feature session.
- [protocol AccessoryFeatureRuntimeSession](./accessoryfeatureruntimesession.md)
  A protocol that represents a feature session’s transport extension.
- [protocol AccessoryFeatureRuntimeSessionHandler](./accessoryfeatureruntimesessionhandler.md)
  A protocol that receives events from a transport extension’s feature session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryfeaturesession)*