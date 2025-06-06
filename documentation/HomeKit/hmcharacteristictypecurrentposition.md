# HMCharacteristicTypeCurrentPosition

**Framework**: HomeKit  
**Kind**: var

The current position of a door, window, awning, or window covering.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeCurrentPosition: String
```

#### Discussion

The corresponding value is an integer percentage. A value of `0` indicates a door or window is fully closed, or that awnings or shades permit the least possible light. A value of `100` indicates the opposite.

## See Also

- [let HMCharacteristicTypeCurrentDoorState: String](hmcharacteristictypecurrentdoorstate.md)
  The current door state.
- [let HMCharacteristicTypeTargetDoorState: String](hmcharacteristictypetargetdoorstate.md)
  The target door state.
- [let HMCharacteristicTypeTargetPosition: String](hmcharacteristictypetargetposition.md)
  The target position of a door, window, awning, or window covering.
- [let HMCharacteristicTypePositionState: String](hmcharacteristictypepositionstate.md)
  The position of an accessory like a door, window, awning, or window covering.
- [let HMCharacteristicTypeStatusJammed: String](hmcharacteristictypestatusjammed.md)
  An indicator of whether an accessory is jammed.
- [let HMCharacteristicTypeHoldPosition: String](hmcharacteristictypeholdposition.md)
  A control for holding the position of an accessory like a door or window.
- [let HMCharacteristicTypeSlatType: String](hmcharacteristictypeslattype.md)
  The type of slat on an accessory like a window or a fan.
- [let HMCharacteristicTypeCurrentSlatState: String](hmcharacteristictypecurrentslatstate.md)
  The current state of slats on an accessory like a window or a fan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypecurrentposition)*