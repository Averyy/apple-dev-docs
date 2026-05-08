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

## See Also

- [macro Animatable()](animatable().md)
  A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.
- [macro AnimatableIgnored()](animatableignored().md)
  An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:
- [associatedtype AnimatableData : VectorArithmetic](animatable/animatabledata-swift.associatedtype.md)
  The type defining the data to animate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatable/animatabledata-6nydg)*