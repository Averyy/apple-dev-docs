# Lighting Attribute Keys

**Framework**: SceneKit

Keys for specifying the behavior of a light using the [`attribute(forKey:)`](scnlight/attribute(forkey:).md) and [`setAttribute(_:forKey:)`](scnlight/setattribute(_:forkey:).md) methods.

#### Overview

You can also get, set, or animate changes to the values of lighting attributes using [`Key-value coding`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/KeyValueCoding.html#//apple_ref/doc/uid/TP40008195-CH25) with the keys listed above.

You provide or retrieve a value for each key as an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the appropriate numeric type.

## Topics

### Constants
- [let SCNLightAttenuationStartKey: String](scnlightattenuationstartkey.md)
  The distance from the light at which its intensity begins to diminish.
- [let SCNLightAttenuationEndKey: String](scnlightattenuationendkey.md)
  The distance from the light at which its intensity is completely diminished.
- [let SCNLightAttenuationFalloffExponentKey: String](scnlightattenuationfalloffexponentkey.md)
  The transition curve for the light’s intensity between its attenuation start and end distances.
- [let SCNLightSpotInnerAngleKey: String](scnlightspotinneranglekey.md)
  The angle, in degrees, of the area fully lit by a spotlight.
- [let SCNLightSpotOuterAngleKey: String](scnlightspotouteranglekey.md)
  The angle, in degrees, of the area partially lit by a spotlight.
- [let SCNLightShadowFarClippingKey: String](scnlightshadowfarclippingkey.md)
  The maximum distance between the light and a visible surface for casting shadows.
- [let SCNLightShadowNearClippingKey: String](scnlightshadownearclippingkey.md)
  The minimum distance between the light and a visible surface for casting shadows.

## See Also

- [var name: String?](scnlight/name.md)
  A name associated with the light.
- [func attribute(forKey: String) -> Any?](scnlight/attribute(forkey:).md)
  Returns the value of a lighting attribute.
- [func setAttribute(Any?, forKey: String)](scnlight/setattribute(_:forkey:).md)
  Sets the value for a lighting attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/lighting-attribute-keys)*