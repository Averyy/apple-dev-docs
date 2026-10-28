# imageScaling

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A key that contains the behavior to use when scaling the image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
static let imageScaling: NSWorkspace.DesktopImageOptionKey
```

```c
extern NSWorkspaceDesktopImageOptionKey const NSWorkspaceDesktopImageScalingKey;
```

## Discussion

The value is an [`NSNumber`](../../../Foundation/nsnumber.md) object that contains an [`NSImageScaling`](../../nsimagescaling.md) constant as declared in [`NSCell`](../../nscell.md). If you don’t include this key, the workspace object uses [`NSImageScaling.scaleProportionallyUpOrDown`](../../nsimagescaling/scaleproportionallyupordown.md). [`NSImageScaling.scaleProportionallyDown`](../../nsimagescaling/scaleproportionallydown.md) isn’t supported.

## See Also

### Option Keys
- [static let allowClipping: NSWorkspace.DesktopImageOptionKey](./allowclipping.md)
  A key that contains the behavior to use when clipping the image.
- [static let fillColor: NSWorkspace.DesktopImageOptionKey](./fillcolor.md)
  A key that contains the behavior to use when filling the empty space around the image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsworkspace/desktopimageoptionkey/imagescaling)*