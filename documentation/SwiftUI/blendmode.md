# BlendMode

**Framework**: SwiftUI  
**Kind**: enum

Modes for compositing a view with overlapping content.

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
enum BlendMode
```

## Topics

### Getting the default
- [BlendMode.normal](blendmode/normal.md)
### Darkening
- [BlendMode.darken](blendmode/darken.md)
- [BlendMode.multiply](blendmode/multiply.md)
- [BlendMode.colorBurn](blendmode/colorburn.md)
- [BlendMode.plusDarker](blendmode/plusdarker.md)
### Lightening
- [BlendMode.lighten](blendmode/lighten.md)
- [BlendMode.screen](blendmode/screen.md)
- [BlendMode.colorDodge](blendmode/colordodge.md)
- [BlendMode.plusLighter](blendmode/pluslighter.md)
### Adding contrast
- [BlendMode.overlay](blendmode/overlay.md)
- [BlendMode.softLight](blendmode/softlight.md)
- [BlendMode.hardLight](blendmode/hardlight.md)
### Inverting
- [BlendMode.difference](blendmode/difference.md)
- [BlendMode.exclusion](blendmode/exclusion.md)
### Mixing color components
- [BlendMode.hue](blendmode/hue.md)
- [BlendMode.saturation](blendmode/saturation.md)
- [BlendMode.color](blendmode/color.md)
- [BlendMode.luminosity](blendmode/luminosity.md)
### Accessing porter-duff modes
- [BlendMode.sourceAtop](blendmode/sourceatop.md)
- [BlendMode.destinationOver](blendmode/destinationover.md)
- [BlendMode.destinationOut](blendmode/destinationout.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [func blendMode(BlendMode) -> some View](view/blendmode(_:).md)
  Sets the blend mode for compositing this view with overlapping views.
- [func compositingGroup() -> some View](view/compositinggroup.md)
  Wraps this view in a compositing group.
- [func drawingGroup(opaque: Bool, colorMode: ColorRenderingMode) -> some View](view/drawinggroup(opaque:colormode:).md)
  Composites this view’s contents into an offscreen image before final display.
- [enum ColorRenderingMode](colorrenderingmode.md)
  The set of possible working color spaces for color-compositing operations.
- [protocol CompositorContent](compositorcontent.md)
- [struct CompositorContentBuilder](compositorcontentbuilder.md)
  A result builder for composing a collection of [`CompositorContent`](compositorcontent.md) elements.
- [struct AnyCompositorContent](anycompositorcontent.md)
  Type erased compositor content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/blendmode)*