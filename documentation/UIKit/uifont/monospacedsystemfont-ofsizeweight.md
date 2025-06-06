# monospacedSystemFont(ofSize:weight:)

**Framework**: UIKit  
**Kind**: method

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

#### Return Value

A font object of the specified size.

#### Discussion

This method provides the same font as the [`monospaced`](uifontdescriptor/systemdesign/monospaced.md) system font descriptor. For design guidance, see [`Typography`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/visual-design/typography/) in the Human Interface Guidelines.

> **Note**:  To display text in the standard system font, but with fixed-width digits, use [`monospacedDigitSystemFont(ofSize:weight:)`](uifont/monospaceddigitsystemfont(ofsize:weight:).md) instead.

 To display text in the standard system font, but with fixed-width digits, use [`monospacedDigitSystemFont(ofSize:weight:)`](uifont/monospaceddigitsystemfont(ofsize:weight:).md) instead.

## Parameters

- `fontSize`: The size (in points) for the font. This value must be greater than  .
- `weight`: The weight of the font, specified as a font weight constant. For a list of possible values, see  . Avoid passing an arbitrary floating-point number for  , because a font might not include a variant for every weight.

## See Also

- [class func systemFont(ofSize: CGFloat) -> UIFont](uifont/systemfont(ofsize:).md)
  Returns the font object for standard interface items in the specified size.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/systemfont(ofsize:weight:).md)
  Returns the font object for standard interface items in the specified size and weight.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight, width: UIFont.Width) -> UIFont](uifont/systemfont(ofsize:weight:width:).md)
- [UIFont.Width](uifont/width.md)
- [class func boldSystemFont(ofSize: CGFloat) -> UIFont](uifont/boldsystemfont(ofsize:).md)
  Returns the font object for standard interface items in boldface type in the specified size.
- [class func italicSystemFont(ofSize: CGFloat) -> UIFont](uifont/italicsystemfont(ofsize:).md)
  Returns the font object for standard interface items in italic type in the specified size.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospaceddigitsystemfont(ofsize:weight:).md)
  Returns the standard system font with all digits of consistent width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/monospacedsystemfont(ofsize:weight:))*