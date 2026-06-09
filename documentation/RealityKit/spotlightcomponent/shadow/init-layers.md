# init(layers:)

**Framework**: RealityKit  
**Kind**: init

Creates a spot light shadow with the specified layers.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
init(layers: RenderLayer.Set? = nil)
```

## Parameters

- `layers`: The layers from which this light accepts shadow casters. If nil, uses layers for shadow casting.

## See Also

- [init()](spotlightcomponent/shadow/init.md)
  Creates a new spot light shadow object.
- [var layers: RenderLayer.Set?](spotlightcomponent/shadow/layers.md)
  The layers from which this light casts shadows. If nil, uses layers for shadow casting. Only entities whose RenderLayerComponent.layers intersect with these layers will cast shadows in this light’s shadow map. If `nil`, the light uses its `layers` for shadow casting. Set to an empty set to disable shadow casting entirely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/init(layers:))*