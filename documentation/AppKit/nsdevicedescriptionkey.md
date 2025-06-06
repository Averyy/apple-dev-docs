# NSDeviceDescriptionKey

**Framework**: AppKit  
**Kind**: struct

These constants are the keys for device description dictionaries.

**Availability**:
- macOS ?+

## Declaration

```swift
struct NSDeviceDescriptionKey
```

## Topics

### Type Properties
- [static let bitsPerSample: NSDeviceDescriptionKey](nsdevicedescriptionkey/bitspersample.md)
  The corresponding value is an `NSNumber` object containing an integer that gives the bit depth of the window’s raster image (2-bit, 8-bit, and so forth).
- [static let colorSpaceName: NSDeviceDescriptionKey](nsdevicedescriptionkey/colorspacename.md)
  The corresponding value is an `NSString` object giving the name of the window’s color space.
- [static let isPrinter: NSDeviceDescriptionKey](nsdevicedescriptionkey/isprinter.md)
  If there is a corresponding value, this indicates that the display device is a printer.
- [static let isScreen: NSDeviceDescriptionKey](nsdevicedescriptionkey/isscreen.md)
  If there is a corresponding value, this indicates that the display device is a screen.
- [static let resolution: NSDeviceDescriptionKey](nsdevicedescriptionkey/resolution.md)
  The corresponding value is an `NSValue` object containing a value of type `NSSize` that describes the window’s raster resolution in dots per inch (dpi).
- [static let size: NSDeviceDescriptionKey](nsdevicedescriptionkey/size.md)
  The corresponding value is an `NSValue` object containing a value of type `NSSize` that gives the size of the window’s frame rectangle.
### Initializers
- [init(String)](nsdevicedescriptionkey/init(_:).md)
- [init(rawValue: String)](nsdevicedescriptionkey/init(rawvalue:).md)

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var depth: NSWindow.Depth](nsscreen/depth.md)
  The current bit depth and colorspace information of the screen.
- [var frame: NSRect](nsscreen/frame.md)
  The dimensions and location of the screen.
- [var supportedWindowDepths: UnsafePointer<NSWindow.Depth>](nsscreen/supportedwindowdepths.md)
  A zero-terminated array of the window depths supported by the screen.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](nsscreen/devicedescription.md)
  The device dictionary for the screen.
- [var colorSpace: NSColorSpace?](nsscreen/colorspace.md)
  The color space of the screen.
- [var localizedName: String](nsscreen/localizedname.md)
  The localized name of the display.
- [func canRepresent(NSDisplayGamut) -> Bool](nsscreen/canrepresent(_:).md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](nsdisplaygamut.md)
- [class var screensHaveSeparateSpaces: Bool](nsscreen/screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdevicedescriptionkey)*