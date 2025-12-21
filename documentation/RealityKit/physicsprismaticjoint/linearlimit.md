# linearLimit

**Framework**: RealityKit  
**Kind**: property

A limit of the translation between the pins in the direction of the x-axis.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
var linearLimit: ClosedRange<Float>?
```

#### Discussion

If defined, this limits the translation of `pin1` from `pin0`, in the direction of the x-axis of `pin0`. There is no limit if this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsprismaticjoint/linearlimit)*