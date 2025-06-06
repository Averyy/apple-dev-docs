# blueComponent

**Framework**: AppKit  
**Kind**: property

The blue component value of the color.

**Availability**:
- macOS ?+

## Declaration

```swift
var blueComponent: CGFloat { get }
```

#### Discussion

Access this property only for colors in the [`calibratedRGB`](nscolorspacename/calibratedrgb.md) or [`deviceRGB`](nscolorspacename/devicergb.md) color spaces. Accessing it for other color types raises an exception.

## See Also

- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](nscolor/getred(_:green:blue:alpha:).md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [var alphaComponent: CGFloat](nscolor/alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var whiteComponent: CGFloat](nscolor/whitecomponent.md)
  The white component value of the color.
- [var redComponent: CGFloat](nscolor/redcomponent.md)
  The red component value of the color.
- [var greenComponent: CGFloat](nscolor/greencomponent.md)
  The green component value of the color.
- [var cyanComponent: CGFloat](nscolor/cyancomponent.md)
  The cyan component value of the color.
- [var magentaComponent: CGFloat](nscolor/magentacomponent.md)
  The magenta component value of the color.
- [var yellowComponent: CGFloat](nscolor/yellowcomponent.md)
  The yellow component value of the color.
- [var blackComponent: CGFloat](nscolor/blackcomponent.md)
  The black component value of the color.
- [var hueComponent: CGFloat](nscolor/huecomponent.md)
  The hue component value of the color.
- [var saturationComponent: CGFloat](nscolor/saturationcomponent.md)
  The saturation component value of the color.
- [var brightnessComponent: CGFloat](nscolor/brightnesscomponent.md)
  The brightness component value of the color.
- [var catalogNameComponent: NSColorList.Name](nscolor/catalognamecomponent.md)
  The catalog containing the color’s name.
- [var localizedCatalogNameComponent: String](nscolor/localizedcatalognamecomponent.md)
  The localized version of the catalog name containing the color.
- [var colorNameComponent: NSColor.Name](nscolor/colornamecomponent.md)
  The name of the color.
- [var localizedColorNameComponent: String](nscolor/localizedcolornamecomponent.md)
  The localized version of the color name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/bluecomponent)*