# angularLimit

**Framework**: RealityKit  
**Kind**: property

A limit of the rotational freedom between the pins around the x-axis.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
var angularLimit: ClosedRange<Float>?
```

#### Discussion

If defined, this limits the rotation of `pin1` around the x-axis of `pin0`. There is no limit if this property is `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsrevolutejoint/angularlimit)*