# gestureRecognizers

**Framework**: UIKit  
**Kind**: property

The gesture recognizers that are receiving the press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var gestureRecognizers: [UIGestureRecognizer]? { get }
```

#### Discussion

The objects held in this array are instances of a subclass of the abstract base class, [`UIGestureRecognizer`](uigesturerecognizer.md). If there are no gesture recognizers currently receiving the touch objects, this property holds an empty array.

## See Also

- [var force: CGFloat](uipress/force.md)
  The force of the button press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/gesturerecognizers)*