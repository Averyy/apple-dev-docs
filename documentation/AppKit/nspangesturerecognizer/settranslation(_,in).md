# setTranslation(_:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Changes the current translation value of the gesture recognizer.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func setTranslation(_ translation: NSPoint, in view: NSView?)
```

```objc
- (void) setTranslation:(NSPoint) translation inView:(NSView *) view;
```

## Discussion

This method changes the current translation value of the gesture recognizer. Changing the value resets the velocity of the pan. You might call this method at mouse-down time to adjust the translation value and make it relative to some specific point in your view.

## Parameters

- `translation`: The new translation values to use in the gesture recognizer.
- `view`: The view in whose coordinate system you specified the new translation value. Specifying `nil` resets the previous translation value.

## See Also

### Tracking the location and velocity of the gesture
- [func translation(in: NSView?) -> NSPoint](./translation%28in%29.md)
  The distance traveled by the mouse during the gesture.
- [func velocity(in: NSView?) -> NSPoint](./velocity%28in%29.md)
  The velocity of the pan, measured in points per second.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/settranslation(_:in:))*