# gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if two gesture recognizers should be allowed to recognize gestures simultaneously.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(UIGestureRecognizer *) gestureRecognizer shouldRecognizeSimultaneouslyWithGestureRecognizer:(UIGestureRecognizer *) otherGestureRecognizer;
```

## Mentions

- [Allowing the simultaneous recognition of multiple gestures](../allowing-the-simultaneous-recognition-of-multiple-gestures.md)

#### Return Value

[`true`](../../Swift/true.md) to allow both `gestureRecognizer` and `otherGestureRecognizer` to recognize their gestures simultaneously. The default implementation returns [`false`](../../Swift/false.md)—no two gestures can be recognized simultaneously.

#### Discussion

This method is called when recognition of a gesture by either `gestureRecognizer` or `otherGestureRecognizer` would block the other gesture recognizer from recognizing its gesture. Note that returning [`true`](../../Swift/true.md) is guaranteed to allow simultaneous recognition; returning [`false`](../../Swift/false.md), on the other hand, is not guaranteed to prevent simultaneous recognition because the other gesture recognizer’s delegate may return [`true`](../../Swift/true.md).

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md). This is the object sending the message to the delegate.
- `otherGestureRecognizer`: An instance of a subclass of the abstract base class [`UIGestureRecognizer`](../uigesturerecognizer.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:))*