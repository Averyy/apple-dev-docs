# NSColor.ColorType.componentBased

**Framework**: AppKit  
**Kind**: case  
**Role**: Case

Colors that include floating-point color components and a color space.

**Availability**:
- macOS

## Declaration

```swift
case componentBased
```

```c
NSColorTypeComponentBased
```

## Discussion

Examples of this type are RGB, CMYK, and HSB colors. Before acessing components that are specific to one colorspace, such as the [`redComponent`](../redcomponent.md) of an RGB color, call [`usingColorSpace(_:)`](../usingcolorspace%28_%29.md).

## See Also

### Color Types
- [NSColor.ColorType.pattern](./pattern.md)
  Colors that include an image to be used as a pattern.
- [NSColor.ColorType.catalog](./catalog.md)
  Colors that are retrieved from an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colortype/componentbased)*