# setTranslation(_:in:)

**Framework**: AppKit  
**Kind**: method

Changes the current translation value of the gesture recognizer.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func setTranslation(_ translation: NSPoint, in view: NSView?)
```

#### Discussion

This method changes the current translation value of the gesture recognizer. Changing the value resets the velocity of the pan. You might call this method at mouse-down time to adjust the translation value and make it relative to some specific point in your view.

## Parameters

- `translation`: The new translation values to use in the gesture recognizer.
- `view`: The view in whose coordinate system you specified the new translation value. Specifying   resets the previous translation value.

## See Also

- [func translation(in: NSView?) -> NSPoint](nspangesturerecognizer/translation(in:).md)
  The distance traveled by the mouse during the gesture.
- [func velocity(in: NSView?) -> NSPoint](nspangesturerecognizer/velocity(in:).md)
  The velocity of the pan, measured in points per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/settranslation(_:in:))*