# numberOfTouchesRequired

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of necessary touches on a Touch Bar for the gesture recognizer to match.

**Availability**:
- macOS 10.12.2+

## Declaration

```swift
var numberOfTouchesRequired: Int { get set }
```

```objc
@property NSInteger numberOfTouchesRequired;
```

## See Also

### Related Documentation
- [class NSTouchBar](../nstouchbar.md)
  An object that provides dynamic contextual controls in the Touch Bar of supported models of MacBook Pro.
### Configuring the gesture recognizer
- [var allowableMovement: CGFloat](./allowablemovement.md)
  The maximum movement of the mouse in the view before the gesture fails.
- [var buttonMask: Int](./buttonmask.md)
  A bit mask of the buttons required to recognize this press.
- [var minimumPressDuration: TimeInterval](./minimumpressduration.md)
  The minimum time (in seconds) that the user must hold the mouse button in the view for a valid gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer/numberoftouchesrequired)*