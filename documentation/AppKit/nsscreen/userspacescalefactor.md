# userSpaceScaleFactor

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the scaling factor from user space to device space on the screen.

**Availability**:
- macOS 10.4+ - Deprecated in 10.7

## Declaration

```objc
- (CGFloat) userSpaceScaleFactor;
```

## Return Value

The scaling factor, measured in pixels per point, where a point is always equal to 1/72 of an inch. For example, a scaling factor of `2.0` indicates the display has a resolution 2 pixels per point or 144 pixels per inch.

## See Also

### Related Documentation
- [func convertRectToBacking(NSRect) -> NSRect](./convertrecttobacking%28_%29.md)
  Converts the rectangle to the device pixel aligned coordinates system of a screen.
- [var backingScaleFactor: CGFloat](./backingscalefactor.md)
  The backing store pixel scale factor for the screen.
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
- [var localizedName: String](./localizedname.md)
  The localized name of the display.
- [func canRepresent(NSDisplayGamut) -> Bool](./canrepresent%28_%29.md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [enum NSDisplayGamut](../nsdisplaygamut.md)
- [class var screensHaveSeparateSpaces: Bool](./screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/userspacescalefactor)*