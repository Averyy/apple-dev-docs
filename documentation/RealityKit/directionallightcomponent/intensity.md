# intensity

**Framework**: RealityKit  
**Kind**: property

The intensity of the directional light, measured in lumen per square meter.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS 2.0+

## Declaration

```swift
var intensity: Float
```

#### Discussion

Lumen per square meter, also known as lux, measures how much light is spread over an area. It tells you how bright a surface appears based on the light it receives.

The default value for this property is `2145.7078`.

Use the following table as an estimate for Lux levels:

| Environment | Typical Lux Level |
| --- | --- |
| Full moon | 0.1 - 1 lux |
| Street lighting | 10 - 20 lux |
| Living room lighting | 50 - 100 lux |
| Classroom | 250 - 750 lux |
| Office lighting | 300 - 500 lux |
| Sunrise/Sunset on a clear day | 400 lux |
| Overcast daylight | 1000 - 2000 lux |
| Photography studio lighting | 1,000 - 2,000 lux |
| Ambient daylight | 10,000 - 25,000 lux |
| Direct sunlight | 32,000 - 100,000 lux |

## See Also

- [var isRealWorldProxy: Bool](directionallightcomponent/isrealworldproxy.md)
  A Boolean that you use to control whether the directional light operates as a proxy for a real-world light.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/directionallightcomponent/intensity)*