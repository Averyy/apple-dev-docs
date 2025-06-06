# blendLayer

**Framework**: RealityKit  
**Kind**: property

An integer that specifies the order in which to apply animations when more than one animation is playing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
var blendLayer: Int
```

#### Discussion

Animations in a lower layer are applied before animations in a higher layer. Animations in the same layer are applied in the order in which the animations where started.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/playanimationaction/blendlayer)*