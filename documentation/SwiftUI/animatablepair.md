# AnimatablePair

**Framework**: SwiftUI  
**Kind**: struct

A pair of animatable values, which is itself animatable.

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
struct AnimatablePair<First, Second> where First : VectorArithmetic, Second : VectorArithmetic
```

## Topics

### Creating an animatable pair
- [init(First, Second)](animatablepair/init(_:_:).md)
  Creates an animated pair with the provided values.
### Getting the constituent animations
- [var first: First](animatablepair/first.md)
  The first value.
- [var second: Second](animatablepair/second.md)
  The second value.
### Manipulating values
- [var magnitudeSquared: Double](animatablepair/magnitudesquared.md)
  The dot-product of this animated pair with itself.

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [VectorArithmetic](vectorarithmetic.md)

## See Also

- [protocol Animatable](animatable.md)
  A type that describes how to animate a property of a view.
- [struct AnimatableValues](animatablevalues.md)
- [protocol VectorArithmetic](vectorarithmetic.md)
  A type that can serve as the animatable data of an animatable type.
- [struct EmptyAnimatableData](emptyanimatabledata.md)
  An empty type for animatable data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatablepair)*