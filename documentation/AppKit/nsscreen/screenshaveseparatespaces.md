# screensHaveSeparateSpaces

**Framework**: AppKit  
**Kind**: property

Returns a Boolean value indicating whether each screen can have its own set of spaces.

**Availability**:
- macOS 10.9+

## Declaration

```swift
class var screensHaveSeparateSpaces: Bool { get }
```

#### Discussion

This method reflects whether the “Displays have separate Spaces” option is enabled in Mission Control system preference. You might use the return value to determine how to present your app when in fullscreen mode.

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
- [var localizedName: String](nsscreen/localizedname.md)
  The localized name of the display.
- [func canRepresent(NSDisplayGamut) -> Bool](nsscreen/canrepresent(_:).md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](nsdisplaygamut.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/screenshaveseparatespaces)*