# setStateFrom(_:)

**Framework**: Game Controller  
**Kind**: method  
**Role**: Instance Method

Copies the input values from a specified micro gamepad to a snapshot of a micro gamepad.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
func setStateFrom(_ microGamepad: GCMicroGamepad)
```

```objc
- (void) setStateFromMicroGamepad:(GCMicroGamepad *) microGamepad;
```

## Parameters

- `microGamepad`: The micro gamepad to copy the input values from.

## See Also

### Setting snapshot avlues
- [func saveSnapshot() -> GCMicroGamepadSnapshot](./savesnapshot%28%29.md)
  Saves a snapshot of all of the profile’s elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gcmicrogamepad/setstatefrom(_:))*