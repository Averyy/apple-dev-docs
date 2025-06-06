# isRealWorldProxy

**Framework**: RealityKit  
**Kind**: property

A Boolean that you use to control whether the directional light operates as a proxy for a real-world light.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+

## Declaration

```swift
var isRealWorldProxy: Bool
```

#### Discussion

Set the value to `true` when you want the light to cast shadows on virtual content without illuminating anything in the scene. You can use this to create shadows on occlusion materials that accept dynamic lighting.

## See Also

- [var intensity: Float](directionallightcomponent/intensity.md)
  The intensity of the directional light, measured in lumen per square meter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/isrealworldproxy)*