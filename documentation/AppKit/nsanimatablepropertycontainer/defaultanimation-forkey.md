# defaultAnimation(forKey:)

**Framework**: AppKit  
**Kind**: method  
**Required**: Yes

Returns the default animation that should be performed for the specified key.

**Availability**:
- macOS 10.5+

## Declaration

```swift
static func defaultAnimation(forKey key: NSAnimatablePropertyKey) -> Any?
```

#### Return Value

The animation to perform. A subclass of [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation).

#### Discussion

The [`NSAnimatablePropertyContainer`](nsanimatablepropertycontainer.md) method consults this class method when its search of the receivers Getting the Animator Proxy dictionary fails to return an animation for `key`.

An animatable property container should implement this method to return a default animation to be performed for each key that it wants to make auto-animatable, where `key` usually references a property of the receiver, but can also specify a special animation trigger ([`NSAnimationTriggerOrderIn`](nsanimationtriggerorderin.md) or [`NSAnimationTriggerOrderOut`](nsanimationtriggerorderout.md)).

A developer implementing a custom view subclass, can enable automatic animation for properties by overriding this method, and having it return the desired default [`CAAnimation`](https://developer.apple.com/documentation/QuartzCore/CAAnimation) subclass to use for each of the property keys of interest. The override should defer to super for any keys it doesn’t specifically handle, facilitating inheritance of default animation specifications. The following is an example of such an implementation.

```objc
 
@implementation MyView
+ (id)defaultAnimationForKey:(NSString *)key {
    if ([key isEqualToString:@"borderColor"]) {
        // By default, animate border color changes with simple linear interpolation to the new color value.
        return [CABasicAnimation animation];
    } else {
        // Defer to super's implementation for any keys we don't specifically handle.
        return [super defaultAnimationForKey:key];
    }
}
@end
```

## Parameters

- `key`: The action name or property specified as a string.

## See Also

- [var animations: [NSAnimatablePropertyKey : Any]](nsanimatablepropertycontainer/animations.md)
  Sets the option dictionary that maps event trigger keys to animation objects.
- [func animation(forKey: NSAnimatablePropertyKey) -> Any?](nsanimatablepropertycontainer/animation(forkey:).md)
  Returns the animation that should be performed for the specified key.
- [typealias NSAnimatablePropertyKey](nsanimatablepropertykey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimatablepropertycontainer/defaultanimation(forkey:))*