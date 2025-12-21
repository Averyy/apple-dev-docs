# CompositorContentBuilder

**Framework**: SwiftUI  
**Kind**: struct

A result builder for composing a collection of [`CompositorContent`](compositorcontent.md) elements.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
@resultBuilder
struct CompositorContentBuilder
```

## Topics

### Structures
- [CompositorContentBuilder.Content](compositorcontentbuilder/content.md)
  A representation of the content of a compositor content builder.
### Type Methods
- [static func buildBlock<C>(C) -> C](compositorcontentbuilder/buildblock(_:).md)
- [static buildEither(first:)](compositorcontentbuilder/buildeither(first:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<F>(second: F) -> _ConditionalContent<_LimitedAvailabilityCompositorContent, F>](compositorcontentbuilder/buildeither(second:).md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildExpression<C>(C) -> C](compositorcontentbuilder/buildexpression(_:).md)
- [static func buildLimitedAvailability(some CompositorContent) -> _LimitedAvailabilityCompositorContent](compositorcontentbuilder/buildlimitedavailability(_:).md)
  Processes scene content for a conditional compiler-control statement that performs an availability check.

## See Also

- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.
- [protocol CompositorContent](compositorcontent.md)
- [struct AnyCompositorContent](anycompositorcontent.md)
  Type erased compositor content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontentbuilder)*