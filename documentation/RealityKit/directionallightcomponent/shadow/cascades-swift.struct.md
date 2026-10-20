# DirectionalLightComponent.Shadow.Cascades

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
struct Cascades
```

## Topics

### Creating cascades
- [static func fixed(Int, bias: Float) -> DirectionalLightComponent.Shadow.Cascades](./cascades-swift.struct/fixed%28_,bias%29.md)
  Specify a fixed number of shadow cascades to use.
### Type Properties
- [static var automatic: DirectionalLightComponent.Shadow.Cascades](./cascades-swift.struct/automatic.md)
  Allow the engine to determine the optimal number of shadow cascades to use – depending on the scene and camera configuration in any given frame.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Configuring shadow cascades
- [var cascades: DirectionalLightComponent.Shadow.Cascades](./cascades-swift.property.md)
  Number of shadow cascades to use when rendering shadows for this light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/cascades-swift.struct)*