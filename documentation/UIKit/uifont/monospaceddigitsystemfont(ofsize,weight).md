# monospacedDigitSystemFont(ofSize:weight:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (UIFont *) monospacedDigitSystemFontOfSize:(CGFloat) fontSize weight:(UIFontWeight) weight;
```

## Return Value

A font object of the specified size and weight, with variable-width text and fixed-width digits.

## Discussion

The system font uses proportional spacing. When displaying numerical data, you can use this method to retrieve a monospace font for displaying that data. With a monospaced font, each digit occupies the same amount of space, which makes it easier to read numbers that are stacked vertically.

> **Note**:  This method returns the same font as [`systemFont(ofSize:weight:)`](./systemfont%28ofsize,weight%29.md), but with modified digits. If you want all characters to be fixed-width, use [`monospacedSystemFont(ofSize:weight:)`](./monospacedsystemfont%28ofsize,weight%29.md) instead.

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
- [class func monospacedSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./monospacedsystemfont%28ofsize,weight%29.md)
  Returns the fixed-width font for standard interface text in the specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/monospaceddigitsystemfont(ofsize:weight:))*