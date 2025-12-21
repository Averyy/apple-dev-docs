# isEmphasized

**Framework**: AppKit  
**Kind**: property

A Boolean value indicating whether to emphasize the look of the material.

**Availability**:
- macOS 10.12+

## Declaration

```swift
@MainActor
var isEmphasized: Bool { get set }
```

#### Discussion

Some materials change their appearance when they are emphasized. For example, the first responder view conveys its status.

The default value of this property is [`false`](https://developer.apple.com/documentation/Swift/false).

## See Also

- [var blendingMode: NSVisualEffectView.BlendingMode](nsvisualeffectview/blendingmode-swift.property.md)
  A value indicating how the view’s contents blend with the surrounding content.
- [NSVisualEffectView.BlendingMode](nsvisualeffectview/blendingmode-swift.enum.md)
  Constants that specify whether the visual effect view blends with what’s either behind or within the window.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nsvisualeffectview/interiorbackgroundstyle.md)
  The view’s interior background style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/isemphasized)*