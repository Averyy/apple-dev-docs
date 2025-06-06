# allowClipping

**Framework**: AppKit  
**Kind**: property

A key that contains the behavior to use when clipping the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let allowClipping: NSWorkspace.DesktopImageOptionKey
```

#### Discussion

The value is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) containing a Boolean, which affects the interpretation of Proportional scaling types. When the value is [`false`](https://developer.apple.com/documentation/swift/false), the workspace object makes the image fully visible, but it may include empty space on the sides or top and bottom. When the value is [`true`](https://developer.apple.com/documentation/swift/true), the image fills the entire screen, but may be clipped. If you don’t specify this key, the workspace assumes a value of [`false`](https://developer.apple.com/documentation/swift/false).  Non-proportional scaling types ignore this value.

## See Also

- [static let imageScaling: NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey/imagescaling.md)
  A key that contains the behavior to use when scaling the image.
- [static let fillColor: NSWorkspace.DesktopImageOptionKey](nsworkspace/desktopimageoptionkey/fillcolor.md)
  A key that contains the behavior to use when filling the empty space around the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptionkey/allowclipping)*