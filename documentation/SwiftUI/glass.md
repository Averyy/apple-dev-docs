# Glass

**Framework**: SwiftUI  
**Kind**: struct

A structure that defines the configuration of the Liquid Glass material.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Glass
```

## Mentions

- [Applying Liquid Glass to custom views](applying-liquid-glass-to-custom-views.md)

#### Overview

You provide instances of a variant of Liquid Glass to the [`glassEffect(_:in:)`](view/glasseffect(_:in:).md) view modifier:

```swift
Text("Hello, World!")
    .font(.title)
    .padding()
    .glassEffect()
```

You can combine Liquid Glass effects using a [`GlassEffectContainer`](glasseffectcontainer.md), which supports morphing views with this effect into each other based on the geometry of their associated views.

## Topics

### Instance Methods
- [func interactive(Bool) -> Glass](glass/interactive(_:).md)
  Returns a copy of the structure configured to be interactive.
- [func tint(Color?) -> Glass](glass/tint(_:).md)
  Returns a copy of the structure with a configured tint color.
### Type Properties
- [static var clear: Glass](glass/clear.md)
  The clear variant of glass.
- [static var identity: Glass](glass/identity.md)
  The identity variant of glass. When applied, your content remains unaffected as if no glass effect was applied.
- [static var regular: Glass](glass/regular.md)
  The regular variant of the Liquid Glass material.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func border<S>(S, width: CGFloat) -> some View](view/border(_:width:).md)
  Adds a border to this view with the specified style and width.
- [func foregroundStyle<S>(S) -> some View](view/foregroundstyle(_:).md)
  Sets a view’s foreground elements to use a given style.
- [func foregroundStyle<S1, S2>(S1, S2) -> some View](view/foregroundstyle(_:_:).md)
  Sets the primary and secondary levels of the foreground style in the child view.
- [func foregroundStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/foregroundstyle(_:_:_:).md)
  Sets the primary, secondary, and tertiary levels of the foreground style.
- [func backgroundStyle<S>(S) -> some View](view/backgroundstyle(_:).md)
  Sets the specified style to render backgrounds within the view.
- [var backgroundStyle: AnyShapeStyle?](environmentvalues/backgroundstyle.md)
  An optional style that overrides the default system background style when set.
- [protocol ShapeStyle](shapestyle.md)
  A color or pattern to use when rendering a shape.
- [struct AnyShapeStyle](anyshapestyle.md)
  A type-erased ShapeStyle value.
- [struct Gradient](gradient.md)
  A color gradient represented as an array of color stops, each having a parametric location value.
- [struct MeshGradient](meshgradient.md)
  A two-dimensional gradient defined by a 2D grid of positioned colors.
- [struct AnyGradient](anygradient.md)
  A color gradient.
- [struct ShadowStyle](shadowstyle.md)
  A style to use when rendering shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/glass)*