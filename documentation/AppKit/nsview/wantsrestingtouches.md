# wantsRestingTouches

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the view wants resting touches.

**Availability**:
- macOS 10.6+

## Declaration

```swift
var wantsRestingTouches: Bool { get set }
```

```objc
@property BOOL wantsRestingTouches;
```

#### Discussion

A resting touch occurs when a user rests their thumb on a device (for example, the glass trackpad of a MacBook). By default, these touches are not delivered and are not included in the event’s set of touches. Touches may transition in and out of resting at any time. Unless the view wants resting touches, began / ended events are simulated as touches transition from resting to active and vice versa.

The default value of this property is [`false`](../../Swift/false.md), which indicates that the view does not want resting touches.

## See Also

### Handling Touch Events
- [var allowedTouchTypes: NSTouch.TouchTypeMask](./allowedtouchtypes.md)
  The types of touch interactions the view allows.
- [var candidateListTouchBarItem: NSCandidateListTouchBarItem<AnyObject>?](./candidatelisttouchbaritem.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/wantsrestingtouches)*