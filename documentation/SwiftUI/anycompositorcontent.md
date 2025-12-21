# AnyCompositorContent

**Framework**: SwiftUI  
**Kind**: struct

Type erased compositor content.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct AnyCompositorContent
```

## Topics

### Initializers
- [init<T>(T)](anycompositorcontent/init(_:).md)
  Create an instance that type-erases `CompositorContent`.
- [init<T>(erasing: T)](anycompositorcontent/init(erasing:).md)

## Relationships

### Conforms To
- [CompositorContent](compositorcontent.md)

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
- [struct CompositorContentBuilder](compositorcontentbuilder.md)
  A result builder for composing a collection of [`CompositorContent`](compositorcontent.md) elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/anycompositorcontent)*