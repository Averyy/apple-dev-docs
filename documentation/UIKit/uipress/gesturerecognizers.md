# gestureRecognizers

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<UIGestureRecognizer *> * gestureRecognizers;
```

#### Discussion

The objects held in this array are instances of a subclass of the abstract base class, [`UIGestureRecognizer`](../uigesturerecognizer.md). If there are no gesture recognizers currently receiving the touch objects, this property holds an empty array.

## See Also

### Getting a press object’s gesture recognizers
- [var force: CGFloat](./force.md)
  The force of the button press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/gesturerecognizers)*