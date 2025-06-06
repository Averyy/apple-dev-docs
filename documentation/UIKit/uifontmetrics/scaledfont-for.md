# scaledFont(for:)

**Framework**: UIKit  
**Kind**: method

Returns a version of the specified font that adopts the current font metrics.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func scaledFont(for font: UIFont) -> UIFont
```

## Mentions

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)

#### Return Value

A version of the specified font with the appropriate style information applied to it, and scaled to the current Dynamic Type setting.

## Parameters

- `font`: The base font to use when applying the style information. Set the size of your font to the standard Dynamic Type size that you use for the corresponding content. Do not specify a font that has already been scaled; doing so results in an exception.

## See Also

- [Scaling Fonts Automatically](scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [func scaledFont(for: UIFont, compatibleWith: UITraitCollection?) -> UIFont](uifontmetrics/scaledfont(for:compatiblewith:).md)
  Returns a version of the specified font that adopts the current font metrics and supports the specified traits.
- [func scaledFont(for: UIFont, maximumPointSize: CGFloat) -> UIFont](uifontmetrics/scaledfont(for:maximumpointsize:).md)
  Returns a version of the specified font that adopts the current font metrics and is constrained to the specified maximum size.
- [func scaledFont(for: UIFont, maximumPointSize: CGFloat, compatibleWith: UITraitCollection?) -> UIFont](uifontmetrics/scaledfont(for:maximumpointsize:compatiblewith:).md)
  Returns a version of the specified font that adopts the current font metrics and is constrained to the specified traits and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/scaledfont(for:))*