# isPrinter

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

If there is a corresponding value, this indicates that the display device is a printer.

**Availability**:
- macOS

## Declaration

```swift
static let isPrinter: NSDeviceDescriptionKey
```

```c
extern NSDeviceDescriptionKey NSDeviceIsPrinter;
```

## See Also

### Type Properties
- [static let bitsPerSample: NSDeviceDescriptionKey](./bitspersample.md)
  The corresponding value is an `NSNumber` object containing an integer that gives the bit depth of the window’s raster image (2-bit, 8-bit, and so forth).
- [static let colorSpaceName: NSDeviceDescriptionKey](./colorspacename.md)
  The corresponding value is an `NSString` object giving the name of the window’s color space.
- [static let isScreen: NSDeviceDescriptionKey](./isscreen.md)
  If there is a corresponding value, this indicates that the display device is a screen.
- [static let resolution: NSDeviceDescriptionKey](./resolution.md)
  The corresponding value is an `NSValue` object containing a value of type `NSSize` that describes the window’s raster resolution in dots per inch (dpi).
- [static let size: NSDeviceDescriptionKey](./size.md)
  The corresponding value is an `NSValue` object containing a value of type `NSSize` that gives the size of the window’s frame rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdevicedescriptionkey/isprinter)*