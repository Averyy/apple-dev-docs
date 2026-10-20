# systemFont(ofSize:weight:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns the font object for standard interface items in the specified size and weight.

**Availability**:
- iOS 8.2+
- iPadOS 8.2+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func systemFont(ofSize fontSize: CGFloat, weight: UIFont.Weight) -> UIFont
```

```objc
+ (UIFont *) systemFontOfSize:(CGFloat) fontSize weight:(UIFontWeight) weight;
```

#### Return Value

A font object of the specified size and weight.

#### Discussion

Instead of using this method to get a font, it’s often more appropriate to use [`preferredFont(forTextStyle:)`](./preferredfont%28fortextstyle%29.md) because that method respects the user’s selected content size category.

## Parameters

- `fontSize`: The size (in points) to which the font is scaled. This value must be greater than 0.0.
- `weight`: The weight of the font, specified as a font weight constant. For a list of possible values, see “Font Weights” in [`UIFontDescriptor`](../uifontdescriptor.md). Avoid passing an arbitrary floating-point number for `weight`, because a font might not include a variant for every weight.

## See Also

### Creating System Fonts
- [class func systemFont(ofSize: CGFloat) -> UIFont](./systemfont%28ofsize%29.md)
  Returns the font object for standard interface items in the specified size.
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
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./monospaceddigitsystemfont%28ofsize,weight%29.md)
  Returns the standard system font with all digits of consistent width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/systemfont(ofsize:weight:))*