# gestureRecognizer(_:shouldRequireFailureOf:)

**Framework**: AppKit  
**Kind**: method

Asks the delegate if the current gesture recognizer must wait to recognize its gesture until the specified gesture recognizer fails.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer, shouldRequireFailureOf otherGestureRecognizer: NSGestureRecognizer) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `otherGestureRecognizer` must fail before `gestureRecognizer` is allowed to recognize its gesture. If you do not implement this method, the default return value is [`false`](https://developer.apple.com/documentation/swift/false).

#### Discussion

This method is called once per attempt to recognize, so you can change the failure requirements dynamically. The two gesture recognizers do not have to belong to the same view hierarchy.

Returning [`true`](https://developer.apple.com/documentation/swift/true) is guaranteed to set up the failure requirement; returning [`false`](https://developer.apple.com/documentation/swift/false) does not prevent the failure requirement from being set up by the other gesture recognizer.

## Parameters

- `gestureRecognizer`: The gesture recognizer that might need to wait to recognize its gesture. This is the object with which the delegate is associated.
- `otherGestureRecognizer`: The gesture recognizer that must fail before the object in   can recognize its gesture.

## See Also

- [func gestureRecognizer(NSGestureRecognizer, shouldBeRequiredToFailBy: NSGestureRecognizer) -> Bool](nsgesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:).md)
  Asks the delegate if the current gesture recognizer must fail before another gesture recognizer is allowed to recognize its gesture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/gesturerecognizer(_:shouldrequirefailureof:))*