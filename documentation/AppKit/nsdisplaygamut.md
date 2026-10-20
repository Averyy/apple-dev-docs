# NSDisplayGamut

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- macOS 10.12+

## Declaration

```swift
enum NSDisplayGamut
```

```c
enum NSDisplayGamut : NSInteger;
```

## Topics

### Gamuts
- [NSDisplayGamut.p3](./nsdisplaygamut/p3.md)
- [NSDisplayGamut.sRGB](./nsdisplaygamut/srgb.md)
### Initializers
- [init?(rawValue: Int)](./nsdisplaygamut/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Getting Screen Information
- [var depth: NSWindow.Depth](./nsscreen/depth.md)
  The current bit depth and colorspace information of the screen.
- [var frame: NSRect](./nsscreen/frame.md)
  The dimensions and location of the screen.
- [var supportedWindowDepths: UnsafePointer<NSWindow.Depth>](./nsscreen/supportedwindowdepths.md)
  A zero-terminated array of the window depths supported by the screen.
- [var deviceDescription: [NSDeviceDescriptionKey : Any]](./nsscreen/devicedescription.md)
  The device dictionary for the screen.
- [struct NSDeviceDescriptionKey](./nsdevicedescriptionkey.md)
  These constants are the keys for device description dictionaries.
- [var colorSpace: NSColorSpace?](./nsscreen/colorspace.md)
  The color space of the screen.
- [var localizedName: String](./nsscreen/localizedname.md)
  The localized name of the display.
- [func canRepresent(NSDisplayGamut) -> Bool](./nsscreen/canrepresent%28_%29.md)
  A Boolean value indicating whether the color space of the screen is capable of representing the specified display gamut.
- [class var screensHaveSeparateSpaces: Bool](./nsscreen/screenshaveseparatespaces.md)
  Returns a Boolean value indicating whether each screen can have its own set of spaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdisplaygamut)*