# init(data:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an image object using the provided image data.

**Availability**:
- macOS

## Declaration

```swift
convenience init?(data: Data)
```

```objc
- (instancetype) initWithData:(NSData *) data;
```

#### Return Value

An initialized `NSImage` object or `nil` if the method cannot create an image representation from the contents of the specified data object.

#### Discussion

Use this method in cases where you already have image data in a supported format and want to obtain an `NSImage` object that represents that data. This method initializes the object with an image representation that is most appropriate for the type of data you provided.

## Parameters

- `data`: The data object containing the image data. The data can be in any format that macOS supports, including PDF, PICT, EPS, or any number of bitmap data formats.

## See Also

### Creating Images from Existing Data
- [convenience init?(dataIgnoringOrientation: Data)](./init%28dataignoringorientation%29.md)
  Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.
- [convenience init(cgImage: CGImage, size: NSSize)](./init%28cgimage,size%29-8oznv.md)
  Creates a new image using the contents of the provided image.
- [convenience init?(pasteboard: NSPasteboard)](./init%28pasteboard%29.md)
  Initializes and returns an image object with data from the specified pasteboard.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Initializes and returns an image object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(data:))*