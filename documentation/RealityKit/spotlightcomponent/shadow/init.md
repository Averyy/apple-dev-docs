# init()

**Framework**: RealityKit  
**Kind**: init

Creates a new spot light shadow object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
init()
```

## See Also

- [init(layers: RenderLayer.Set?)](spotlightcomponent/shadow/init(layers:).md)
  Creates a spot light shadow with the specified layers.
- [var layers: RenderLayer.Set?](spotlightcomponent/shadow/layers.md)
  The layers from which this light casts shadows. If nil, uses layers for shadow casting. Only entities whose RenderLayerComponent.layers intersect with these layers will cast shadows in this light’s shadow map. If `nil`, the light uses its `layers` for shadow casting. Set to an empty set to disable shadow casting entirely.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/init())*