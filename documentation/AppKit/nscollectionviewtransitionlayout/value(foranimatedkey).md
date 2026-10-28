# value(forAnimatedKey:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the most recently set value for the specified key.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func value(forAnimatedKey key: NSCollectionViewTransitionLayout.AnimatedKey) -> CGFloat
```

```objc
- (CGFloat) valueForAnimatedKey:(NSCollectionViewTransitionLayoutAnimatedKey) key;
```

## Return Value

The last value set for the key.

## Discussion

Use this method to retrieve floating-point values that relate to laying out the contents of your collection view. The key you specify is a string that you define and that has some meaning to your layout’s implementation. At points during an interactive transition, you can assign new values to that key using the [`updateValue(_:forAnimatedKey:)`](./updatevalue%28_,foranimatedkey%29.md) method.

## Parameters

- `key`: A key whose value you set previously using the [`updateValue(_:forAnimatedKey:)`](./updatevalue%28_,foranimatedkey%29.md) method.

## See Also

### Updating the Transition Information
- [var transitionProgress: CGFloat](./transitionprogress.md)
  The completion percentage of the transition.
- [func updateValue(CGFloat, forAnimatedKey: NSCollectionViewTransitionLayout.AnimatedKey)](./updatevalue%28_,foranimatedkey%29.md)
  Sets the value of a key whose value you use during the animation.
- [NSCollectionViewTransitionLayout.AnimatedKey](./animatedkey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscollectionviewtransitionlayout/value(foranimatedkey:))*