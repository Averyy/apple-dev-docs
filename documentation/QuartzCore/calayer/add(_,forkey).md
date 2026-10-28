# add(_:forKey:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Add the specified animation object to the layer’s render tree.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func add(_ anim: CAAnimation, forKey key: String?)
```

```objc
- (void) addAnimation:(CAAnimation *) anim forKey:(NSString *) key;
```

## Discussion

If the `duration` property of the animation is zero or negative, the duration is changed to the current value of the [`kCATransactionAnimationDuration`](../kcatransactionanimationduration.md) transaction property (if set) or to the default value of `0.25` seconds.

## Parameters

- `anim`: The animation to be added to the render tree. This object is copied by the render tree, not referenced. Therefore, subsequent modifications to the object are not propagated into the render tree.
- `key`: A string that identifies the animation. Only one animation per unique key is added to the layer. The special key [`kCATransition`](../kcatransition.md) is automatically used for transition animations. You may specify `nil` for this parameter.

## See Also

### Layer animations
- [func animation(forKey: String) -> CAAnimation?](./animation%28forkey%29.md)
  Returns the animation object with the specified identifier.
- [func removeAllAnimations()](./removeallanimations%28%29.md)
  Remove all animations attached to the layer.
- [func removeAnimation(forKey: String)](./removeanimation%28forkey%29.md)
  Remove the animation object with the specified key.
- [func animationKeys() -> [String]?](./animationkeys%28%29.md)
  Returns an array of strings that identify the animations currently attached to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/add(_:forkey:))*