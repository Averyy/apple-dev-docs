# AnimatableModifier

**Framework**: SwiftUI  
**Kind**: protocol  
**Role**: Protocol

A modifier that can create another modifier with animation.

**Availability**:
- iOS 13.0+ - Deprecated in 27.3
- iPadOS 13.0+ - Deprecated in 27.3
- Mac Catalyst 13.0+ - Deprecated in 27.3
- macOS 10.15+ - Deprecated in 27.3
- tvOS 13.0+ - Deprecated in 27.3
- visionOS 1.0+ - Deprecated in 27.3
- watchOS 6.0+ - Deprecated in 27.3

> **Deprecated**: Use [`Animatable`](./animatable.md) instead.

## Declaration

```swift
protocol AnimatableModifier : Animatable, ViewModifier
```

## Relationships

### Inherits From
- [Animatable](./animatable.md)
- [ViewModifier](./viewmodifier.md)

## See Also

### Making data animatable
- [protocol Animatable](./animatable.md)
  A type that describes how to animate a property of a view.
- [struct AnimatableValues](./animatablevalues.md)
- [struct AnimatablePair](./animatablepair.md)
  A pair of animatable values, which is itself animatable.
- [protocol VectorArithmetic](./vectorarithmetic.md)
  A type that can serve as the animatable data of an animatable type.
- [struct EmptyAnimatableData](./emptyanimatabledata.md)
  An empty type for animatable data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatablemodifier)*