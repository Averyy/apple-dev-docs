# init(cgImage:size:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Creates a new image using the contents of the provided image.

**Availability**:
- macOS 10.6+

## Declaration

```swift
convenience init(cgImage: CGImage, size: NSSize)
```

```objc
- (instancetype) initWithCGImage:(CGImageRef) cgImage size:(NSSize) size;
```

#### Discussion

Don’t assume anything about the image, other than drawing it is equivalent to drawing the source image.

This is not a designated initializer.

## Parameters

- `cgImage`: The source image.
- `size`: The size of the new image. Use [`zero`](../../CoreFoundation/cgsize/zero.md), or [`NSZeroSize`](../../Foundation/nszerosize.md) in Objective-C, to have the new image adopt the pixel dimensions of the source image.

## See Also

### Creating Images from Existing Data
- [convenience init?(data: Data)](./init%28data%29.md)
  Initializes and returns an image object using the provided image data.
- [convenience init?(dataIgnoringOrientation: Data)](./init%28dataignoringorientation%29.md)
  Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.
- [convenience init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Initializes and returns an image object with data from the specified pasteboard.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Initializes and returns an image object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(cgimage:size:)-8oznv)*