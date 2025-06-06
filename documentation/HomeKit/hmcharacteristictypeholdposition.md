# HMCharacteristicTypeHoldPosition

**Framework**: HomeKit  
**Kind**: var

A control for holding the position of an accessory like a door or window.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 9.0+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let HMCharacteristicTypeHoldPosition: String
```

#### Discussion

The corresponding value is a write-only Boolean. Write a value of `true` to indicate that the current position should be maintained. The accessory ignores a written value of `false`. Write a value to the [`HMCharacteristicTypeTargetPosition`](hmcharacteristictypetargetposition.md) characteristic to release the hold.

## See Also

- [let HMCharacteristicTypeCurrentDoorState: String](hmcharacteristictypecurrentdoorstate.md)
  The current door state.
- [let HMCharacteristicTypeTargetDoorState: String](hmcharacteristictypetargetdoorstate.md)
  The target door state.
- [let HMCharacteristicTypeCurrentPosition: String](hmcharacteristictypecurrentposition.md)
  The current position of a door, window, awning, or window covering.
- [let HMCharacteristicTypeTargetPosition: String](hmcharacteristictypetargetposition.md)
  The target position of a door, window, awning, or window covering.
- [let HMCharacteristicTypePositionState: String](hmcharacteristictypepositionstate.md)
  The position of an accessory like a door, window, awning, or window covering.
- [let HMCharacteristicTypeStatusJammed: String](hmcharacteristictypestatusjammed.md)
  An indicator of whether an accessory is jammed.
- [let HMCharacteristicTypeSlatType: String](hmcharacteristictypeslattype.md)
  The type of slat on an accessory like a window or a fan.
- [let HMCharacteristicTypeCurrentSlatState: String](hmcharacteristictypecurrentslatstate.md)
  The current state of slats on an accessory like a window or a fan.


---

*[View on Apple Developer](https://developer.apple.com/documentation/homekit/hmcharacteristictypeholdposition)*