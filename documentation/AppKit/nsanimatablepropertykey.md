# NSAnimatablePropertyKey

**Framework**: AppKit  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- macOS

## Declaration

```swift
typealias NSAnimatablePropertyKey = String
```

```c
typedef NSString * NSAnimatablePropertyKey;
```

## See Also

### Managing Animations for Properties
- [var animations: [NSAnimatablePropertyKey : Any]](./nsanimatablepropertycontainer/animations.md)
  Sets the option dictionary that maps event trigger keys to animation objects.
- [func animation(forKey: NSAnimatablePropertyKey) -> Any?](./nsanimatablepropertycontainer/animation%28forkey%29.md)
  Returns the animation that should be performed for the specified key.
- [static func defaultAnimation(forKey: NSAnimatablePropertyKey) -> Any?](./nsanimatablepropertycontainer/defaultanimation%28forkey%29.md)
  Returns the default animation that should be performed for the specified key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimatablepropertykey)*