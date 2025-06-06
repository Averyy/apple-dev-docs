# depth

**Framework**: AppKit  
**Kind**: property

The current bit depth and colorspace information of the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
var depth: NSWindow.Depth { get }
```

#### Discussion

This value cannot be used directly. You must pass it to a function such as [`bitsPerPixel`](nswindow/depth/bitsperpixel.md) or [`colorSpaceName`](nswindow/depth/colorspacename.md) to obtain a concrete value for the desired information.

## See Also

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
- [var localizedName: String](nsscreen/localizedname.md)
  The localized name of the display.
- [func canRepresent(NSDisplayGamut) -> Bool](nsscreen/canrepresent(_:).md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](nsdisplaygamut.md)
- [class var screensHaveSeparateSpaces: Bool](nsscreen/screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/depth)*