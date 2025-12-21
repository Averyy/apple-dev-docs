# frames

**Framework**: RealityKit  
**Kind**: property

An array of weights in which each element represents a discrete state of the target entity at a given point in the animation’s timeline.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var frames: [BlendShapeWeights] { get set }
```

#### Discussion

This array contains sequential values for the animated property when [`bindTarget`](animationdefinition/bindtarget.md) is an array of weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/sampledanimation/frames-9jtu9)*