# Animatable()

**Framework**: SwiftUI  
**Kind**: macro

A member and extension macro that, when applied to a struct, class or enum declaration, synthesizes the conformance to `Animatable` and its requirement, the `animatableData` property using the existing animatable properties of the type this macro is applied to.

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
(extension, conformances: Animatable) @attached(member, names: named(animatableData)) macro Animatable()
```

#### Overview

```swift
@Animatable
struct CoolShape: Shape {
    var width: CGFloat
    var angle: Angle
    @AnimatableIgnored var isOpaque: Bool

    // ...
}
```

In the above code, `animatableData` will be synthesized using `width` and `angle` properties of `CoolShape` structure.  Since changes to `isOpaque` property cannot be animated, it is annotated with `@AnimatableIgnored`.

> **Note**: The `@Animatable` macro will not generate an `Animatable` conformance if the type already conforms to `Animatable`.

> **Note**: It is only possible to attach `@Animatable` to types with properties.

> **Note**: `@Animatable` will not include computed properties in the synthesized `animatableData`.

## See Also

- [macro AnimatableIgnored()](animatableignored().md)
  An accessor macro that marks a property of a type to be excluded from the `animatableData` synthesis:
- [var animatableData: Self.AnimatableData](animatable/animatabledata-6nydg.md)
  The data to animate.
- [associatedtype AnimatableData : VectorArithmetic](animatable/animatabledata-swift.associatedtype.md)
  The type defining the data to animate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/animatable())*