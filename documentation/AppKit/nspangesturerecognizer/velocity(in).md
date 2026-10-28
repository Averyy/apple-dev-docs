# velocity(in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

The velocity of the pan, measured in points per second.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func velocity(in view: NSView?) -> NSPoint
```

```objc
- (NSPoint) velocityInView:(NSView *) view;
```

## Return Value

The horizontal and vertical velocity of the pan gesture. These values are relative to the specified view.

## Parameters

- `view`: The view that provides the coordinate system for computing the velocity value. This parameter must not be `nil`.

## See Also

### Tracking the location and velocity of the gesture
- [func translation(in: NSView?) -> NSPoint](./translation%28in%29.md)
  The distance traveled by the mouse during the gesture.
- [func setTranslation(NSPoint, in: NSView?)](./settranslation%28_,in%29.md)
  Changes the current translation value of the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspangesturerecognizer/velocity(in:))*