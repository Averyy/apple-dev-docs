# init(color:intensity:isRealWorldProxy:)

**Framework**: RealityKit  
**Kind**: init  
**Role**: Initializer

Creates a directional light with a configuration.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- tvOS 26.0+

## Declaration

```swift
init(color: DirectionalLightComponent.Color = .white, intensity: Float = 2145.7078, isRealWorldProxy: Bool = false)
```

**Other overloads**:

```swift
init(color: DirectionalLightComponent.Color = .white, intensity: Float = 2145.7078, isRealWorldProxy: Bool = false)
```

## Parameters

- `color`: A color for the light.
- `intensity`: The intensity of the light, measured in lumen per square meter.
- `isRealWorldProxy`: A Boolean that you use to control whether the light operates as a proxy for a real-world light.

## See Also

### Creating a directional light
- [init(color: DirectionalLightComponent.Color, intensity: Float)](./init%28color,intensity%29.md)
  Creates a directional light with a configuration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/init(color:intensity:isrealworldproxy:)-42x82)*