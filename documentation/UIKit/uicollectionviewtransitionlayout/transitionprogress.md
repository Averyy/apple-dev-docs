# transitionProgress

**Framework**: UIKit  
**Kind**: property

The completion percentage of the transition.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var transitionProgress: CGFloat { get set }
```

#### Discussion

During the transition, you should set the value of this property periodically and call [`invalidateLayout()`](uicollectionviewlayout/invalidatelayout().md) to force the collection view to update item positions. If you are driving the transition with a gesture recognizer, you would likely set this property from the handler method of your gesture recognizer.

## See Also

- [func updateValue(CGFloat, forAnimatedKey: String)](uicollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md)
  Sets the value for an animatable key.
- [func value(forAnimatedKey: String) -> CGFloat](uicollectionviewtransitionlayout/value(foranimatedkey:).md)
  Returns the most recently set value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionviewtransitionlayout/transitionprogress)*