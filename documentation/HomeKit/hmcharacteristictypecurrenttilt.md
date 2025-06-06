# HMCharacteristicTypeCurrentTilt

**Framework**: HomeKit  
**Kind**: var

The current tilt angle of a slat for an accessory like a window or a fan.

**Availability**:
- iOS 10.2+
- iPadOS 10.2+
- Mac Catalyst 10.2+
- tvOS 10.1+
- visionOS 1.0+
- watchOS 3.1.1+

## Declaration

```swift
let HMCharacteristicTypeCurrentTilt: String
```

#### Discussion

The corresponding value represents the angle in degrees, with a value between -90 and 90.

For horizontal slats, a value of -90 indicates the slats are fully closed and rotated such that the user-facing edge is higher than the opposing edge. For vertical slats, this value indicates that the user-facing edge is to the left of the opposing edge. In either case, a value of 0 indicates that the edges are aligned, with the slats fully open.

## See Also

- [let HMCharacteristicTypeCurrentHorizontalTilt: String](hmcharacteristictypecurrenthorizontaltilt.md)
  The current tilt angle of a horizontal slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetHorizontalTilt: String](hmcharacteristictypetargethorizontaltilt.md)
  The target tilt angle of a horizontal slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeCurrentVerticalTilt: String](hmcharacteristictypecurrentverticaltilt.md)
  The current tilt angle of a vertical slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetVerticalTilt: String](hmcharacteristictypetargetverticaltilt.md)
  The target tilt angle of a vertical slat for an accessory like a window or a fan.
- [let HMCharacteristicTypeTargetTilt: String](hmcharacteristictypetargettilt.md)
  The target tilt angle of a slat for an accessory like a window or a fan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrenttilt)*