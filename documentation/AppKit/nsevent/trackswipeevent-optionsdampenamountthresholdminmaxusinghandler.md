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

 This method returns immediately and tracking is performed asynchronously.

## Parameters

- `options`: The swipe tracking events. See   for possible values.
- `minDampenThreshold`: The minimum dampen threshold. This value is considered to encompass the “current view content area” and is referred to as a page. This is the number of pages with a negative position relative to the current page. The value must be less than or equal to zero.
- `maxDampenThreshold`: The maximum dampen threshold. This value is considered to encompass the “current view content area” and is referred to as a page. This is the number of pages with a positive position relative to the current page. The value must be greater than or equal to zero.
- `trackingHandler`: The   is released and will not be called further.

## See Also

- [class var isSwipeTrackingFromScrollEventsEnabled: Bool](nsevent/isswipetrackingfromscrolleventsenabled.md)
  A Boolean value that indicates whether to track fluid swipe gestures using scroll events.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/trackswipeevent(options:dampenamountthresholdmin:max:usinghandler:))*