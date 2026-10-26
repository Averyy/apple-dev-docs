# localizedName

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The localized name of the display.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var localizedName: String { get }
```

```objc
@property (copy, readonly) NSString * localizedName;
```

## See Also

### Getting Screen Information
- [var depth: NSWindow.Depth](./depth.md)
  The current bit depth and colorspace information of the screen.
- [var frame: NSRect](./frame.md)
  The dimensions and location of the screen.
- [var supportedWindowDepths: UnsafePointer<NSWindow.Depth>](./supportedwindowdepths.md)
  A zero-terminated array of the window depths supported by the screen.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](./devicedescription.md)
  The device dictionary for the screen.
- [struct NSDeviceDescriptionKey](../nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var colorSpace: NSColorSpace?](./colorspace.md)
  The color space of the screen.
- [func canRepresent(NSDisplayGamut) -> Bool](./canrepresent%28_%29.md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](../nsdisplaygamut.md)
- [class var screensHaveSeparateSpaces: Bool](./screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.
- [- userSpaceScaleFactor](./userspacescalefactor.md)
  Returns the scaling factor from user space to device space on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/localizedname)*