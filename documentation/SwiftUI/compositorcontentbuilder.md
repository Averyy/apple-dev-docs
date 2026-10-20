# CompositorContentBuilder

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A result builder for composing a collection of [`CompositorContent`](./compositorcontent.md) elements.

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
- [CompositorContentBuilder.Content](./compositorcontentbuilder/content.md)
  A representation of the content of a compositor content builder.
### Type Methods
- [static func buildBlock<C>(C) -> C](./compositorcontentbuilder/buildblock%28_%29.md)
- [static buildEither(first:)](./compositorcontentbuilder/buildeither%28first%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is true.
- [static func buildEither<F>(second: F) -> _ConditionalContent<_LimitedAvailabilityCompositorContent, F>](./compositorcontentbuilder/buildeither%28second%29.md)
  Produces content for a conditional statement in a multi-statement closure when the condition is false.
- [static func buildExpression<C>(C) -> C](./compositorcontentbuilder/buildexpression%28_%29.md)
- [static func buildLimitedAvailability(some CompositorContent) -> _LimitedAvailabilityCompositorContent](./compositorcontentbuilder/buildlimitedavailability%28_%29.md)
  Processes scene content for a conditional compiler-control statement that performs an availability check.

## See Also

### Compositing views
- [func blendMode(BlendMode) -> some View](./view/blendmode%28_%29.md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](./view/compositinggroup%28%29.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](./view/drawinggroup%28opaque,colormode%29.md)
  Composites this view’s contents into an offscreen image before final display.
- [enum BlendMode](./blendmode.md)
  Modes for compositing a view with overlapping content.
- [enum ColorRenderingMode](./colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.
- [protocol CompositorContent](./compositorcontent.md)
  A type that describes content a scene renders directly with Metal, rather than composing from SwiftUI views.
- [struct AnyCompositorContent](./anycompositorcontent.md)
  Type erased compositor content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/compositorcontentbuilder)*