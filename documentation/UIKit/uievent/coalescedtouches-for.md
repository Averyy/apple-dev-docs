# coalescedTouches(for:)

**Framework**: UIKit  
**Kind**: method

Returns all of the touches associated with the specified main touch.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func coalescedTouches(for touch: UITouch) -> [UITouch]?
```

#### Return Value

An array of [`UITouch`](uitouch.md) objects representing all of the touches that were reported for the specified touch since the last time the event was delivered. The order of the objects in the array matches the order in which the touches were reported to the system, with the last touch being a copy of the same touch you specified in the  parameter. The return value is `nil` if the object in the  parameter is not associated with the current event.

#### Discussion

Use this method to obtain any additional touches that were received by the system but not delivered in the previous [`UIEvent`](uievent.md) object. Some devices gather touch data at rates up to 240 Hz, which is normally higher than the rate that touches are delivered to your app. While this extra touch data offers greater precision, many apps do not need that precision and do not want to incur the overhead associated with processing them. However, apps that want the increased precision may use this method to retrieve the extra touch objects. For example, drawing apps might use these touches to obtain a more precise record of the user’s drawing input. You can then apply the extra touch data to your app’s content. Use this method if you want coalesced touches or use the set of touches passed to your responder methods, but do not mix the two sets of touches. This method returns the complete sequence of touches that were reported since the last event, including a copy of the touch reported to your responder methods. The event passed to your responder method contains only the last touch in the sequence. Similarly, the [`allTouches`](uievent/alltouches.md) property contains only the last touch in the sequence.

## Parameters

- `touch`: A main touch object that was reported with the event. The touch object you specify determines which sequence of additional touches is returned.

## See Also

- [var allTouches: Set<UITouch>?](uievent/alltouches.md)
  All touches associated with the event.
- [func touches(for: UIView) -> Set<UITouch>?](uievent/touches(for:)-9neb4.md)
  Returns the touch objects from the event that belong to the specified given view.
- [func touches(for: UIWindow) -> Set<UITouch>?](uievent/touches(for:)-767rm.md)
  Returns the touch objects from the event that belong to the specified window.
- [func predictedTouches(for: UITouch) -> [UITouch]?](uievent/predictedtouches(for:).md)
  Returns an array of touches that are predicted to occur for the specified touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/coalescedtouches(for:))*