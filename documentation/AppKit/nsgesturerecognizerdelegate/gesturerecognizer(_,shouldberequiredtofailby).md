# gestureRecognizer(_:shouldBeRequiredToFailBy:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if the current gesture recognizer must fail before another gesture recognizer is allowed to recognize its gesture.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer, shouldBeRequiredToFailBy otherGestureRecognizer: NSGestureRecognizer) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(NSGestureRecognizer *) gestureRecognizer shouldBeRequiredToFailByGestureRecognizer:(NSGestureRecognizer *) otherGestureRecognizer;
```

## Mentions

- [Handling AppKit gestures](../handling-appkit-gestures.md)

## Return Value

[`true`](../../Swift/true.md) if `gestureRecognizer` must fail before `otherGestureRecognizer` is allowed to recognize its gesture. If you do not implement this method, the default return value is [`false`](../../Swift/false.md).

## Discussion

This method is called once per attempt to recognize, so you can change the failure requirements dynamically. The two gesture recognizers do not have to belong to the same view hierarchy.

Returning [`true`](../../Swift/true.md) is guaranteed to set up the failure requirement; returning [`false`](../../Swift/false.md) does not prevent the failure requirement from being set up by the other gesture recognizer.

## Parameters

- `gestureRecognizer`: The gesture recognizer that must fail before `otherGestureRecognizer` can recognize its gesture. This is the object with which the delegate is associated.
- `otherGestureRecognizer`: The gesture recognizer that might need to wait to recognize its gesture.

## See Also

### Setting up failure requirements
- [func gestureRecognizer(NSGestureRecognizer, shouldRequireFailureOf: NSGestureRecognizer) -> Bool](./gesturerecognizer%28_,shouldrequirefailureof%29.md)
  Asks the delegate if the current gesture recognizer must wait to recognize its gesture until the specified gesture recognizer fails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/gesturerecognizer(_:shouldberequiredtofailby:))*