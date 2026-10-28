# allowClipping

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A key that contains the behavior to use when clipping the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let allowClipping: NSWorkspace.DesktopImageOptionKey
```

```c
extern NSWorkspaceDesktopImageOptionKey const NSWorkspaceDesktopImageAllowClippingKey;
```

## Discussion

The value is an [`NSNumber`](../../../Foundation/nsnumber.md) containing a Boolean, which affects the interpretation of Proportional scaling types. When the value is [`false`](../../../Swift/false.md), the workspace object makes the image fully visible, but it may include empty space on the sides or top and bottom. When the value is [`true`](../../../Swift/true.md), the image fills the entire screen, but may be clipped. If you don’t specify this key, the workspace assumes a value of [`false`](../../../Swift/false.md).  Non-proportional scaling types ignore this value.

## See Also

### Option Keys
- [static let imageScaling: NSWorkspace.DesktopImageOptionKey](./imagescaling.md)
  A key that contains the behavior to use when scaling the image.
- [static let fillColor: NSWorkspace.DesktopImageOptionKey](./fillcolor.md)
  A key that contains the behavior to use when filling the empty space around the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptionkey/allowclipping)*