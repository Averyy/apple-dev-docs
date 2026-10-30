# buttonMask

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A bit mask of the button (or buttons) required to recognize this click.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var buttonMask: Int { get set }
```

```objc
@property NSUInteger buttonMask;
```

## Discussion

Bit `0` represents the primary button, bit `1` is the secondary button, and so on. So to track clicks of the secondary button, assign the value `0x2` (which corresponds to a `1` in bit `1`) to this property. The default value of this property is `0x1`, which detects clicks in the primary mouse button.

Set this property to `0` to make the gesture recognizer recognize only direct touches on a Mac with a touch display, and ignore mouse and trackpad input. Use this to add touch support to a view that handles the mouse or trackpad in another way, such as with a tracking loop, without the gesture recognizer competing for mouse input. Direct touches are allowed by default; see [`allowedTouchTypes`](../nsgesturerecognizer/allowedtouchtypes.md).

Changing the value of this property also sets the values of the [`delaysPrimaryMouseButtonEvents`](../nsgesturerecognizer/delaysprimarymousebuttonevents.md), [`delaysSecondaryMouseButtonEvents`](../nsgesturerecognizer/delayssecondarymousebuttonevents.md), and [`delaysOtherMouseButtonEvents`](../nsgesturerecognizer/delaysothermousebuttonevents.md) properties to [`true`](../../Swift/true.md) for each of the buttons you specified.

## See Also

### Configuring the gesture
- [var numberOfClicksRequired: Int](./numberofclicksrequired.md)
  The number of clicks required to match.
- [var numberOfTouchesRequired: Int](./numberoftouchesrequired.md)
  The number of touches required in an [`NSTouchBar`](../nstouchbar.md) object for the gesture recognizer to match.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsclickgesturerecognizer/buttonmask)*