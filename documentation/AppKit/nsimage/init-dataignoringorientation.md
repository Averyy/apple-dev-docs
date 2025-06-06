# init(dataIgnoringOrientation:)

**Framework**: AppKit  
**Kind**: init

Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.

**Availability**:
- macOS 10.6+

## Declaration

```swift
convenience init?(dataIgnoringOrientation data: Data)
```

#### Return Value

An initialized `NSImage` object or `nil` if the method cannot create an image representation from the contents of the specified data object.

## Parameters

- `data`: The data object containing the image data. The data can be in any format that macOS supports, including PDF, PICT, EPS, or any number of bitmap data formats.

## See Also

- [convenience init?(data: Data)](nsimage/init(data:).md)
  Initializes and returns an image object using the provided image data.
- [convenience init(cgImage: CGImage, size: NSSize)](nsimage/init(cgimage:size:).md)
  Creates a new image using the contents of the provided image.
- [convenience init?(pasteboard: NSPasteboard)](nsimage/init(pasteboard:).md)
  Initializes and returns an image object with data from the specified pasteboard.
- [init(coder: NSCoder)](nsimage/init(coder:).md)
  Initializes and returns an image object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(dataignoringorientation:))*