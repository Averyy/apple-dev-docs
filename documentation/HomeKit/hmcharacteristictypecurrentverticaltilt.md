# HMCharacteristicTypeCurrentVerticalTilt

**Framework**: HomeKit  
**Kind**: var

The current tilt angle of a vertical slat for an accessory like a window or a fan.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeCurrentVerticalTilt: String
```

#### Discussion

The corresponding value represents the angle in degrees, with a value between -90 and 90.

A value of -90 indicates the slats are fully closed and rotated such that the user-facing edge is to the left of the opposing edge. A value of 0 indicates that the edges are aligned, with the slats fully open.

## See Also

- [let HMCharacteristicTypeCurrentHorizontalTilt: String](hmcharacteristictypecurrenthorizontaltilt.md)
  The current tilt angle of a horizontal slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetHorizontalTilt: String](hmcharacteristictypetargethorizontaltilt.md)
  The target tilt angle of a horizontal slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetVerticalTilt: String](hmcharacteristictypetargetverticaltilt.md)
  The target tilt angle of a vertical slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeCurrentTilt: String](hmcharacteristictypecurrenttilt.md)
  The current tilt angle of a slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetTilt: String](hmcharacteristictypetargettilt.md)
  The target tilt angle of a slat for an accessory like a window or a fan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentverticaltilt)*