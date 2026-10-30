# allowedTouchTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The touch types that this gesture recognizer accepts.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var allowedTouchTypes: NSTouch.TouchTypeMask { get set }
```

```objc
@property NSTouchTypeMask allowedTouchTypes;
```

## Mentions

- [Adopting gesture recognizers in your app](../adopting-gesture-recognizers-in-your-app.md)

## Discussion

Gesture recognizers only support direct touches, such as those from a Mac with a touch display or a Sidecar-connected iPad. Setting this property to include [`indirect`](../nstouch/touchtypemask/indirect.md) — for touches from a trackpad — isn’t supported.

This property defaults to [`direct`](../nstouch/touchtypemask/direct.md) as of macOS 27. On earlier releases, it defaults to an empty mask, so set it explicitly if your gesture recognizer needs to receive touches.

## See Also

### Getting additional recognizer information
- [var isCancellableByScrollGesture: Bool](./iscancellablebyscrollgesture.md)
  Causes the receiver to be cancelled when its enclosing scroll view’s gesture recognizer begins.
- [var modifierFlags: NSEvent.ModifierFlags](./modifierflags.md)
  The keyboard modifier flags in effect while the receiver last processed an event.
- [var name: String?](./name.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/allowedtouchtypes)*