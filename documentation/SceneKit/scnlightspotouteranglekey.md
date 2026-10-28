# SCNLightSpotOuterAngleKey

**Framework**: SceneKit  
**Kind**: var  
**Role**: Global Variable

The angle, in degrees, of the area partially lit by a spotlight.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use the [`spotOuterAngle`](./scnlight/spotouterangle.md) property instead.

## Declaration

```swift
let SCNLightSpotOuterAngleKey: String
```

```c
extern NSString * const SCNLightSpotOuterAngleKey;
```

## Discussion

This attribute’s default value is `45.0`.

## See Also

### Constants
- [let SCNLightAttenuationStartKey: String](./scnlightattenuationstartkey.md)
  The distance from the light at which its intensity begins to diminish.
- [let SCNLightAttenuationEndKey: String](./scnlightattenuationendkey.md)
  The distance from the light at which its intensity is completely diminished.
- [let SCNLightAttenuationFalloffExponentKey: String](./scnlightattenuationfalloffexponentkey.md)
  The transition curve for the light’s intensity between its attenuation start and end distances.
- [let SCNLightSpotInnerAngleKey: String](./scnlightspotinneranglekey.md)
  The angle, in degrees, of the area fully lit by a spotlight.
- [let SCNLightShadowFarClippingKey: String](./scnlightshadowfarclippingkey.md)
  The maximum distance between the light and a visible surface for casting shadows.
- [let SCNLightShadowNearClippingKey: String](./scnlightshadownearclippingkey.md)
  The minimum distance between the light and a visible surface for casting shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlightspotouteranglekey)*