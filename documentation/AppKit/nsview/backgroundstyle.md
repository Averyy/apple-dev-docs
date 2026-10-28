# NSView.BackgroundStyle

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

Background styles to apply to a view’s cell.

**Availability**:
- macOS 10.5+

## Declaration

```swift
enum BackgroundStyle
```

```c
enum NSBackgroundStyle : NSInteger;
```

## Overview

Apply these styles to the [`backgroundStyle`](../nscell/backgroundstyle.md) or [`interiorBackgroundStyle`](../nscell/interiorbackgroundstyle.md) properties of an [`NSCell`](../nscell.md) object.

## Topics

### Getting the Background Styles
- [NSView.BackgroundStyle.normal](./backgroundstyle/normal.md)
  A style that reflects the predominant color scheme of the view’s appearance.
- [NSView.BackgroundStyle.emphasized](./backgroundstyle/emphasized.md)
  A style that adds emphasis to the background using an alternate color or visual effect.
- [NSView.BackgroundStyle.raised](./backgroundstyle/raised.md)
  A style that makes the background appear higher than the content drawn on it.
- [NSView.BackgroundStyle.lowered](./backgroundstyle/lowered.md)
  A style that makes the background appear lower than the content drawn on it.
- [static var light: NSView.BackgroundStyle](./backgroundstyle/light.md)
  The background is a light color.
- [static var dark: NSView.BackgroundStyle](./backgroundstyle/dark.md)
  The background is a dark color.
### Initializers
- [init?(rawValue: Int)](./backgroundstyle/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing Display Attributes
- [var isBezeled: Bool](../nscell/isbezeled.md)
  A Boolean value indicating whether the cell has a bezeled border.
- [var isBordered: Bool](../nscell/isbordered.md)
  A Boolean value indicating whether the cell draws itself outlined with a plain border.
- [var isOpaque: Bool](../nscell/isopaque.md)
  A Boolean value indicating whether the cell is completely opaque.
- [var backgroundStyle: NSView.BackgroundStyle](../nscell/backgroundstyle.md)
  The cell’s background style.
- [var interiorBackgroundStyle: NSView.BackgroundStyle](../nscell/interiorbackgroundstyle.md)
  The cell’s interior background style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsview/backgroundstyle)*