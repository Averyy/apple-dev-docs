# reservedLayoutSize

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The layout size that the system reserves for the image, and then centers the image within.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- tvOS 14.0+
- visionOS

## Declaration

```swift
var reservedLayoutSize: CGSize { get set }
```

#### Discussion

Use this property to ensure:

- Consistent horizontal alignment for images across adjacent content views, even when the images vary in width.
- Consistent height for content views, even when the images vary in height.

The reserved layout size only affects the amount of space for the image, and its positioning within that space. It doesn’t affect the size of the image.

The default value is [`CGSizeZero`](../../../CoreGraphics/cgsizezero.md). A width or height of zero means that the system uses the default behavior for that dimension:

- The system centers symbol images inside a predefined reserved layout size that scales with the content size category.
- Nonsymbol images use a reserved layout size equal to the actual size of the displayed image.

At Accessibility Dynamic Type sizes, content views ignore the reserved layout width. Content views ignore the reserved layout height when using the special Accessibility Dynamic Type layout where text wraps around the image.

## See Also

### Configuring image properties
- [var preferredSymbolConfiguration: UIImage.SymbolConfiguration?](./preferredsymbolconfiguration.md)
  The symbol configuration to use.
- [var tintColor: UIColor?](./tintcolor.md)
  The tint color to apply to the image view.
- [var tintColorTransformer: UIConfigurationColorTransformer?](./tintcolortransformer.md)
  The color transformer for resolving the tint color.
- [func resolvedTintColor(for: UIColor) -> UIColor](./resolvedtintcolor%28for%29.md)
  Generates the resolved tint color for the specified tint color, using the tint color and color transformer.
- [var cornerRadius: CGFloat](./cornerradius.md)
  The preferred corner radius, using a continuous corner curve, for the image.
- [var maximumSize: CGSize](./maximumsize.md)
  The maximum size for the image.
- [static let standardDimension: CGFloat](./standarddimension.md)
  The system standard layout dimension for reserved layout size.
- [var accessibilityIgnoresInvertColors: Bool](./accessibilityignoresinvertcolors.md)
  A Boolean value that determines whether the image inverts its colors when the user turns on the Invert Colors accessibility setting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uilistcontentconfiguration-swift.struct/imageproperties-swift.struct/reservedlayoutsize)*