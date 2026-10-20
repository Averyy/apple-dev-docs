# allowsImplicitAnimation

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

Determine if animations are enabled or not for animations that occur as a result of another property change.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var allowsImplicitAnimation: Bool { get set }
```

```objc
@property BOOL allowsImplicitAnimation;
```

#### Discussion

Using the [`animator()`](../nsanimatablepropertycontainer/animator%28%29.md) proxy will automatically set `allowsImplicitAnimation` to [`true`](../../Swift/true.md). When [`true`](../../Swift/true.md), other properties can implicitly animate along with the initially changed property.

For instance, calling `[[view animator] setFrame:frame]` will allow subviews to also animate their frame positions. When the value is [`false`](../../Swift/false.md) the behavior is diabled.

The default value is [`false`](../../Swift/false.md).

This is only applicable when layer backed on OS v10.8 and later.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsanimationcontext/allowsimplicitanimation)*