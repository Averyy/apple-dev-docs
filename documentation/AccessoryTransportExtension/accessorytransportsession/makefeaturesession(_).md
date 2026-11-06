# makeFeatureSession(_:)

**Framework**: Accessory Transport Extension  
**Kind**: method  
**Role**: Instance Method

Creates a feature session for the provided handler.

**Availability**:
- iOS 27.3+ (Beta)

## Declaration

```swift
func makeFeatureSession<H>(_ handlerFactory: () -> H) throws(AccessoryTransportSession.Error) -> H.Session where H : AccessoryFeatureRuntimeSessionHandler
```

## Mentions

- [Sending data to an accessory in the background](../sending-data-to-an-accessory-in-the-background.md)

## Discussion

This method requires a Bluetooth transport and throws [`AccessoryTransportSession.Error.unsupported`](./error/unsupported.md) otherwise. It throws [`AccessoryTransportSession.Error.invalidated`](./error/invalidated.md) if the transport session isn’t valid. It doesn’t fail when the feature isn’t enrolled for the accessory; see [`activate()`](../accessoryfeatureruntimesession/activate%28%29.md) for when the session starts. The returned session does nothing until you call [`activate()`](../accessoryfeatureruntimesession/activate%28%29.md), and you need to call [`invalidate()`](../accessoryfeatureruntimesession/invalidate%28%29.md) before releasing an activated session.

Your transport extension calls this method. A data provider extension can’t create a feature session or wake your transport extension on its own. Call this method in response to an event from your accessory, such as a Bluetooth characteristic update. Only the worker features, [`AccessoryWorker`](../accessoryworker.md) and [`AccessoryGPUWorker`](../accessorygpuworker.md), use feature sessions that you create this way; for more information, see [Accessory features](../accessory-features.md).

## Parameters

- `handlerFactory`: A closure that creates the handler for the new session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accessorytransportextension/accessorytransportsession/makefeaturesession(_:))*