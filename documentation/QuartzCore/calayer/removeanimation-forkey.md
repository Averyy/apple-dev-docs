# removeAnimation(forKey:)

**Framework**: Core Animation  
**Kind**: method

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

## Parameters

- `key`: The identifier of the animation to remove.

## See Also

- [func add(CAAnimation, forKey: String?)](calayer/add(_:forkey:).md)
  Add the specified animation object to the layer’s render tree.
- [func animation(forKey: String) -> CAAnimation?](calayer/animation(forkey:).md)
  Returns the animation object with the specified identifier.
- [func removeAllAnimations()](calayer/removeallanimations.md)
  Remove all animations attached to the layer.
- [func animationKeys() -> [String]?](calayer/animationkeys.md)
  Returns an array of strings that identify the animations currently attached to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/removeanimation(forkey:))*