# localizedName

**Framework**: AppKit  
**Kind**: property

The localized name of the display.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var localizedName: String { get }
```

## See Also

- [var depth: NSWindow.Depth](nsscreen/depth.md)
  The current bit depth and colorspace information of the screen.
- [var frame: NSRect](nsscreen/frame.md)
  The dimensions and location of the screen.
- [var supportedWindowDepths: UnsafePointer<NSWindow.Depth>](nsscreen/supportedwindowdepths.md)
  A zero-terminated array of the window depths supported by the screen.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](nsscreen/devicedescription.md)
  The device dictionary for the screen.
- [struct NSDeviceDescriptionKey](nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var colorSpace: NSColorSpace?](nsscreen/colorspace.md)
  The color space of the screen.
- [func canRepresent(NSDisplayGamut) -> Bool](nsscreen/canrepresent(_:).md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](nsdisplaygamut.md)
- [class var screensHaveSeparateSpaces: Bool](nsscreen/screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/localizedname)*