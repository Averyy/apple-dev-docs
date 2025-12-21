# gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)

**Framework**: UIKit  
**Kind**: method

Asks the delegate if two gesture recognizers should be allowed to recognize gestures simultaneously.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: UIGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: UIGestureRecognizer) -> Bool
```

## Mentions

- [Allowing the simultaneous recognition of multiple gestures](allowing-the-simultaneous-recognition-of-multiple-gestures.md)

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) to allow both `gestureRecognizer` and `otherGestureRecognizer` to recognize their gestures simultaneously. The default implementation returns [`false`](https://developer.apple.com/documentation/Swift/false)—no two gestures can be recognized simultaneously.

#### Discussion

This method is called when recognition of a gesture by either `gestureRecognizer` or `otherGestureRecognizer` would block the other gesture recognizer from recognizing its gesture. Note that returning [`true`](https://developer.apple.com/documentation/Swift/true) is guaranteed to allow simultaneous recognition; returning [`false`](https://developer.apple.com/documentation/Swift/false), on the other hand, is not guaranteed to prevent simultaneous recognition because the other gesture recognizer’s delegate may return [`true`](https://developer.apple.com/documentation/Swift/true).

## Parameters

- `gestureRecognizer`: An instance of a subclass of the abstract base class  . This is the object sending the message to the delegate.
- `otherGestureRecognizer`: An instance of a subclass of the abstract base class  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:))*