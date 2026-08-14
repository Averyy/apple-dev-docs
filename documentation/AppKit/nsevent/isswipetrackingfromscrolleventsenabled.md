# isSwipeTrackingFromScrollEventsEnabled

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether to track fluid swipe gestures using scroll events.

**Availability**:
- macOS 10.7+

## Declaration

```swift
class var isSwipeTrackingFromScrollEventsEnabled: Bool { get }
```

#### Discussion

If your app implements its own scrolling, or one of your responder objects tracks scroll wheel messages before they reach a scroll view, make sure the value of this property is [`true`](https://developer.apple.com/documentation/swift/true) before you call [`trackSwipeEvent(options:dampenAmountThresholdMin:max:usingHandler:)`](nsevent/trackswipeevent(options:dampenamountthresholdmin:max:usinghandler:).md) to handle the event. The system defines the value of this property based on user-level preferences.

If you use [`NSScrollView`](nsscrollview.md) for your app’s scrolling behavior, you don’t need to check this property. Scroll views automatically account for this behavior.

## See Also

- [func trackSwipeEvent(options: NSEvent.SwipeTrackingOptions, dampenAmountThresholdMin: CGFloat, max: CGFloat, usingHandler: (CGFloat, NSEvent.Phase, Bool, UnsafeMutablePointer<ObjCBool>) -> Void)](nsevent/trackswipeevent(options:dampenamountthresholdmin:max:usinghandler:).md)
  Allows tracking and user interface feedback of scroll wheel events.
- [NSEvent.SwipeTrackingOptions](nsevent/swipetrackingoptions.md)
  Constants that specify swipe-tracking options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsevent/isswipetrackingfromscrolleventsenabled)*