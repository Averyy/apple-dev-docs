# init(pasteboard:)

**Framework**: AppKit  
**Kind**: init  
**Role**: Initializer

Initializes and returns an image object with data from the specified pasteboard.

**Availability**:
- macOS

## Declaration

```swift
convenience init?(pasteboard: NSPasteboard)
```

```objc
- (instancetype) initWithPasteboard:(NSPasteboard *) pasteboard;
```

## Return Value

An initialized `NSImage` object or `nil` if the method cannot create an image from the contents of the pasteboard.

## Discussion

The specified pasteboard should contain a type supported by one of the registered `NSImageRep` subclasses. The table below lists the default pasteboard types and file extensions for several `NSImageRep` subclasses.

| Image representation class | Default pasteboard type | Default file extensions |
| --- | --- | --- |
| `NSBitmapImageRep` | `NSTIFFPboardType` | `tiff`, `gif`, `jpg`, and others |
| `NSPDFImageRep` | `NSPDFPboardType` | `pdf` |
| `NSEPSImageRep` | `NSPostscriptPboardType` | `eps` |
| `NSPICTImageRep` | `NSPICTPboardType` | `pict` |

If the specified pasteboard contains the value `NSFilenamesPboardType`, each filename on the pasteboard should have an extension supported by one of the registered `NSImageRep` subclasses. You can use the [`imageUnfilteredFileTypes()`](../nsimagerep/imageunfilteredfiletypes%28%29.md) method of a given subclass to obtain the list of supported types for that class.

## Parameters

- `pasteboard`: The pasteboard containing the image data. The data on the pasteboard can be in any format that macOS supports, including PDF, PICT, EPS, or any number of bitmap data formats.

## See Also

### Creating Images from Existing Data
- [convenience init?(data: Data)](./init%28data%29.md)
  Initializes and returns an image object using the provided image data.
- [convenience init?(dataIgnoringOrientation: Data)](./init%28dataignoringorientation%29.md)
  Initializes and returns an image object using the provided image data and ignoring the EXIF orientation tags.
- [convenience init(cgImage: CGImage, size: NSSize)](./init%28cgimage,size%29-8oznv.md)
  Creates a new image using the contents of the provided image.
- [init(coder: NSCoder)](./init%28coder%29.md)
  Initializes and returns an image object from data in an unarchiver.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsimage/init(pasteboard:))*