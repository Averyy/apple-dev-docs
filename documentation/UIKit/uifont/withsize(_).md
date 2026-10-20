# withSize(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Returns a font object that is the same as the font, but has the specified size.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func withSize(_ fontSize: CGFloat) -> UIFont
```

```objc
- (UIFont *) fontWithSize:(CGFloat) fontSize;
```

#### Return Value

A font object of the specified size.

## Parameters

- `fontSize`: The desired size (in points) of the new font object. This value must be greater than 0.0.

## See Also

### Creating Fonts
- [Scaling fonts automatically](../scaling-fonts-automatically.md)
  Scale text in your interface automatically using Dynamic Type.
- [Creating self-sizing table view cells](../creating-self-sizing-table-view-cells.md)
  Create table view cells that support Dynamic Type and use system spacing constraints to adjust the spacing surrounding text labels.
- [class func preferredFont(forTextStyle: UIFont.TextStyle) -> UIFont](./preferredfont%28fortextstyle%29.md)
  Returns an instance of the system font for the specified text style with scaling for the user’s selected content size category.
- [class func preferredFont(forTextStyle: UIFont.TextStyle, compatibleWith: UITraitCollection?) -> UIFont](./preferredfont%28fortextstyle,compatiblewith%29.md)
  Returns an instance of the system font for the appropriate text style and traits.
- [UIFont.TextStyle](./textstyle.md)
  Constants that describe the preferred styles for fonts.
- [init?(name: String, size: CGFloat)](./init%28name,size%29.md)
  Creates and returns a font object for the specified font name and size.
- [init(descriptor: UIFontDescriptor, size: CGFloat)](./init%28descriptor,size%29.md)
  Returns a font that matches the specified font descriptor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifont/withsize(_:))*