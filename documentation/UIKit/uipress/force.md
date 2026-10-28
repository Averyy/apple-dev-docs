# force

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The force of the button press.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
var force: CGFloat { get }
```

```objc
@property (nonatomic, readonly) CGFloat force;
```

## Discussion

While all buttons can be “down” or “up”, some physical buttons also have a notion of a “force” with which they’re pressed. For analog buttons, force returns a value between 0 and 1, and for digital buttons it returns 0 or 1.

## See Also

### Getting a press object’s gesture recognizers
- [var gestureRecognizers: [UIGestureRecognizer]?](./gesturerecognizers.md)
  The gesture recognizers that are receiving the press.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipress/force)*