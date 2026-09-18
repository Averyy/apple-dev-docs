# modifierFlags

**Framework**: AppKit  
**Kind**: property

The keyboard modifier flags in effect while the receiver last processed an event.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var modifierFlags: NSEvent.ModifierFlags { get }
```

#### Discussion

Use this property from an action method or delegate callback to determine which modifier keys, such as Shift or Command, were held down as part of the gesture.

## See Also

- [var allowedTouchTypes: NSTouch.TouchTypeMask](nsgesturerecognizer/allowedtouchtypes.md)
- [var isCancellableByScrollGesture: Bool](nsgesturerecognizer/iscancellablebyscrollgesture.md)
  Causes the receiver to be cancelled when its enclosing scroll view’s gesture recognizer begins.
- [var name: String?](nsgesturerecognizer/name.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/modifierflags)*