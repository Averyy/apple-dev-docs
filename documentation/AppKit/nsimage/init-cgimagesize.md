# init(cgImage:size:)

**Framework**: AppKit  
**Kind**: init

Creates a new image using the contents of the provided image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
convenience init(cgImage: CGImage, size: NSSize)
```

#### Discussion

Don’t assume anything about the image, other than drawing it is equivalent to drawing the source image.

This is not a designated initializer.

## Parameters

- `cgImage`: The source image.
- `size`: The size of the new image. Use  , or   in Objective-C, to have the new image adopt the pixel dimensions of the source image.

## See Also

- [convenience init?(data: Data)](nsimage/init(data:).md)
  Initializes and returns an image object using the provided image data.
- [convenience init?(dataIgnoringOrientation: Data)](nsimage/init(dataignoringorientation:).md)
  Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.
- [convenience init?(pasteboard: NSPasteboard)](nsimage/init(pasteboard:).md)
  Initializes and returns an image object with data from the specified pasteboard.
- [init(coder: NSCoder)](nsimage/init(coder:).md)
  Initializes and returns an image object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(cgimage:size:))*