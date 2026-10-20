# init(coder:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an image object from data in an unarchiver.

**Availability**:
- macOS

## Declaration

```swift
init(coder: NSCoder)
```

```objc
- (instancetype) initWithCoder:(NSCoder *) coder;
```

## See Also

### Creating Images from Existing Data
- [convenience init?(data: Data)](./init%28data%29.md)
  Initializes and returns an image object using the provided image data.
- [convenience init?(dataIgnoringOrientation: Data)](./init%28dataignoringorientation%29.md)
  Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.
- [convenience init(cgImage: CGImage, size: NSSize)](./init%28cgimage,size%29-8oznv.md)
  Creates a new image using the contents of the provided image.
- [convenience init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Initializes and returns an image object with data from the specified pasteboard.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(coder:))*