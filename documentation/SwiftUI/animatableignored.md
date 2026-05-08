# AnimatableIgnored()

**Framework**: SwiftUI  
**Kind**: macro

An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:

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
@attached
(accessor, names: named(willSet)) macro AnimatableIgnored()
```

#### Overview

```swift
@Animatable
struct CoolShape: Shape {
    var width: CGFloat
    var height: CGFloat
    @AnimatableIgnored var isVisible: Bool

    // ...
}
```

In the above example, the `isVisible` property of `CoolShape` will not be participating in the synthesis of `animatableData`.

## See Also

- [macro Animatable()](animatable().md)
  A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.
- [var animatableData: Self.AnimatableData](animatable/animatabledata-6nydg.md)
  The data to animate.
- [associatedtype AnimatableData : VectorArithmetic](animatable/animatabledata-swift.associatedtype.md)
  The type defining the data to animate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatableignored())*