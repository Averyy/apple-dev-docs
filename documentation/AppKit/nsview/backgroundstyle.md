# NSView.BackgroundStyle

**Framework**: AppKit  
**Kind**: enum

Background styles to apply to a view’s cell.

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum BackgroundStyle
```

#### Overview

Apply these styles to the [`backgroundStyle`](nscell/backgroundstyle.md) or [`interiorBackgroundStyle`](nscell/interiorbackgroundstyle.md) properties of an [`NSCell`](nscell.md) object.

## Topics

### Getting the Background Styles
- [NSView.BackgroundStyle.normal](nsview/backgroundstyle/normal.md)
  A style that reflects the predominant color scheme of the view’s appearance.
- [NSView.BackgroundStyle.emphasized](nsview/backgroundstyle/emphasized.md)
  A style that adds emphasis to the background using an alternate color or visual effect.
- [NSView.BackgroundStyle.raised](nsview/backgroundstyle/raised.md)
  A style that makes the background appear higher than the content drawn on it.
- [NSView.BackgroundStyle.lowered](nsview/backgroundstyle/lowered.md)
  A style that makes the background appear lower than the content drawn on it.
### Deprecated
- [static let light: NSView.BackgroundStyle](nsview/backgroundstyle/light.md)
  The background is a light color.
- [static let dark: NSView.BackgroundStyle](nsview/backgroundstyle/dark.md)
  The background is a dark color.
### Initializers
- [init?(rawValue: Int)](nsview/backgroundstyle/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var isBezeled: Bool](nscell/isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](nscell/isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var controlTint: NSControlTint](nscell/controltint.md)
  The cell’s control tint.
- [var backgroundStyle: NSView.BackgroundStyle](nscell/backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](nscell/interiorbackgroundstyle.md)
  The cell’s interior background style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/backgroundstyle)*