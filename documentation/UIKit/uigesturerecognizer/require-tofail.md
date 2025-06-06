# require(toFail:)

**Framework**: UIKit  
**Kind**: method

Creates a dependency relationship between the gesture recognizer and another gesture recognizer when the objects are created.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func require(toFail otherGestureRecognizer: UIGestureRecognizer)
```

#### Discussion

This method works fine when gesture recognizers aren’t created elsewhere in the app — or in a framework — and the set of gesture recognizers remains the same. If you need to set up failure requirements lazily or in different view hierarchies, use [`gestureRecognizer(_:shouldRequireFailureOf:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md) and [`gestureRecognizer(_:shouldBeRequiredToFailBy:)`](uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:).md) instead. (Note that the [`shouldRequireFailure(of:)`](uigesturerecognizer/shouldrequirefailure(of:).md) and [`shouldBeRequiredToFail(by:)`](uigesturerecognizer/shouldberequiredtofail(by:).md) methods let subclasses define class-wide failure requirements.)

This method creates a relationship with another gesture recognizer that delays the current gesture recognizer’s transition out of [`UIGestureRecognizer.State.possible`](uigesturerecognizer/state-swift.enum/possible.md). The state that the current gesture recognizer transitions to depends on what happens with `otherGestureRecognizer`:

- If `otherGestureRecognizer` transitions to [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md), the current gesture recognizer transitions to its normal next state.
- If `otherGestureRecognizer` transitions to [`recognized`](uigesturerecognizer/state-swift.enum/recognized.md) or [`UIGestureRecognizer.State.began`](uigesturerecognizer/state-swift.enum/began.md), the current gesture recognizer transitions to [`UIGestureRecognizer.State.failed`](uigesturerecognizer/state-swift.enum/failed.md).

An example where this method might be called is when you want a single-tap gesture require that a double-tap gesture fail.

## Parameters

- `otherGestureRecognizer`: Another gesture-recognizer object (an instance of a subclass of  ).

## See Also

- [func shouldBeRequiredToFail(by: UIGestureRecognizer) -> Bool](uigesturerecognizer/shouldberequiredtofail(by:).md)
  Overridden to indicate that the receiver should be required to fail by the specified gesture recognizer.
- [func shouldRequireFailure(of: UIGestureRecognizer) -> Bool](uigesturerecognizer/shouldrequirefailure(of:).md)
  Overridden to indicate that the receiver requires the specified gesture recognizer to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/require(tofail:))*