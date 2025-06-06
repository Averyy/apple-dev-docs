# touches(for:)

**Framework**: UIKit  
**Kind**: method

Returns the touch objects from the event that belong to the specified given view.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func touches(for view: UIView) -> Set<UITouch>?
```

#### Return Value

A set of [`UITouch`](uitouch.md) objects representing the touches that belong to the specified view.

## Parameters

- `view`: The   object in which the touches originally occurred.

## See Also

- [var allTouches: Set<UITouch>?](uievent/alltouches.md)
  All touches associated with the event.
- [func touches(for: UIWindow) -> Set<UITouch>?](uievent/touches(for:)-767rm.md)
  Returns the touch objects from the event that belong to the specified window.
- [func coalescedTouches(for: UITouch) -> [UITouch]?](uievent/coalescedtouches(for:).md)
  Returns all of the touches associated with the specified main touch.
- [func predictedTouches(for: UITouch) -> [UITouch]?](uievent/predictedtouches(for:).md)
  Returns an array of touches that are predicted to occur for the specified touch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uievent/touches(for:)-9neb4)*