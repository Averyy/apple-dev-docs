# systemFont(ofSize:weight:)

**Framework**: UIKit  
**Kind**: method

Returns the font object for standard interface items in the specified size and weight.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func systemFont(ofSize fontSize: CGFloat, weight: UIFont.Weight) -> UIFont
```

#### Return Value

A font object of the specified size and weight.

#### Discussion

Instead of using this method to get a font, it’s often more appropriate to use [`preferredFont(forTextStyle:)`](uifont/preferredfont(fortextstyle:).md) because that method respects the user’s selected content size category.

## Parameters

- `fontSize`: The size (in points) to which the font is scaled. This value must be greater than 0.0.
- `weight`: The weight of the font, specified as a font weight constant. For a list of possible values, see “Font Weights” in  . Avoid passing an arbitrary floating-point number for  , because a font might not include a variant for every weight.

## See Also

- [class func systemFont(ofSize: CGFloat) -> UIFont](uifont/systemfont(ofsize:).md)
  Returns the font object for standard interface items in the specified size.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [class func systemFont(ofSize: CGFloat, weight: UIFont.Weight, width: UIFont.Width) -> UIFont](uifont/systemfont(ofsize:weight:width:).md)
- [UIFont.Width](uifont/width.md)
- [class func boldSystemFont(ofSize: CGFloat) -> UIFont](uifont/boldsystemfont(ofsize:).md)
  Returns the font object for standard interface items in boldface type in the specified size.
- [class func italicSystemFont(ofSize: CGFloat) -> UIFont](uifont/italicsystemfont(ofsize:).md)
  Returns the font object for standard interface items in italic type in the specified size.
- [class func monospacedSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospacedsystemfont(ofsize:weight:).md)
  Returns the fixed-width font for standard interface text in the specified size.
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospaceddigitsystemfont(ofsize:weight:).md)
  Returns the standard system font with all digits of consistent width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/systemfont(ofsize:weight:))*