# animatableData

**Framework**: SwiftUI  
**Kind**: property  
**Required**: Yes

The data to animate.

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
var animatableData: Self.AnimatableData { get set }
```

#### Discussion

SwiftUI reads this property to capture the current vector representation of the animatable state, and writes it back on each animation frame with an interpolated value. The default implementation returns [`EmptyAnimatableData`](emptyanimatabledata.md), meaning nothing is animated.

Use the [`Animatable()`](animatable().md) macro to synthesize this property automatically. Implement it by hand only when you need custom interpolation logic such as clamping, normalization, or mapping to a derived value.

## See Also

- [macro Animatable()](animatable().md)
  A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.
- [macro AnimatableIgnored()](animatableignored().md)
  An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:
- [associatedtype AnimatableData : VectorArithmetic](animatable/animatabledata-swift.associatedtype.md)
  The type defining the data to animate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatable/animatabledata-6nydg)*