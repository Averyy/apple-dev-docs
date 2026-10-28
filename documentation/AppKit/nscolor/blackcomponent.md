# blackComponent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The black component value of the color.

**Availability**:
- macOS

## Declaration

```swift
var blackComponent: CGFloat { get }
```

```objc
@property (readonly) CGFloat blackComponent;
```

## Discussion

Access this property only for colors in the [`deviceCMYK`](../nscolorspacename/devicecmyk.md) color space, which have a black component. Accessing it for other color types raises an exception.

## See Also

### Related Documentation
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getcyan%28_,magenta,yellow,black,alpha%29.md)
  Returns the color object’s CMYK and opacity values.
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
- [var colorNameComponent: NSColor.Name](./colornamecomponent.md)
  The name of the color.
- [var localizedColorNameComponent: String](./localizedcolornamecomponent.md)
  The localized version of the color name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/blackcomponent)*