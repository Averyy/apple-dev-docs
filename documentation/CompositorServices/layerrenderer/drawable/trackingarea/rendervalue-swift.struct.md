# LayerRenderer.Drawable.TrackingArea.RenderValue

**Framework**: Compositor Services  
**Kind**: struct  
**Role**: Structure

A value used when rendering a tracking area.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct RenderValue
```

```c
typedef uint16_t cp_tracking_area_render_value;
```

## Overview

When rendering to [`cp_drawable_get_tracking_areas_texture`](../../../cp_drawable_get_tracking_areas_texture.md) use this value to write the pixel value. Upper bound limit is based on pixel format set by [`cp_layer_renderer_configuration_get_tracking_areas_format`](../../../cp_layer_renderer_configuration_get_tracking_areas_format.md) Can change per-frame for the same rendered mesh/object. A value of 0 is reserved to represent the absence of a tracking area.

## Topics

### Initializers
- [init(UInt16)](./rendervalue-swift.struct/init%28_%29.md)
- [init(rawValue: UInt16)](./rendervalue-swift.struct/init%28rawvalue%29.md)
### Type Properties
- [static let invalid: LayerRenderer.Drawable.TrackingArea.RenderValue](./rendervalue-swift.struct/invalid.md)
  Render value reserved as invalid.

## Relationships

### Conforms To
- [BitwiseCopyable](../../../../Swift/bitwisecopyable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/trackingarea/rendervalue-swift.struct)*