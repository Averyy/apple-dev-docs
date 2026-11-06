# AccessoryGPUWorker.FeatureSession

**Framework**: Accessory Transport Extension  
**Kind**: class  
**Role**: Class

A class that represents the session’s transport extension.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
final class FeatureSession
```

## Overview

When the session starts, the system starts a matching [`AccessoryGPUWorker.Session`](./session.md) on the data provider. Create a session of this type with [`makeFeatureSession(_:)`](../accessorytransportsession/makefeaturesession%28_%29.md), then call [`activate()`](../accessoryfeatureruntimesession/activate%28%29.md) to start it. Call [`invalidate()`](../accessoryfeatureruntimesession/invalidate%28%29.md) before you release an activated session.

## Topics

### Creating a handler
- [AccessoryGPUWorker.FeatureSession.Handler](./featuresession/handler.md)
  A handler type for the session’s transport extension.

## Relationships

### Conforms To
- [AccessoryFeatureRuntimeSession](../accessoryfeatureruntimesession.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorygpuworker/featuresession)*