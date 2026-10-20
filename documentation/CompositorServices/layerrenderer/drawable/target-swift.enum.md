# LayerRenderer.Drawable.Target

**Framework**: Compositor Services  
**Kind**: enum  
**Role**: Enumeration

The target where the drawable will be displayed/used.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Target
```

```c
enum cp_drawable_target : uint32_t;
```

#### Overview

Use these constants to determine whether content should be drawn for certain targets.

## Topics

### Enumeration Cases
- [LayerRenderer.Drawable.Target.builtIn](./target-swift.enum/builtin.md)
  A drawable that is targeting the built-in display, this is what a user will see in the device.
- [LayerRenderer.Drawable.Target.capture](./target-swift.enum/capture.md)
  A drawable that will be used for capture purposes, this could be used for video or AirPlay streaming and will be visible to users outside of the device.
### Initializers
- [init?(rawValue: UInt32)](./target-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Retrieving the target
- [var target: LayerRenderer.Drawable.Target](./target-swift.property.md)
  Returns a value that indicates the target of the drawable type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/target-swift.enum)*