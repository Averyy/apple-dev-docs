# alphaComponent

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The alpha (opacity) component value of the color.

**Availability**:
- macOS

## Declaration

```swift
var alphaComponent: CGFloat { get }
```

```objc
@property (readonly) CGFloat alphaComponent;
```

## Discussion

The value of this property is between `0.0` and `1.0`, where `0.0` represents fully transparent and `1.0` represents fully opaque. If the color has no alpha component, the value of this property is `1.0`.

## See Also

### Related Documentation
- [func getRed(UnsafeMutablePointer<CGFloat>?, green: UnsafeMutablePointer<CGFloat>?, blue: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getred%28_,green,blue,alpha%29.md)
  Returns the color object’s RGB component and opacity values in the respective arguments.
- [func getHue(UnsafeMutablePointer<CGFloat>?, saturation: UnsafeMutablePointer<CGFloat>?, brightness: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./gethue%28_,saturation,brightness,alpha%29.md)
  Returns the color object’s HSB component and opacity values in the respective arguments.
- [func getCyan(UnsafeMutablePointer<CGFloat>?, magenta: UnsafeMutablePointer<CGFloat>?, yellow: UnsafeMutablePointer<CGFloat>?, black: UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getcyan%28_,magenta,yellow,black,alpha%29.md)
  Returns the color object’s CMYK and opacity values.
- [func getWhite(UnsafeMutablePointer<CGFloat>?, alpha: UnsafeMutablePointer<CGFloat>?)](./getwhite%28_,alpha%29.md)
  Returns the grayscale and alpha values of the color.
### Retrieving individual components
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
- [var colorNameComponent: NSColor.Name](./colornamecomponent.md)
  The name of the color.
- [var localizedColorNameComponent: String](./localizedcolornamecomponent.md)
  The localized version of the color name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscolor/alphacomponent)*