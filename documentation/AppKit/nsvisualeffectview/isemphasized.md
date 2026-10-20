# isEmphasized

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether to emphasize the look of the material.

**Availability**:
- macOS 10.12+

## Declaration

```swift
var isEmphasized: Bool { get set }
```

```objc
@property (getter=isEmphasized) BOOL emphasized;
```

#### Discussion

Some materials change their appearance when they are emphasized. For example, the first responder view conveys its status.

The default value of this property is [`false`](../../Swift/false.md).

## See Also

### Specifying the Effect Appearance
- [var blendingMode: NSVisualEffectView.BlendingMode](./blendingmode-swift.property.md)
  A value indicating how the view’s contents blend with the surrounding content.
- [NSVisualEffectView.BlendingMode](./blendingmode-swift.enum.md)
  Constants that specify whether the visual effect view blends with what’s either behind or within the window.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](./interiorbackgroundstyle.md)
  The view’s interior background style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsvisualeffectview/isemphasized)*