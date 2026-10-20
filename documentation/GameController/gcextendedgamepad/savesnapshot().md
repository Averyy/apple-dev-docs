# saveSnapshot()

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Saves a snapshot of all of the profile’s elements.

**Availability**:
- iOS 7.0+ - Deprecated in 13.0
- iPadOS 7.0+ - Deprecated in 13.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- macOS 10.9+ - Deprecated in 10.15
- tvOS 9.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`capture()`](../gccontroller/capture%28%29.md) method instead.

## Declaration

```swift
func saveSnapshot() -> GCExtendedGamepadSnapshot
```

```objc
- (GCExtendedGamepadSnapshot *) saveSnapshot;
```

#### Return Value

A snapshot that is a copy of the controller at a moment in time, and has element values you can set.

## See Also

### Setting snapshot values
- [func setStateFrom(GCExtendedGamepad)](./setstatefrom%28_%29.md)
  Copies the input values from a specified extended gamepad to a snapshot of an extended gamepad.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcextendedgamepad/savesnapshot())*