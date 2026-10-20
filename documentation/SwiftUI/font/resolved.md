# Font.Resolved

**Framework**: SwiftUI  
**Kind**: struct  
**Role**: Structure

A concrete font value.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
struct Resolved
```

#### Overview

`Font.Resolved` is a concrete representation of a Font that can be shown, with a specific set of `EnvironmentValues`. A `Resolved` font will always map to the same CTFont on a given platform.

> **See Also**: [`Font`](../font.md).

## Topics

### Instance Properties
- [var ctFont: CTFont](./resolved/ctfont.md)
  Returns the CTFont opaque type that represents a CoreText font object.
- [var isBold: Bool](./resolved/isbold.md)
  Returns `true` if the resolved font has a bold trait according to CoreText or the font’s weight is semi-bold or greater.
- [var isItalic: Bool](./resolved/isitalic.md)
  Returns `true` if the resolved font is italic.
- [var isLowercaseSmallCaps: Bool](./resolved/islowercasesmallcaps.md)
  Returns `true` if the resolved font’s lowercased characters use small caps.
- [var isMonospaced: Bool](./resolved/ismonospaced.md)
  Returns `true` if a resolved font is monospaced, false otherwise.
- [var isSmallCaps: Bool](./resolved/issmallcaps.md)
  Returns `true` if all of the resolved font’s characters use small caps.
- [var isUppercaseSmallCaps: Bool](./resolved/isuppercasesmallcaps.md)
  Returns `true` if the resolved font’s uppercased characters use small caps.
- [var leading: Font.Leading](./resolved/leading.md)
  The leading of a resolved font.
- [var pointSize: CGFloat](./resolved/pointsize.md)
  The point size of a resolved font.
- [var weight: Font.Weight](./resolved/weight.md)
  The weight of a resolved font.
- [var width: Font.Width](./resolved/width.md)
  The width of a resolved font.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/resolved)*