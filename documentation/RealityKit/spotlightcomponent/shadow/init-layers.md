# init(layers:)

**Framework**: RealityKit  
**Kind**: init

Creates a spot light shadow that accepts shadow casters from the specified layers.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
init(layers: RenderLayer.Set? = nil)
```

## Parameters

- `layers`: The layers of entities that cast shadows from this light. Pass `nil` (the default) to inherit [`layers`](spotlightcomponent/layers.md), or an empty set to disable shadow casting entirely.

## See Also

- [init()](spotlightcomponent/shadow/init.md)
  Creates a new spot light shadow object.
- [var layers: RenderLayer.Set?](spotlightcomponent/shadow/layers.md)
  The layers of entities that cast shadows from this light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spotlightcomponent/shadow/init(layers:))*