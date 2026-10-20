# NSVisualEffectView.BlendingMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Constants that specify whether the visual effect view blends with what’s either behind or within the window.

**Availability**:
- macOS 10.10+

## Declaration

```swift
enum BlendingMode
```

```c
enum NSVisualEffectBlendingMode : NSInteger;
```

## Topics

### Blend Modes
- [NSVisualEffectView.BlendingMode.behindWindow](./blendingmode-swift.enum/behindwindow.md)
  A mode that blends and blurs the visual effect view with the contents behind the window, such as the desktop or other windows.
- [NSVisualEffectView.BlendingMode.withinWindow](./blendingmode-swift.enum/withinwindow.md)
  A mode that blends and blurs the visual effect view with contents behind the view in the current window only.
### Initializers
- [init?(rawValue: Int)](./blendingmode-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Specifying the Effect Appearance
- [var blendingMode: NSVisualEffectView.BlendingMode](./blendingmode-swift.property.md)
  A value indicating how the view’s contents blend with the surrounding content.
- [var isEmphasized: Bool](./isemphasized.md)
  A Boolean value indicating whether to emphasize the look of the material.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](./interiorbackgroundstyle.md)
  The view’s interior background style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/blendingmode-swift.enum)*