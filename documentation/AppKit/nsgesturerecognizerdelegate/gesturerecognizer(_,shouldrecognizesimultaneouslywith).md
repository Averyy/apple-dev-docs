# gestureRecognizer(_:shouldRecognizeSimultaneouslyWith:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Asks the delegate if two gesture recognizers should be allowed to recognize their gestures simultaneously.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
optional func gestureRecognizer(_ gestureRecognizer: NSGestureRecognizer, shouldRecognizeSimultaneouslyWith otherGestureRecognizer: NSGestureRecognizer) -> Bool
```

```objc
- (BOOL) gestureRecognizer:(NSGestureRecognizer *) gestureRecognizer shouldRecognizeSimultaneouslyWithGestureRecognizer:(NSGestureRecognizer *) otherGestureRecognizer;
```

## Return Value

[`true`](../../Swift/true.md) to allow `gestureRecognizer` and `otherGestureRecognizer` to recognize their gestures simultaneously. If you do not implement this method, the default return value is [`false`](../../Swift/false.md)—no two gestures can be recognized simultaneously.

## Discussion

This method is called when recognition of a gesture by either `gestureRecognizer` and `otherGestureRecognizer` would block the other gesture recognizer from recognizing its gesture. Returning [`true`](../../Swift/true.md) is guaranteed to allow simultaneous recognition; returning [`false`](../../Swift/false.md) is not guaranteed to prevent simultaneous recognition because the other gesture recognizer’s delegate may return [`true`](../../Swift/true.md).

## Parameters

- `gestureRecognizer`: The first gesture recognizer to be considered. This is the object with which the delegate is associated.
- `otherGestureRecognizer`: The second gesture recognizer to be considered.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsgesturerecognizerdelegate/gesturerecognizer(_:shouldrecognizesimultaneouslywith:))*