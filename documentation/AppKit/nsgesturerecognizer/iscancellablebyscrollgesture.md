# isCancellableByScrollGesture

**Framework**: AppKit  
**Kind**: property

Causes the receiver to be cancelled when its enclosing scroll view’s gesture recognizer begins.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var isCancellableByScrollGesture: Bool { get set }
```

#### Discussion

Defaults to `false`.

## See Also

- [var allowedTouchTypes: NSTouch.TouchTypeMask](nsgesturerecognizer/allowedtouchtypes.md)
- [var modifierFlags: NSEvent.ModifierFlags](nsgesturerecognizer/modifierflags.md)
  The keyboard modifier flags in effect while the receiver last processed an event.
- [var name: String?](nsgesturerecognizer/name.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/iscancellablebyscrollgesture)*