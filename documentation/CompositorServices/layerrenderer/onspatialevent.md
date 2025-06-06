# onSpatialEvent

**Framework**: Compositor Services  
**Kind**: property

A closure that receives spatial event updates from the layer renderer.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@MainActor
@preconcurrency var onSpatialEvent: @MainActor (SpatialEventCollection) -> Void { get set }
```

#### Discussion

Assign a closure to this property when configuring your layer renderer. When a person interacts with your immersive content, the layer renderer delivers the associated events as a parameter to your closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/onspatialevent)*