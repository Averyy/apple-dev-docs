# animation(forKey:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the animation that should be performed for the specified key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func animation(forKey key: NSAnimatablePropertyKey) -> Any?
```

#### Return Value

The animation to perform. A subclass of [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation).

#### Discussion

When the action specified by `key` is triggered for an object, this method is consulted to find the animation, if any, that should be performed in response.

Like its Core Animation [`CALayer`](https://developer.apple.com/documentation/QuartzCore/CALayer) counterpart, [`action(forKey:)`](https://developer.apple.com/documentation/QuartzCore/CALayer/action(forKey:)), this method is a funnel point that defines the order in which the search for an animation proceeds.It first checks the receiver’s Getting the Animator Proxy dictionary for a value matching `key`, then falls back to  [`animator()`](nsanimatablepropertycontainer/animator().md) for the receiver’s class.

Subclasses should not typically need to override this method.

## Parameters

- `key`: The action name or property specified as a string.

## See Also

- [func animator() -> Self](nsanimatablepropertycontainer/animator.md)
  Returns a proxy object for the receiver that can be used to initiate implied animation for property changes.
- [var animations: [NSAnimatablePropertyKey : Any]](nsanimatablepropertycontainer/animations.md)
  Sets the option dictionary that maps event trigger keys to animation objects.
- [static func defaultAnimation(forKey: NSAnimatablePropertyKey) -> Any?](nsanimatablepropertycontainer/defaultanimation(forkey:).md)
  Returns the default animation that should be performed for the specified key.
- [typealias NSAnimatablePropertyKey](nsanimatablepropertykey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimatablepropertycontainer/animation(forkey:))*