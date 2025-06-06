# monospacedDigitSystemFont(ofSize:weight:)

**Framework**: Uikit  
**Kind**: method

Returns the standard system font with all digits of consistent width.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func monospacedDigitSystemFont(ofSize fontSize: CGFloat, weight: UIFont.Weight) -> UIFont
```

#### Return Value

A font object of the specified size and weight, with variable-width text and fixed-width digits.

#### Discussion

The system font uses proportional spacing. When displaying numerical data, you can use this method to retrieve a monospace font for displaying that data. With a monospaced font, each digit occupies the same amount of space, which makes it easier to read numbers that are stacked vertically.

> **Note**:  This method returns the same font as [`systemFont(ofSize:weight:)`](uifont/systemfont(ofsize:weight:).md), but with modified digits. If you want all characters to be fixed-width, use [`monospacedSystemFont(ofSize:weight:)`](uifont/monospacedsystemfont(ofsize:weight:).md) instead.

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
- [class func monospacedSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](uifont/monospacedsystemfont(ofsize:weight:).md)
  Returns the fixed-width font for standard interface text in the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/monospaceddigitsystemfont(ofsize:weight:))*