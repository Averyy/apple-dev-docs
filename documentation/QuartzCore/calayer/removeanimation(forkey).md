# removeAnimation(forKey:)

**Framework**: Core Animation  
**Kind**: method  
**Role**: Instance Method

Remove the animation object with the specified key.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func removeAnimation(forKey key: String)
```

```objc
- (void) removeAnimationForKey:(NSString *) key;
```

## Parameters

- `key`: The identifier of the animation to remove.

## See Also

### Layer animations
- [func add(CAAnimation, forKey: String?)](./add%28_,forkey%29.md)
  Add the specified animation object to the layer’s render tree.
- [func animation(forKey: String) -> CAAnimation?](./animation%28forkey%29.md)
  Returns the animation object with the specified identifier.
- [func removeAllAnimations()](./removeallanimations%28%29.md)
  Remove all animations attached to the layer.
- [func animationKeys() -> [String]?](./animationkeys%28%29.md)
  Returns an array of strings that identify the animations currently attached to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/removeanimation(forkey:))*