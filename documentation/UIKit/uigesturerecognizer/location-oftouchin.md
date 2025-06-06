# location(ofTouch:in:)

**Framework**: UIKit  
**Kind**: method

Returns the location of one of the gesture’s touches in the local coordinate system of a given view.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func location(ofTouch touchIndex: Int, in view: UIView?) -> CGPoint
```

#### Return Value

A point in the local coordinate system of `view` that identifies the location of the touch. If `nil` is specified for `view`, the method returns the touch location in the window’s base coordinate system.

## Parameters

- `touchIndex`: The index of a   object in a private array maintained by the receiver. This touch object represents a touch of the current gesture.
- `view`: A   object on which the gesture took place. Specify   to indicate the window.

## See Also

- [func location(in: UIView?) -> CGPoint](uigesturerecognizer/location(in:).md)
  Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.
- [var numberOfTouches: Int](uigesturerecognizer/numberoftouches.md)
  The number of touches involved in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/location(oftouch:in:))*