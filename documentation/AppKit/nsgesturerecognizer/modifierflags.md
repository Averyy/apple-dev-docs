# modifierFlags

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The keyboard modifier flags in effect while the receiver last processed an event.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var modifierFlags: NSEvent.ModifierFlags { get }
```

```objc
@property (readonly) NSEventModifierFlags modifierFlags;
```

## Discussion

Use this property from an action method or delegate callback to determine which modifier keys, such as Shift or Command, were held down as part of the gesture.

## See Also

### Getting additional recognizer information
- [var allowedTouchTypes: NSTouch.TouchTypeMask](./allowedtouchtypes.md)
- [var isCancellableByScrollGesture: Bool](./iscancellablebyscrollgesture.md)
  Causes the receiver to be cancelled when its enclosing scroll view’s gesture recognizer begins.
- [var name: String?](./name.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizer/modifierflags)*