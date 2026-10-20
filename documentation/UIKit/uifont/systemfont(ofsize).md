# systemFont(ofSize:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Type Method

Returns the font object for standard interface items in the specified size.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func systemFont(ofSize fontSize: CGFloat) -> UIFont
```

```objc
+ (UIFont *) systemFontOfSize:(CGFloat) fontSize;
```

#### Return Value

A font object of the specified size.

#### Discussion

Instead of using this method to get a font, it’s often more appropriate to use [`preferredFont(forTextStyle:)`](./preferredfont%28fortextstyle%29.md) because that method respects the user’s selected content size category.

## Parameters

- `fontSize`: The size (in points) to which the font is scaled. This value must be greater than 0.0.

## See Also

### Creating System Fonts
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
- [class func monospacedDigitSystemFont(ofSize: CGFloat, weight: UIFont.Weight) -> UIFont](./monospaceddigitsystemfont%28ofsize,weight%29.md)
  Returns the standard system font with all digits of consistent width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/systemfont(ofsize:))*