# animation(forKey:)

**Framework**: Core Animation  
**Kind**: method

Returns the animation object with the specified identifier.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func animation(forKey key: String) -> CAAnimation?
```

#### Return Value

The animation object matching the identifier, or `nil` if no such animation exists.

#### Discussion

Use this method to retrieve only animation objects already associated with a layer. Modifying any properties of the returned object results in undefined behavior.

## Parameters

- `key`: A string that specifies the identifier of the animation. This string corresponds to the identifier string you passed to the   method.

## See Also

- [func add(CAAnimation, forKey: String?)](calayer/add(_:forkey:).md)
  Add the specified animation object to the layer’s render tree.
- [func removeAllAnimations()](calayer/removeallanimations.md)
  Remove all animations attached to the layer.
- [func removeAnimation(forKey: String)](calayer/removeanimation(forkey:).md)
  Remove the animation object with the specified key.
- [func animationKeys() -> [String]?](calayer/animationkeys.md)
  Returns an array of strings that identify the animations currently attached to the layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/calayer/animation(forkey:))*