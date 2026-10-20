# scaledFont(for:compatibleWith:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a version of the specified font that adopts the current font metrics and supports the specified traits.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
func scaledFont(for font: UIFont, compatibleWith traitCollection: UITraitCollection?) -> UIFont
```

```objc
- (UIFont *) scaledFontForFont:(UIFont *) font compatibleWithTraitCollection:(UITraitCollection *) traitCollection;
```

#### Return Value

A version of the specified font with the appropriate style information applied to it, and scaled to the current Dynamic Type setting.

## Parameters

- `font`: The base font to use when applying the style information. Set the size of your font to the standard Dynamic Type size that you use for the corresponding content. Do not specify a font that has already been scaled; doing so results in an exception.
- `traitCollection`: The trait collection to use when determining compatibility. The returned font is appropriate for use in an interface that adopts the specified traits.

## See Also

### Creating Scaled Fonts
- [Scaling fonts automatically](../scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [func scaledFont(for: UIFont) -> UIFont](./scaledfont%28for%29.md)
  Returns a version of the specified font that adopts the current font metrics.
- [func scaledFont(for: UIFont, maximumPointSize: CGFloat) -> UIFont](./scaledfont%28for,maximumpointsize%29.md)
  Returns a version of the specified font that adopts the current font metrics and is constrained to the specified maximum size.
- [func scaledFont(for: UIFont, maximumPointSize: CGFloat, compatibleWith: UITraitCollection?) -> UIFont](./scaledfont%28for,maximumpointsize,compatiblewith%29.md)
  Returns a version of the specified font that adopts the current font metrics and is constrained to the specified traits and size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontmetrics/scaledfont(for:compatiblewith:))*