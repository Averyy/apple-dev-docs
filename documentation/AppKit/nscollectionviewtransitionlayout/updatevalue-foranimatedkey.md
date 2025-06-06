# updateValue(_:forAnimatedKey:)

**Framework**: AppKit  
**Kind**: method

Sets the value of a key whose value you use during the animation.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func updateValue(_ value: CGFloat, forAnimatedKey key: NSCollectionViewTransitionLayout.AnimatedKey)
```

#### Discussion

Use this method to update the value of a specific key that you use in your custom transition layout.

## Parameters

- `value`: The value of the key.
- `key`: The key that you define for your custom transition layout.

## See Also

- [var transitionProgress: CGFloat](nscollectionviewtransitionlayout/transitionprogress.md)
  The completion percentage of the transition.
- [func value(forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey) -> CGFloat](nscollectionviewtransitionlayout/value(foranimatedkey:).md)
  Returns the most recently set value for the specified key.
- [NSCollectionViewTransitionLayout.AnimatedKey](nscollectionviewtransitionlayout/animatedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/updatevalue(_:foranimatedkey:))*