# gestureRecognizer(_:shouldBeRequiredToFailBy:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if a gesture recognizer should be required to fail by another gesture recognizer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldBeRequiredToFailBy otherGestureRecognizer: UIGestureRecognizer) -> Bool
```

## Mentions

- [Preferring one gesture over another](preferring-one-gesture-over-another.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to set up a dynamic failure requirement between `gestureRecognizer` and `otherGestureRecognizer`. The default implementation returns [`false`](https://developer.apple.com/documentation/Swift/false)—`gestureRecognizer` isn’t required to fail by `otherGestureRecognizer`.

#### Discussion

This method is called once per attempt to recognize, so failure requirements can be determined lazily and may be set up between recognizers across view hierarchies. Note that returning [`true`](https://developer.apple.com/documentation/Swift/true) is guaranteed to set up the failure requirement; returning [`false`](https://developer.apple.com/documentation/Swift/false), on the other hand, isn’t guaranteed to prevent or remove a failure requirement because `otherGestureRecognizer` might make itself a failure requirement by using its own subclass or delegate methods.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class  . This is the object sending the message to the delegate.
- `otherGestureRecognizer`: An instance of a subclass of the abstract base class  .

## See Also

- [func gestureRecognizer(UIGestureRecognizer, shouldRequireFailureOf: UIGestureRecognizer) -> Bool](uigesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:).md)
  Asks the delegate if a gesture recognizer should require another gesture recognizer to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:))*