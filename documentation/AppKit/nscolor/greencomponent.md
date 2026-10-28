# greenComponent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The green component value of the color.

**Availability**:
- macOS

## Declaration

```swift
var greenComponent: CGFloat { get }
```

```objc
@property (readonly) CGFloat greenComponent;
```

## Discussion

Access this property only for colors in the [`calibratedRGB`](../nscolorspacename/calibratedrgb.md) or [`deviceRGB`](../nscolorspacename/devicergb.md) color spaces. Accessing it for other color types raises an exception.

## See Also

### Related Documentation
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getred%28_,green,blue,alpha%29.md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
### Retrieving individual components
- [var alphaComponent: CGFloat](./alphacomponent.md)
  The alpha (opacity) component value of the color.
- [var whiteComponent: CGFloat](./whitecomponent.md)
  The white component value of the color.
- [var redComponent: CGFloat](./redcomponent.md)
  The red component value of the color.
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
- [var colorNameComponent: NSColor.Name](./colornamecomponent.md)
  The name of the color.
- [var localizedColorNameComponent: String](./localizedcolornamecomponent.md)
  The localized version of the color name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/greencomponent)*