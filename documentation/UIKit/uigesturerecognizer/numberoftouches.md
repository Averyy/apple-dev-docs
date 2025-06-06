# numberOfTouches

**Framework**: UIKit  
**Kind**: property

The number of touches involved in the gesture represented by the gesture recognizer.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var numberOfTouches: Int { get }
```

#### Return Value

The number of [`UITouch`](uitouch.md) objects in a private array maintained by the receiver. Each of these objects represents a touch in the current gesture.

#### Discussion

Using the value returned by this method in a loop, you can ask for the location of individual touches using the [`location(ofTouch:in:)`](uigesturerecognizer/location(oftouch:in:).md) method.

## See Also

- [func location(in: UIView?) -> CGPoint](uigesturerecognizer/location(in:).md)
  Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.
- [func location(ofTouch: Int, in: UIView?) -> CGPoint](uigesturerecognizer/location(oftouch:in:).md)
  Returns the location of one of the gesture’s touches in the local coordinate system of a given view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/numberoftouches)*