# DirectionalLightComponent.Shadow.Cascades

**Framework**: RealityKit  
**Kind**: struct

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
struct Cascades
```

## Topics

### Creating cascades
- [static func fixed(Int, bias: Float) -> DirectionalLightComponent.Shadow.Cascades](directionallightcomponent/shadow/cascades-swift.struct/fixed(_:bias:).md)
  Specify a fixed number of shadow cascades to use.
### Type Properties
- [static var automatic: DirectionalLightComponent.Shadow.Cascades](directionallightcomponent/shadow/cascades-swift.struct/automatic.md)
  Allow the engine to determine the optimal number of shadow cascades to use – depending on the scene and camera configuration in any given frame.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var cascades: DirectionalLightComponent.Shadow.Cascades](directionallightcomponent/shadow/cascades-swift.property.md)
  Number of shadow cascades to use when rendering shadows for this light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/shadow/cascades-swift.struct)*