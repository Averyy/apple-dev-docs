# value(forAnimatedKey:)

**Framework**: AppKit  
**Kind**: method

Returns the most recently set value for the specified key.

**Availability**:
- macOS 10.11+

## Declaration

```swift
@MainActor
func value(forAnimatedKey key: NSCollectionViewTransitionLayout.AnimatedKey) -> CGFloat
```

#### Return Value

The last value set for the key.

#### Discussion

Use this method to retrieve floating-point values that relate to laying out the contents of your collection view. The key you specify is a string that you define and that has some meaning to your layout’s implementation. At points during an interactive transition, you can assign new values to that key using the [`updateValue(_:forAnimatedKey:)`](nscollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md) method.

## Parameters

- `key`: A key whose value you set previously using the   method.

## See Also

- [var transitionProgress: CGFloat](nscollectionviewtransitionlayout/transitionprogress.md)
  The completion percentage of the transition.
- [func updateValue(CGFloat, forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey)](nscollectionviewtransitionlayout/updatevalue(_:foranimatedkey:).md)
  Sets the value of a key whose value you use during the animation.
- [NSCollectionViewTransitionLayout.AnimatedKey](nscollectionviewtransitionlayout/animatedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/value(foranimatedkey:))*