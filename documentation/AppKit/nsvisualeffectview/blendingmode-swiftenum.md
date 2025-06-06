# NSVisualEffectView.BlendingMode

**Framework**: AppKit  
**Kind**: enum

Constants that specify whether the visual effect view blends with what’s either behind or within the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum BlendingMode
```

## Topics

### Blend Modes
- [NSVisualEffectView.BlendingMode.behindWindow](nsvisualeffectview/blendingmode-swift.enum/behindwindow.md)
  A mode that blends and blurs the visual effect view with the contents behind the window, such as the desktop or other windows.
- [NSVisualEffectView.BlendingMode.withinWindow](nsvisualeffectview/blendingmode-swift.enum/withinwindow.md)
  A mode that blends and blurs the visual effect view with contents behind the view in the current window only.
### Initializers
- [init?(rawValue: Int)](nsvisualeffectview/blendingmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var blendingMode: NSVisualEffectView.BlendingMode](nsvisualeffectview/blendingmode-swift.property.md)
  A value indicating how the view’s contents blend with the surrounding content.
- [var isEmphasized: Bool](nsvisualeffectview/isemphasized.md)
  A Boolean value indicating whether to emphasize the look of the material.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nsvisualeffectview/interiorbackgroundstyle.md)
  The view’s interior background style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum)*