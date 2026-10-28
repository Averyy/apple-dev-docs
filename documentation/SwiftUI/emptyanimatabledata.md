# EmptyAnimatableData

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

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

## Overview

This type is suitable for use as the `animatableData` property of types that do not have any animatable properties.

## Topics

### Creating the data
- [init()](./emptyanimatabledata/init%28%29.md)
### Manipulating the data
- [var magnitudeSquared: Double](./emptyanimatabledata/magnitudesquared.md)
  The dot-product of this animatable data instance with itself.

## Relationships

### Conforms To
- [AdditiveArithmetic](../Swift/additivearithmetic.md)
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Copyable](../Swift/copyable.md)
- [Equatable](../Swift/equatable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [VectorArithmetic](./vectorarithmetic.md)

## See Also

### Making data animatable
- [protocol Animatable](./animatable.md)
  A type that describes how to animate a property of a view.
- [struct AnimatableValues](./animatablevalues.md)
- [struct AnimatablePair](./animatablepair.md)
  A pair of animatable values, which is itself animatable.
- [protocol VectorArithmetic](./vectorarithmetic.md)
  A type that can serve as the animatable data of an animatable type.
- [protocol AnimatableModifier](./animatablemodifier.md)
  A modifier that can create another modifier with animation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/emptyanimatabledata)*