# deviceDescription

**Framework**: AppKit  
**Kind**: property

The device dictionary for the screen.

**Availability**:
- macOS ?+

## Declaration

```swift
var deviceDescription: [NSDeviceDescriptionKey : Any] { get }
```

#### Discussion

This is a dictionary containing the attributes of the receiver’s screen. For the list of keys you can use to retrieve values from the returned dictionary, see `Display Device—Descriptions`.

In addition to the display device constants described in [`NSWindow`](nswindow.md), you can also retrieve the [`CGDirectDisplayID`](https://developer.apple.com/documentation/CoreGraphics/CGDirectDisplayID) value associated with the screen from this dictionary. To access this value, specify the Objective-C string `@"NSScreenNumber"` as the key when requesting the item from the dictionary. The value associated with this key is an [`NSNumber`](https://developer.apple.com/documentation/Foundation/NSNumber) object containing the display ID value. This string is only valid when used as a key for the dictionary returned by this method.

## See Also

- [var depth: NSWindow.Depth](nsscreen/depth.md)
  The current bit depth and colorspace information of the screen.
- [var frame: NSRect](nsscreen/frame.md)
  The dimensions and location of the screen.
- [var supportedWindowDepths: UnsafePointer<NSWindow.Depth>](nsscreen/supportedwindowdepths.md)
  A zero-terminated array of the window depths supported by the screen.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsscreen/devicedescription)*