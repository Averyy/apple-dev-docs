# supportedWindowDepths

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A zero-terminated array of the window depths supported by the screen.

**Availability**:
- macOS

## Declaration

```swift
var supportedWindowDepths: UnsafePointer<NSWindow.Depth> { get }
```

```objc
@property (readonly) const NSWindowDepth * supportedWindowDepths;
```

## Discussion

This is a C-style array of window depths. The returned values cannot be used directly. You must pass each one to a function such as [`bitsPerPixel`](../nswindow/depth/bitsperpixel.md) or [`colorSpaceName`](../nswindow/depth/colorspacename.md) to obtain a concrete value for the desired screen.

## See Also

### Getting Screen Information
- [var depth: NSWindow.Depth](./depth.md)
  The current bit depth and colorspace information of the screen.
- [var frame: NSRect](./frame.md)
  The dimensions and location of the screen.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](./devicedescription.md)
  The device dictionary for the screen.
- [struct NSDeviceDescriptionKey](../nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var colorSpace: NSColorSpace?](./colorspace.md)
  The color space of the screen.
- [var localizedName: String](./localizedname.md)
  The localized name of the display.
- [func canRepresent(NSDisplayGamut) -> Bool](./canrepresent%28_%29.md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](../nsdisplaygamut.md)
- [class var screensHaveSeparateSpaces: Bool](./screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.
- [- userSpaceScaleFactor](./userspacescalefactor.md)
  Returns the scaling factor from user space to device space on the screen.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/supportedwindowdepths)*