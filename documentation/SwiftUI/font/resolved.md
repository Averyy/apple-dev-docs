# Font.Resolved

**Framework**: SwiftUI  
**Kind**: struct

A concrete font value.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct Resolved
```

#### Overview

`Font.Resolved` is a concrete representation of a Font that can be shown, with a specific set of `EnvironmentValues`. A `Resolved` font will always map to the same CTFont on a given platform.

> **Note**: `Font`.

## Topics

### Instance Properties
- [var ctFont: CTFont](font/resolved/ctfont.md)
  Returns the CTFont opaque type that represents a CoreText font object.
- [var isBold: Bool](font/resolved/isbold.md)
  Returns `true` if the resolved font has a bold trait according to CoreText or the font’s weight is semi-bold or greater.
- [var isItalic: Bool](font/resolved/isitalic.md)
  Returns `true` if the resolved font is italic.
- [var isLowercaseSmallCaps: Bool](font/resolved/islowercasesmallcaps.md)
  Returns `true` if the resolved font’s lowercased characters use small caps.
- [var isMonospaced: Bool](font/resolved/ismonospaced.md)
  Returns `true` if a resolved font is monospaced, false otherwise.
- [var isSmallCaps: Bool](font/resolved/issmallcaps.md)
  Returns `true` if all of the resolved font’s characters use small caps.
- [var isUppercaseSmallCaps: Bool](font/resolved/isuppercasesmallcaps.md)
  Returns `true` if the resolved font’s uppercased characters use small caps.
- [var leading: Font.Leading](font/resolved/leading.md)
  The leading of a resolved font.
- [var pointSize: CGFloat](font/resolved/pointsize.md)
  The point size of a resolved font.
- [var weight: Font.Weight](font/resolved/weight.md)
  The weight of a resolved font.
- [var width: Font.Width](font/resolved/width.md)
  The width of a resolved font.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/font/resolved)*