# isVertical

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether the status bar has a vertical orientation.

**Availability**:
- macOS ?+

## Declaration

```swift
var isVertical: Bool { get }
```

#### Discussion

When the value of this property is [`true`](https://developer.apple.com/documentation/Swift/true), the status bar has a vertical orientation. The status bar returned by the [`system`](nsstatusbar/system.md) method is horizontal and has the value [`false`](https://developer.apple.com/documentation/Swift/false) for this property.

## See Also

- [var thickness: CGFloat](nsstatusbar/thickness.md)
  The thickness of the status bar, in pixels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsstatusbar/isvertical)*