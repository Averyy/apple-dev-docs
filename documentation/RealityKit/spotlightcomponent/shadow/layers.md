# layers

**Framework**: RealityKit  
**Kind**: property

The layers from which this light casts shadows. If nil, uses layers for shadow casting. Only entities whose RenderLayerComponent.layers intersect with these layers will cast shadows in this light’s shadow map. If `nil`, the light uses its `layers` for shadow casting. Set to an empty set to disable shadow casting entirely.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
var layers: RenderLayer.Set? { get set }
```

## See Also

- [init()](spotlightcomponent/shadow/init.md)
  Creates a new spot light shadow object.
- [init(layers: RenderLayer.Set?)](spotlightcomponent/shadow/init(layers:).md)
  Creates a spot light shadow with the specified layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/layers)*