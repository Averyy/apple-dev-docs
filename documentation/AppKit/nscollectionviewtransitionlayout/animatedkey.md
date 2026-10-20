# NSCollectionViewTransitionLayout.AnimatedKey

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias AnimatedKey = String
```

```c
typedef NSString * NSCollectionViewTransitionLayoutAnimatedKey;
```

## See Also

### Updating the Transition Information
- [var transitionProgress: CGFloat](./transitionprogress.md)
  The completion percentage of the transition.
- [func updateValue(CGFloat, forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey)](./updatevalue%28_,foranimatedkey%29.md)
  Sets the value of a key whose value you use during the animation.
- [func value(forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey) -> CGFloat](./value%28foranimatedkey%29.md)
  Returns the most recently set value for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/animatedkey)*