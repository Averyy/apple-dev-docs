# scaledFont(for:maximumPointSize:compatibleWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a version of the specified font that adopts the current font metrics and is constrained to the specified traits and size.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func scaledFont(for font: UIFont, maximumPointSize: CGFloat, compatibleWith traitCollection: UITraitCollection?) -> UIFont
```

```objc
- (UIFont *) scaledFontForFont:(UIFont *) font maximumPointSize:(CGFloat) maximumPointSize compatibleWithTraitCollection:(UITraitCollection *) traitCollection;
```

## Return Value

A version of the specified font with the appropriate style information applied to it, and scaled appropriately for the specified settings.

## Parameters

- `font`: The base font to use when applying the style information. Set the size of your font to the standard Dynamic Type size that you use for the corresponding content. Do not specify a font that has already been scaled; doing so results in an exception.
- `maximumPointSize`: The maximum point size allowed for the font. Use this value to constrain the font to the specified size when your interface cannot accommodate text that is any larger.
- `traitCollection`: The trait collection to use when determining compatibility. The returned font is appropriate for use in an interface that adopts the specified traits.

## See Also

### Creating Scaled Fonts
- [Scaling fonts automatically](../scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [func scaledFont(for: UIFont) -> UIFont](./scaledfont%28for%29.md)
  Returns a version of the specified font that adopts the current font metrics.
- [func scaledFont(for: UIFont, compatibleWith: UITraitCollection?) -> UIFont](./scaledfont%28for,compatiblewith%29.md)
  Returns a version of the specified font that adopts the current font metrics and supports the specified traits.
- [func scaledFont(for: UIFont, maximumPointSize: CGFloat) -> UIFont](./scaledfont%28for,maximumpointsize%29.md)
  Returns a version of the specified font that adopts the current font metrics and is constrained to the specified maximum size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/scaledfont(for:maximumpointsize:compatiblewith:))*