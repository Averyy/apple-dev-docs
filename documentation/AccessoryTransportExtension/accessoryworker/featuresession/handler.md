# AccessoryWorker.FeatureSession.Handler

**Framework**: Accessory Transport Extension  
**Kind**: typealias  
**Role**: Type Alias

A handler type for the session’s transport extension.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
typealias Handler = AccessoryFeatureRuntimeSessionHandler<AccessoryWorker.FeatureSession>
```

## Mentions

- [Sending data to an accessory in the background](../../sending-data-to-an-accessory-in-the-background.md)

## Discussion

Create a handler type that conforms to this type alias to receive events from an [`AccessoryWorker.FeatureSession`](../featuresession.md). Because each feature declares its own `Handler` type alias, your transport extension needs a distinct handler type for each feature it supports: the compiler rejects a handler written for [`AccessoryGPUWorker.FeatureSession`](../../accessorygpuworker/featuresession.md) if you pass it to this feature’s session, or any other feature’s session. Return an instance of your handler from the factory closure that you pass to [`makeFeatureSession(_:)`](../../accessorytransportsession/makefeaturesession%28_%29.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessoryworker/featuresession/handler)*