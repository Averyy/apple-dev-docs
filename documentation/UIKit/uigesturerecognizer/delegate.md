# delegate

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The delegate of the gesture recognizer.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
weak var delegate: (any UIGestureRecognizerDelegate)? { get set }
```

```objc
@property (nonatomic, weak, nullable) id<UIGestureRecognizerDelegate> delegate;
```

## Discussion

The gesture recognizer maintains a weak reference to its delegate. The delegate must adopt the [`UIGestureRecognizerDelegate`](../uigesturerecognizerdelegate.md) protocol and implement one or more of its methods.

## See Also

### Managing gesture-related interactions
- [protocol UIGestureRecognizerDelegate](../uigesturerecognizerdelegate.md)
  A set of methods implemented by the delegate of a gesture recognizer to fine-tune an app’s gesture-recognition behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uigesturerecognizer/delegate)*