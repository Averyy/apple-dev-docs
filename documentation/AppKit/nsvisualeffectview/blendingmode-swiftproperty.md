# blendingMode

**Framework**: AppKit  
**Kind**: property

A value indicating how the view’s contents blend with the surrounding content.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var blendingMode: NSVisualEffectView.BlendingMode { get set }
```

#### Discussion

When the value of this property is [`NSVisualEffectView.BlendingMode.behindWindow`](nsvisualeffectview/blendingmode-swift.enum/behindwindow.md) (the default), the visual effect view blurs the content behind the window. When the value is [`NSVisualEffectView.BlendingMode.withinWindow`](nsvisualeffectview/blendingmode-swift.enum/withinwindow.md), it blurs the content behind the view of the current window.

If the visual effect view’s material is [`NSVisualEffectView.Material.titlebar`](nsvisualeffectview/material-swift.enum/titlebar.md), set the blending mode to [`NSVisualEffectView.BlendingMode.withinWindow`](nsvisualeffectview/blendingmode-swift.enum/withinwindow.md).

## See Also

- [NSVisualEffectView.BlendingMode](nsvisualeffectview/blendingmode-swift.enum.md)
  Constants that specify whether the visual effect view blends with what’s either behind or within the window.
- [var isEmphasized: Bool](nsvisualeffectview/isemphasized.md)
  A Boolean value indicating whether to emphasize the look of the material.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nsvisualeffectview/interiorbackgroundstyle.md)
  The view’s interior background style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.property)*