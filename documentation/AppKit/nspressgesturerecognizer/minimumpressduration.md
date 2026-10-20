# minimumPressDuration

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The minimum time (in seconds) that the user must hold the mouse button in the view for a valid gesture.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var minimumPressDuration: TimeInterval { get set }
```

```objc
@property NSTimeInterval minimumPressDuration;
```

#### Discussion

The default value of this property is the same as the current double-click interval.

## See Also

### Configuring the gesture recognizer
- [var allowableMovement: CGFloat](./allowablemovement.md)
  The maximum movement of the mouse in the view before the gesture fails.
- [var buttonMask: Int](./buttonmask.md)
  A bit mask of the buttons required to recognize this press.
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer/minimumpressduration)*