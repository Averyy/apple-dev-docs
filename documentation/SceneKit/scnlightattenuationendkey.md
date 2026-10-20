# SCNLightAttenuationEndKey

**Framework**: SceneKit  
**Kind**: var  
**Role**: Global Variable

The distance from the light at which its intensity is completely diminished.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: Use the [`attenuationEndDistance`](./scnlight/attenuationenddistance.md) property instead.

## Declaration

```swift
let SCNLightAttenuationEndKey: String
```

```c
extern NSString * const SCNLightAttenuationEndKey;
```

## See Also

### Constants
- [let SCNLightAttenuationStartKey: String](./scnlightattenuationstartkey.md)
  The distance from the light at which its intensity begins to diminish.
- [let SCNLightAttenuationFalloffExponentKey: String](./scnlightattenuationfalloffexponentkey.md)
  The transition curve for the light’s intensity between its attenuation start and end distances.
- [let SCNLightSpotInnerAngleKey: String](./scnlightspotinneranglekey.md)
  The angle, in degrees, of the area fully lit by a spotlight.
- [let SCNLightSpotOuterAngleKey: String](./scnlightspotouteranglekey.md)
  The angle, in degrees, of the area partially lit by a spotlight.
- [let SCNLightShadowFarClippingKey: String](./scnlightshadowfarclippingkey.md)
  The maximum distance between the light and a visible surface for casting shadows.
- [let SCNLightShadowNearClippingKey: String](./scnlightshadownearclippingkey.md)
  The minimum distance between the light and a visible surface for casting shadows.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnlightattenuationendkey)*