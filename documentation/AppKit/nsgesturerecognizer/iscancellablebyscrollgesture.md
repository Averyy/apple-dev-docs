# isCancellableByScrollGesture

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Causes the receiver to be cancelled when its enclosing scroll view’s gesture recognizer begins.

**Availability**:
- macOS 27.0+

## Declaration

```swift
var isCancellableByScrollGesture: Bool { get set }
```

```objc
@property (getter=isCancellableByScrollGesture) BOOL cancellableByScrollGesture;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## Discussion

Defaults to `false`.

## See Also

### Getting additional recognizer information
- [var allowedTouchTypes: NSTouch.TouchTypeMask](./allowedtouchtypes.md)
  The touch types that this gesture recognizer accepts.
- [var modifierFlags: NSEvent.ModifierFlags](./modifierflags.md)
  The keyboard modifier flags in effect while the receiver last processed an event.
- [var name: String?](./name.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/iscancellablebyscrollgesture)*