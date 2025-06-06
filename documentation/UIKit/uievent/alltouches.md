# allTouches

**Framework**: UIKit  
**Kind**: property

All touches associated with the event.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var allTouches: Set<UITouch>? { get }
```

#### Return Value

A set of [`UITouch`](uitouch.md) objects representing all touches associated with the event.

#### Discussion

If the touches of the event originate in different views and windows, the [`UITouch`](uitouch.md) objects obtained from this method will be associated with different responder objects.

## See Also

- [func touches(for: UIView) -> Set<UITouch>?](uievent/touches(for:)-9neb4.md)
  Returns the touch objects from the event that belong to the specified given view.
- [func touches(for: UIWindow) -> Set<UITouch>?](uievent/touches(for:)-767rm.md)
  Returns the touch objects from the event that belong to the specified window.
- [func coalescedTouches(for: UITouch) -> [UITouch]?](uievent/coalescedtouches(for:).md)
  Returns all of the touches associated with the specified main touch.
- [func predictedTouches(for: UITouch) -> [UITouch]?](uievent/predictedtouches(for:).md)
  Returns an array of touches that are predicted to occur for the specified touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/alltouches)*