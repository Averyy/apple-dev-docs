# animations

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

Sets the option dictionary that maps event trigger keys to animation objects.

**Availability**:
- macOS 10.5+

## Declaration

```swift
var animations: [NSAnimatablePropertyKey : Any] { get set }
```

```objc
@property (copy, readwrite) NSDictionary<NSString *,id> * animations;
```

## Parameters

- `dict`: A dictionary containing the event trigger keys and associated animation objects.

## See Also

### Related Documentation
- [func animator() -> Self](./animator%28%29.md)
  Returns a proxy object for the receiver that can be used to initiate implied animation for property changes.
- [protocol NSAnimatablePropertyContainer](../nsanimatablepropertycontainer.md)
  A set of methods that defines a way to add animation to an existing class with a minimum of API impact.
### Managing Animations for Properties
- [func animation(forKey: NSAnimatablePropertyKey) -> Any?](./animation%28forkey%29.md)
  Returns the animation that should be performed for the specified key.
- [static func defaultAnimation(forKey: NSAnimatablePropertyKey) -> Any?](./defaultanimation%28forkey%29.md)
  Returns the default animation that should be performed for the specified key.
- [typealias NSAnimatablePropertyKey](../nsanimatablepropertykey.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimatablepropertycontainer/animations)*