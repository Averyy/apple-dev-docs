# monospacedSystemFont(ofSize:weight:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns the fixed-width font for standard interface text in the specified size.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class func monospacedSystemFont(ofSize fontSize: CGFloat, weight: UIFont.Weight) -> UIFont
```

```objc
+ (UIFont *) monospacedSystemFontOfSize:(CGFloat) fontSize weight:(UIFontWeight) weight;
```

#### Return Value

A font object of the specified size.

#### Discussion

This method provides the same font as the [`monospaced`](../uifontdescriptor/systemdesign/monospaced.md) system font descriptor. For design guidance, see [Typography](https://developer.apple.com/design/human-interface-guidelines/ios/visual-design/typography/) in the Human Interface Guidelines.

> **Note**:  To display text in the standard system font, but with fixed-width digits, use [`monospacedDigitSystemFont(ofSize:weight:)`](./monospaceddigitsystemfont%28ofsize,weight%29.md) instead.

## Parameters

- `fontSize`: The size (in points) for the font. This value must be greater than `0.0`.
- `weight`: The weight of the font, specified as a font weight constant. For a list of possible values, see [`UIFont.Weight`](./weight.md). Avoid passing an arbitrary floating-point number for `weight`, because a font might not include a variant for every weight.

## See Also

### Creating System Fonts
- [class func systemFont(ofSize: CGFloat) -> UIFont](./systemfont%28ofsize%29.md)
  Returns the font object for standard interface items in the specified size.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./systemfont%28ofsize,weight%29.md)
  Returns the font object for standard interface items in the specified size and weight.
- [UIFont.Weight](./weight.md)
  Constants that represent standard typeface styles.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight, width: UIFont.Width) -> UIFont](./systemfont%28ofsize,weight,width%29.md)
- [UIFont.Width](./width.md)
- [class func boldSystemFont(ofSize: CGFloat) -> UIFont](./boldsystemfont%28ofsize%29.md)
  Returns the font object for standard interface items in boldface type in the specified size.
- [class func italicSystemFont(ofSize: CGFloat) -> UIFont](./italicsystemfont%28ofsize%29.md)
  Returns the font object for standard interface items in italic type in the specified size.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./monospaceddigitsystemfont%28ofsize,weight%29.md)
  Returns the standard system font with all digits of consistent width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/monospacedsystemfont(ofsize:weight:))*