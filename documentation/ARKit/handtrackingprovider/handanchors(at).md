# handAnchors(at:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Instance Method

Queries for hand anchors at the provided target timestamp.

**Availability**:
- visionOS 2.0+

## Declaration

```swift
final func handAnchors(at timestamp: TimeInterval) -> (leftHand: HandAnchor?, rightHand: HandAnchor?)
```

## Return Value

A tuple that contains optional left and right anchors for the given time. Anchors are `nil` when the provider isn’t running.

## Discussion

Obtain the `timestamp` you provide to this function from the [`trackableAnchorTime`](../../CompositorServices/layerrenderer/frame/timing/trackableanchortime.md) property of [`LayerRenderer.Frame.Timing`](../../CompositorServices/layerrenderer/frame/timing.md).

> ❗ **Important**:  This function isn’t safe to call on multiple threads at the same time. You need to provide your own synchronization.

## Parameters

- `timestamp`: The target timestamp, mach absolute time, in seconds.

## See Also

### Inspecting a hand-tracking provider
- [var state: DataProviderState](./state.md)
  The current status of this hand tracking provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/handtrackingprovider/handanchors(at:))*