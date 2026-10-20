# AnyCompositorContent

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

Type erased compositor content.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
nonisolated
struct AnyCompositorContent
```

## Topics

### Initializers
- [init<T>(T)](./anycompositorcontent/init%28_%29.md)
  Create an instance that type-erases `CompositorContent`.
- [init<T>(erasing: T)](./anycompositorcontent/init%28erasing%29.md)

## Relationships

### Conforms To
- [CompositorContent](./compositorcontent.md)

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
- [struct CompositorContentBuilder](./compositorcontentbuilder.md)
  A result builder for composing a collection of [`CompositorContent`](./compositorcontent.md) elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anycompositorcontent)*