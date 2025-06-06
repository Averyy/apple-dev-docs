# NSColor.ColorType.componentBased

**Framework**: AppKit  
**Kind**: case

Colors that include floating-point color components and a color space.

**Availability**:
- macOS ?+

## Declaration

```swift
case componentBased
```

#### Discussion

Examples of this type are RGB, CMYK, and HSB colors. Before acessing components that are specific to one colorspace, such as the [`redComponent`](nscolor/redcomponent.md) of an RGB color, call [`usingColorSpace(_:)`](nscolor/usingcolorspace(_:).md).

## See Also

- [NSColor.ColorType.pattern](nscolor/colortype/pattern.md)
  Colors that include an image to be used as a pattern.
- [NSColor.ColorType.catalog](nscolor/colortype/catalog.md)
  Colors that are retrieved from an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colortype/componentbased)*