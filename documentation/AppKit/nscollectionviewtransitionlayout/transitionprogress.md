# transitionProgress

**Framework**: AppKit  
**Kind**: property

The completion percentage of the transition.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
var transitionProgress: CGFloat { get set }
```

#### Discussion

During the transition, set the value of this property periodically and call the [`invalidateLayout()`](nscollectionviewlayout/invalidatelayout().md) method to force the collection view to update item positions. For example, when driving a transition using a gesture recognizer, you can set this property from the handler method of your gesture recognizer.

## See Also

- [func updateValue(CGFloat, forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey)](nscollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md)
  Sets the value of a key whose value you use during the animation.
- [func value(forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey) -> CGFloat](nscollectionviewtransitionlayout/value(foranimatedkey:).md)
  Returns the most recently set value for the specified key.
- [NSCollectionViewTransitionLayout.AnimatedKey](nscollectionviewtransitionlayout/animatedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/transitionprogress)*