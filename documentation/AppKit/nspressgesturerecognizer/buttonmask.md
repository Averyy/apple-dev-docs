# buttonMask

**Framework**: AppKit  
**Kind**: property

A bit mask of the buttons required to recognize this press.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var buttonMask: Int { get set }
```

#### Discussion

Bit 0 represents the primary button, bit 1 is the secondary button, and so on. So to track clicks of the secondary button, assign the value `0x2` (which corresponds to a `1` in bit 1) to this property. The default value of this property is `0x1`, which detects clicks in the primary mouse button.

Changing the value of this property also sets the values of the [`delaysPrimaryMouseButtonEvents`](nsgesturerecognizer/delaysprimarymousebuttonevents.md), [`delaysSecondaryMouseButtonEvents`](nsgesturerecognizer/delayssecondarymousebuttonevents.md), and [`delaysOtherMouseButtonEvents`](nsgesturerecognizer/delaysothermousebuttonevents.md) properties to [`true`](https://developer.apple.com/documentation/Swift/true) for each of the buttons you specified.

## See Also

- [var allowableMovement: CGFloat](nspressgesturerecognizer/allowablemovement.md)
  The maximum movement of the mouse in the view before the gesture fails.
- [var minimumPressDuration: TimeInterval](nspressgesturerecognizer/minimumpressduration.md)
  The minimum time (in seconds) that the user must hold the mouse button in the view for a valid gesture.
- [var numberOfTouchesRequired: Int](nspressgesturerecognizer/numberoftouchesrequired.md)
  The number of necessary touches on a Touch Bar for the gesture recognizer to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspressgesturerecognizer/buttonmask)*