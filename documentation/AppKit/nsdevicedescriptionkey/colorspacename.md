# colorSpaceName

**Framework**: AppKit  
**Kind**: property

The corresponding value is an `NSString` object giving the name of the window’s color space.

**Availability**:
- macOS ?+

## Declaration

```swift
static let colorSpaceName: NSDeviceDescriptionKey
```

#### Discussion

See Color Space Names in [`Constants`](constants.md) for a list of possible values.

## See Also

- [static let bitsPerSample: NSDeviceDescriptionKey](nsdevicedescriptionkey/bitspersample.md)
  The corresponding value is an `NSNumber` object containing an integer that gives the bit depth of the window’s raster image (2-bit, 8-bit, and so forth).
- [static let isPrinter: NSDeviceDescriptionKey](nsdevicedescriptionkey/isprinter.md)
  If there is a corresponding value, this indicates that the display device is a printer.
- [static let isScreen: NSDeviceDescriptionKey](nsdevicedescriptionkey/isscreen.md)
  If there is a corresponding value, this indicates that the display device is a screen.
- [static let resolution: NSDeviceDescriptionKey](nsdevicedescriptionkey/resolution.md)
  The corresponding value is an `NSValue` object containing a value of type `NSSize` that describes the window’s raster resolution in dots per inch (dpi).
- [static let size: NSDeviceDescriptionKey](nsdevicedescriptionkey/size.md)
  The corresponding value is an `NSValue` object containing a value of type `NSSize` that gives the size of the window’s frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdevicedescriptionkey/colorspacename)*