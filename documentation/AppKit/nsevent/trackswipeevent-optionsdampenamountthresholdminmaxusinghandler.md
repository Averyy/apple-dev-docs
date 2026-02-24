# trackSwipeEvent(options:dampenAmountThresholdMin:max:usingHandler:)

**Framework**: AppKit  
**Kind**: method

Allows tracking and user interface feedback of scroll wheel events.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func trackSwipeEvent(options: NSEvent.SwipeTrackingOptions = [], dampenAmountThresholdMin minDampenThreshold: CGFloat, max maxDampenThreshold: CGFloat, usingHandler trackingHandler: @escaping (CGFloat, NSEvent.Phase, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)
```

#### Discussion

Scroll wheel swipes are tracked not only to the end of the physical gesture phase by the user, but also to the completion of any user interface animation that should be performed. Using this method allows your implementation to maintain a consistent fluid feel with other applications. Any gesture amount outside of the supplied minimum and maximum dampen amount is pre-dampened for you to provide an elastic feel.

The swipe `gestureAmount` that would fall outside of the range specified by the `minDampenThreshold` and `maxDampenThreshold` are automatically dampened. For example, the user’s physical swipe action results in a value of .50, however, there is no page in that direction to swipe to. The `gestureAmount` reported is adjusted by a damping factor resulting in something like .125. As a developer, you simply treat the `gestureAmount` like you normally do, and the result is an elastic feedback effect to let the user know that there is nothing to swipe to in that direction.

> **Note**:  This method returns immediately and tracking is performed asynchronously.

## Parameters

- `options`: The swipe tracking events. See [`NSEvent.SwipeTrackingOptions`](nsevent/swipetrackingoptions.md) for possible values.
- `minDampenThreshold`: The minimum dampen threshold. This value is considered to encompass the “current view content area” and is referred to as a page. This is the number of pages with a negative position relative to the current page. The value must be less than or equal to zero.
- `maxDampenThreshold`: The maximum dampen threshold. This value is considered to encompass the “current view content area” and is referred to as a page. This is the number of pages with a positive position relative to the current page. The value must be greater than or equal to zero.
- `trackingHandler`: The Block used as the tracking handler. The Block takes four arguments: - **gestureAmount**: The amount of gesture that you should display in the user interface. This may be a fractional amount. The direction of the gestureAmount matches the user’s “scroll content” preference setting as set in [`isDirectionInvertedFromDevice`](nsevent/isdirectioninvertedfromdevice.md), which is based on a user preference. Upon completion, the gesture amount will animate to one of the following values: -1, 0, 1. - **phase**: The phase of the physical gesture as performed by the user. See [`NSEvent.Phase`](nsevent/phase-swift.struct.md) for possible values. When the phase is either [`ended`](nsevent/phase-swift.struct/ended.md), or [`mayBegin`](nsevent/phase-swift.struct/maybegin.md), the user has physically ended the gesture successfully or un-successfully, respectively. Your handler will continue to be called with updated progress values to complete the fluid swipe animation with a phase of [`NSEventPhaseNone`](nseventphase/nseventphasenone.md). - **isComplete**: Signifies the swipe and animation are complete and you should release any temporary animation objects. The `trackingHandler` is released and will not be called further. - **stop**: A reference to a Boolean value. The Block can set the value to [`true`](https://developer.apple.com/documentation/Swift/true) to stop further processing of the array. The `stop` argument is an out-only argument. You should only ever set this Boolean to [`true`](https://developer.apple.com/documentation/Swift/true) within the Block

## See Also

- [class var isSwipeTrackingFromScrollEventsEnabled: Bool](nsevent/isswipetrackingfromscrolleventsenabled.md)
  A Boolean value that indicates whether to track fluid swipe gestures using scroll events.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/trackswipeevent(options:dampenamountthresholdmin:max:usinghandler:))*