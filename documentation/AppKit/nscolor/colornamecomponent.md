# colorNameComponent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The name of the color.

**Availability**:
- macOS

## Declaration

```swift
var colorNameComponent: NSColor.Name { get }
```

```objc
@property (copy, readonly) NSColorName colorNameComponent;
```

## Discussion

Access this property only for colors in the [`named`](../nscolorspacename/named.md) color space. Accessing it for other color types raises an exception.

## See Also

### Related Documentation
- [init?(catalogName: NSColorList.Name, colorName: NSColor.Name)](./init%28catalogname,colorname%29.md)
  Creates a color object using the specified asset catalog and color names.
### Retrieving individual components
- [var alphaComponent: CGFloat](./alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var whiteComponent: CGFloat](./whitecomponent.md)
  The white component value of the color.
- [var redComponent: CGFloat](./redcomponent.md)
  The red component value of the color.
- [var greenComponent: CGFloat](./greencomponent.md)
  The green component value of the color.
- [var blueComponent: CGFloat](./bluecomponent.md)
  The blue component value of the color.
- [var cyanComponent: CGFloat](./cyancomponent.md)
  The cyan component value of the color.
- [var magentaComponent: CGFloat](./magentacomponent.md)
  The magenta component value of the color.
- [var yellowComponent: CGFloat](./yellowcomponent.md)
  The yellow component value of the color.
- [var blackComponent: CGFloat](./blackcomponent.md)
  The black component value of the color.
- [var hueComponent: CGFloat](./huecomponent.md)
  The hue component value of the color.
- [var saturationComponent: CGFloat](./saturationcomponent.md)
  The saturation component value of the color.
- [var brightnessComponent: CGFloat](./brightnesscomponent.md)
  The brightness component value of the color.
- [var catalogNameComponent: NSColorList.Name](./catalognamecomponent.md)
  The catalog containing the color’s name.
- [var localizedCatalogNameComponent: String](./localizedcatalognamecomponent.md)
  The localized version of the catalog name containing the color.
- [var localizedColorNameComponent: String](./localizedcolornamecomponent.md)
  The localized version of the color name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/colornamecomponent)*