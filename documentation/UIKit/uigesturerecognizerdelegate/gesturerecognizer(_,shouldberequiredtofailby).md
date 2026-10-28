# gestureRecognizer(_:shouldBeRequiredToFailBy:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if a gesture recognizer should be required to fail by another gesture recognizer.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldBeRequiredToFailBy otherGestureRecognizer: UIGestureRecognizer) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(UIGestureRecognizer *) gestureRecognizer shouldBeRequiredToFailByGestureRecognizer:(UIGestureRecognizer *) otherGestureRecognizer;
```

## Mentions

- [Preferring one gesture over another](../preferring-one-gesture-over-another.md)

## Return Value

[`true`](../../Swift/true.md) to set up a dynamic failure requirement between `gestureRecognizer` and `otherGestureRecognizer`. The default implementation returns [`false`](../../Swift/false.md)—`gestureRecognizer` isn’t required to fail by `otherGestureRecognizer`.

## Discussion

This method is called once per attempt to recognize, so failure requirements can be determined lazily and may be set up between recognizers across view hierarchies. Note that returning [`true`](../../Swift/true.md) is guaranteed to set up the failure requirement; returning [`false`](../../Swift/false.md), on the other hand, isn’t guaranteed to prevent or remove a failure requirement because `otherGestureRecognizer` might make itself a failure requirement by using its own subclass or delegate methods.

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md). This is the object sending the message to the delegate.
- `otherGestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md).

## See Also

### Setting up failure requirements
- [func gestureRecognizer(UIGestureRecognizer, shouldRequireFailureOf: UIGestureRecognizer) -> Bool](./gesturerecognizer%28_,shouldrequirefailureof%29.md)
  Asks the delegate if a gesture recognizer should require another gesture recognizer to fail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:))*