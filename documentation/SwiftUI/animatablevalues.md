# AnimatableValues

**Framework**: SwiftUI  
**Kind**: struct

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
@frozen
struct AnimatableValues<each Value> where repeat each Value : VectorArithmetic
```

## Topics

### Initializers
- [init(repeat each Value)](animatablevalues/init(_:).md)
  Creates a tuple of animatable values.
### Instance Properties
- [var magnitudeSquared: Double](animatablevalues/magnitudesquared.md)
  The dot-product of the tuple of animatable values with itself.
- [var value: (repeat each Value)](animatablevalues/value.md)
  The tuple of values.

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/AdditiveArithmetic.md)
- [Equatable](../Swift/Equatable.md)
- [VectorArithmetic](vectorarithmetic.md)

## See Also

- [protocol Animatable](animatable.md)
  A type that describes how to animate a property of a view.
- [struct AnimatablePair](animatablepair.md)
  A pair of animatable values, which is itself animatable.
- [protocol VectorArithmetic](vectorarithmetic.md)
  A type that can serve as the animatable data of an animatable type.
- [struct EmptyAnimatableData](emptyanimatabledata.md)
  An empty type for animatable data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatablevalues)*