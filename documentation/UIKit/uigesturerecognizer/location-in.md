# location(in:)

**Framework**: UIKit  
**Kind**: method

Returns the point computed as the location in a given view of the gesture represented by the gesture recognizer.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func location(in view: UIView?) -> CGPoint
```

#### Return Value

A point in the local coordinate system of `view` that identifies the location of the gesture. If `nil` is specified for `view`, the method returns the gesture location in the window’s base coordinate system.

#### Discussion

The returned value is a generic single-point location for the gesture computed by the UIKit framework. It is usually the centroid of the touches involved in the gesture. For objects of the [`UISwipeGestureRecognizer`](uiswipegesturerecognizer.md) and [`UITapGestureRecognizer`](uitapgesturerecognizer.md) classes, the location returned by this method has a significance special to the gesture. This significance is documented in the reference for those classes.

## Parameters

- `view`: A   object on which the gesture took place. Specify   to indicate the window.

## See Also

- [func location(ofTouch: Int, in: UIView?) -> CGPoint](uigesturerecognizer/location(oftouch:in:).md)
  Returns the location of one of the gesture’s touches in the local coordinate system of a given view.
- [var numberOfTouches: Int](uigesturerecognizer/numberoftouches.md)
  The number of touches involved in the gesture represented by the gesture recognizer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/location(in:))*