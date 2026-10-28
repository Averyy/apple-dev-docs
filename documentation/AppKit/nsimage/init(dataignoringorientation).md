# init(dataIgnoringOrientation:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.

**Availability**:
- macOS 10.6+

## Declaration

```swift
convenience init?(dataIgnoringOrientation data: Data)
```

```objc
- (instancetype) initWithDataIgnoringOrientation:(NSData *) data;
```

## Return Value

An initialized `NSImage` object or `nil` if the method cannot create an image representation from the contents of the specified data object.

## Parameters

- `data`: The data object containing the image data. The data can be in any format that macOS supports, including PDF, PICT, EPS, or any number of bitmap data formats.

## See Also

### Creating Images from Existing Data
- [convenience init?(data: Data)](./init%28data%29.md)
  Initializes and returns an image object using the provided image data.
- [convenience init(cgImage: CGImage, size: NSSize)](./init%28cgimage,size%29-8oznv.md)
  Creates a new image using the contents of the provided image.
- [convenience init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Initializes and returns an image object with data from the specified pasteboard.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Initializes and returns an image object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(dataignoringorientation:))*