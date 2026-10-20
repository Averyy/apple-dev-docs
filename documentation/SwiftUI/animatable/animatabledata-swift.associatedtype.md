# AnimatableData

**Framework**: SwiftUI  
**Kind**: associatedtype  
**Role**: Associated Type  
**Required**: Yes

The type defining the data to animate.

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
associatedtype AnimatableData : VectorArithmetic
```

## See Also

### Animating data
- [macro Animatable()](../animatable%28%29.md)
  A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.
- [macro AnimatableIgnored()](../animatableignored%28%29.md)
  An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:
- [var animatableData: Self.AnimatableData](./animatabledata-6nydg.md)
  The data to animate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatable/animatabledata-swift.associatedtype)*