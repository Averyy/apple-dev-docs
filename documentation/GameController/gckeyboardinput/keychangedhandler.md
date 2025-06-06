# keyChangedHandler

**Framework**: Game Controller  
**Kind**: property

The block that the profile calls when the user presses a key.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var keyChangedHandler: GCKeyboardValueChangedHandler? { get set }
```

#### Discussion

If multiple keys change values at the same time, the profile calls this block once for each key that changes.

## See Also

- [typealias GCKeyboardValueChangedHandler](gckeyboardvaluechangedhandler.md)
  The signature for the block that the keyboard input profile calls when a key value changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/gamecontroller/gckeyboardinput/keychangedhandler)*