# LayerRenderer.Drawable.Target

**Framework**: Compositor Services  
**Kind**: enum

The target where the drawable will be displayed/used.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Target
```

#### Overview

Use these constants to determine whether content should be drawn for certain targets.

## Topics

### Enumeration Cases
- [LayerRenderer.Drawable.Target.builtIn](layerrenderer/drawable/target-swift.enum/builtin.md)
  A drawable that is targeting the built-in display, this is what a user will see in the device.
- [LayerRenderer.Drawable.Target.capture](layerrenderer/drawable/target-swift.enum/capture.md)
  A drawable that will be used for capture purposes, this could be used for video or AirPlay streaming and will be visible to users outside of the device.
### Initializers
- [init?(rawValue: UInt32)](layerrenderer/drawable/target-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var target: LayerRenderer.Drawable.Target](layerrenderer/drawable/target-swift.property.md)
  Returns a value that indicates the target of the drawable type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/target-swift.enum)*