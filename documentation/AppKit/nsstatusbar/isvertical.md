# isVertical

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the status bar has a vertical orientation.

**Availability**:
- macOS

## Declaration

```swift
var isVertical: Bool { get }
```

```objc
@property (readonly, getter=isVertical) BOOL vertical;
```

## Discussion

When the value of this property is [`true`](../../Swift/true.md), the status bar has a vertical orientation. The status bar returned by the [`system`](./system.md) method is horizontal and has the value [`false`](../../Swift/false.md) for this property.

## See Also

### Getting Status-Bar Attributes
- [var thickness: CGFloat](./thickness.md)
  The thickness of the status bar, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusbar/isvertical)*