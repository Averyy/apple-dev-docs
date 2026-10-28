# transitionProgress

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The completion percentage of the transition.

**Availability**:
- macOS 10.11+

## Declaration

```swift
var transitionProgress: CGFloat { get set }
```

```objc
@property (assign) CGFloat transitionProgress;
```

## Discussion

During the transition, set the value of this property periodically and call the [`invalidateLayout()`](../nscollectionviewlayout/invalidatelayout%28%29.md) method to force the collection view to update item positions. For example, when driving a transition using a gesture recognizer, you can set this property from the handler method of your gesture recognizer.

## See Also

### Updating the Transition Information
- [func updateValue(CGFloat, forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey)](./updatevalue%28_,foranimatedkey%29.md)
  Sets the value of a key whose value you use during the animation.
- [func value(forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey) -> CGFloat](./value%28foranimatedkey%29.md)
  Returns the most recently set value for the specified key.
- [NSCollectionViewTransitionLayout.AnimatedKey](./animatedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/transitionprogress)*