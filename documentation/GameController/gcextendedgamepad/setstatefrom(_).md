# setStateFrom(_:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Copies the input values from a specified extended gamepad to a snapshot of an extended gamepad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setStateFrom(_ extendedGamepad: GCExtendedGamepad)
```

```objc
- (void) setStateFromExtendedGamepad:(GCExtendedGamepad *) extendedGamepad;
```

## Discussion

If this extended gamepad isn’t a snapshot, this method does nothing. A snapshot is a copy of a controller at a moment in time that has element values you can set.

## Parameters

- `extendedGamepad`: The extended gamepad to copy the input values from.

## See Also

### Setting snapshot values
- [func saveSnapshot() -> GCExtendedGamepadSnapshot](./savesnapshot%28%29.md)
  Saves a snapshot of all of the profile’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/setstatefrom(_:))*