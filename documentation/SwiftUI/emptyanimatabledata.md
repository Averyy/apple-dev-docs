# EmptyAnimatableData

**Framework**: SwiftUI  
**Kind**: struct

An empty type for animatable data.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@frozen
struct EmptyAnimatableData
```

#### Overview

This type is suitable for use as the `animatableData` property of types that do not have any animatable properties.

## Topics

### Creating the data
- [init()](emptyanimatabledata/init.md)
### Manipulating the data
- [var magnitudeSquared: Double](emptyanimatabledata/magnitudesquared.md)
  The dot-product of this animatable data instance with itself.

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [VectorArithmetic](vectorarithmetic.md)

## See Also

- [protocol Animatable](animatable.md)
  A type that describes how to animate a property of a view.
- [struct AnimatablePair](animatablepair.md)
  A pair of animatable values, which is itself animatable.
- [protocol VectorArithmetic](vectorarithmetic.md)
  A type that can serve as the animatable data of an animatable type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptyanimatabledata)*