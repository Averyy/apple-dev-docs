# animation(forKey:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Returns the animation that should be performed for the specified key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
func animation(forKey key: NSAnimatablePropertyKey) -> Any?
```

```objc
- (id) animationForKey:(NSAnimatablePropertyKey) key;
```

## Return Value

The animation to perform. A subclass of [`CAAnimation`](../../QuartzCore/caanimation.md).

## Discussion

When the action specified by `key` is triggered for an object, this method is consulted to find the animation, if any, that should be performed in response.

Like its Core Animation [`CALayer`](../../QuartzCore/calayer.md) counterpart, [`action(forKey:)`](../../QuartzCore/calayer/action%28forkey%29.md), this method is a funnel point that defines the order in which the search for an animation proceeds.It first checks the receiver’s Getting the Animator Proxy dictionary for a value matching `key`, then falls back to  [`animator()`](./animator%28%29.md) for the receiver’s class.

Subclasses should not typically need to override this method.

## Parameters

- `key`: The action name or property specified as a string.

## See Also

### Related Documentation
- [func animator() -> Self](./animator%28%29.md)
  Returns a proxy object for the receiver that can be used to initiate implied animation for property changes.
### Managing Animations for Properties
- [var animations: [NSAnimatablePropertyKey : Any]](./animations.md)
  Sets the option dictionary that maps event trigger keys to animation objects.
- [static func defaultAnimation(forKey: NSAnimatablePropertyKey) -> Any?](./defaultanimation%28forkey%29.md)
  Returns the default animation that should be performed for the specified key.
- [typealias NSAnimatablePropertyKey](../nsanimatablepropertykey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimatablepropertycontainer/animation(forkey:))*