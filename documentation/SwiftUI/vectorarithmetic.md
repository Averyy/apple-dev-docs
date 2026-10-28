# VectorArithmetic

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A type that can serve as the animatable data of an animatable type.

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
protocol VectorArithmetic : AdditiveArithmetic
```

## Overview

`VectorArithmetic` extends the `AdditiveArithmetic` protocol with scalar multiplication and a way to query the vector magnitude of the value. Use this type as the `animatableData` associated type of a type that conforms to the [`Animatable`](./animatable.md) protocol.

## Topics

### Manipulating values
- [var magnitudeSquared: Double](./vectorarithmetic/magnitudesquared.md)
  Returns the dot-product of this vector arithmetic instance with itself.
- [func scale(by: Double)](./vectorarithmetic/scale%28by%29.md)
  Multiplies each component of this value by the given value.
- [func scaled(by: Double) -> Self](./vectorarithmetic/scaled%28by%29.md)
  Returns a value with each component of this value multiplied by the given value.
- [func interpolate(towards: Self, amount: Double)](./vectorarithmetic/interpolate%28towards,amount%29.md)
  Interpolates this value with `other` by the specified `amount`.
- [func interpolated(towards: Self, amount: Double) -> Self](./vectorarithmetic/interpolated%28towards,amount%29.md)
  Returns this value interpolated with `other` by the specified `amount`.

## Relationships

### Inherits From
- [AdditiveArithmetic](../Swift/additivearithmetic.md)
- [Equatable](../Swift/equatable.md)
### Conforming Types
- [AnimatablePair](./animatablepair.md)
- [AnimatableValues](./animatablevalues.md)
- [EmptyAnimatableData](./emptyanimatabledata.md)

## See Also

### Making data animatable
- [protocol Animatable](./animatable.md)
  A type that describes how to animate a property of a view.
- [struct AnimatableValues](./animatablevalues.md)
- [struct AnimatablePair](./animatablepair.md)
  A pair of animatable values, which is itself animatable.
- [struct EmptyAnimatableData](./emptyanimatabledata.md)
  An empty type for animatable data.
- [protocol AnimatableModifier](./animatablemodifier.md)
  A modifier that can create another modifier with animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/vectorarithmetic)*