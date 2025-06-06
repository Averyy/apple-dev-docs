# animationKeys()

**Framework**: Core Animation  
**Kind**: method

Returns an array of strings that identify the animations currently attached to the layer.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func animationKeys() -> [String]?
```

#### Return Value

An array of [`NSString`](https://developer.apple.com/documentation/Foundation/NSString) objects identifying the current animations.

#### Discussion

The order of the array matches the order in which animations will be applied to the layer.

## See Also

- [func add(CAAnimation, forKey: String?)](calayer/add(_:forkey:).md)
  Add the specified animation object to the layer’s render tree.
- [func animation(forKey: String) -> CAAnimation?](calayer/animation(forkey:).md)
  Returns the animation object with the specified identifier.
- [func removeAllAnimations()](calayer/removeallanimations.md)
  Remove all animations attached to the layer.
- [func removeAnimation(forKey: String)](calayer/removeanimation(forkey:).md)
  Remove the animation object with the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/animationkeys())*