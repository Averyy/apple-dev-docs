# QLThumbnailRepresentation

**Framework**: Quick Look Thumbnailing  
**Kind**: class

Information about the thumbnail that the thumbnail generator returns.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
class QLThumbnailRepresentation
```

#### Overview

QuickLook Thumbnailing is a non-UI framework, so your app doesn’t have to link to either [`UIKit`](https://developer.apple.com/documentation/uikit) or [`AppKit`](https://developer.apple.com/documentation/appkit). Quicklook Thumbnailing generates a thumbnail as a Core Graphics image object and makes the thumbnail available as the [`cgImage`](qlthumbnailrepresentation/cgimage.md) property. If an app links to AppKit or UIKit, the thumbnail is available through the [`nsImage`](qlthumbnailrepresentation/nsimage.md) or [`uiImage`](qlthumbnailrepresentation/uiimage.md) properties.

For more information on the different types of thumbnails that [`QLThumbnailGenerator`](qlthumbnailgenerator.md) can create, see [`QLThumbnailGenerator.Request.RepresentationTypes`](qlthumbnailgenerator/request/representationtypes-swift.struct.md).

## Topics

### Thumbnail Images
- [var cgImage: CGImage](qlthumbnailrepresentation/cgimage.md)
  A thumbnail in the form of a Core Graphics image object.
- [var nsImage: NSImage](qlthumbnailrepresentation/nsimage.md)
  A thumbnail in the form of an AppKit image object.
- [var uiImage: UIImage](qlthumbnailrepresentation/uiimage.md)
  A thumbnail in the form of a UIKit image object.
- [var type: QLThumbnailRepresentation.RepresentationType](qlthumbnailrepresentation/type.md)
  The type of thumbnail.
- [var contentRect: CGRect](qlthumbnailrepresentation/contentrect.md)
  The rectangle within the thumbnail image of the document that represents its contents.
- [QLThumbnailRepresentation.RepresentationType](qlthumbnailrepresentation/representationtype.md)
  The different types of thumbnails that you can create.

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [Creating Quick Look Thumbnails to Preview Files in Your App](creating-quick-look-thumbnails-to-preview-files-in-your-app.md)
  Generate thumbnails of images, text files, PDFs, audio files, videos, and more.
- [class QLThumbnailGenerator](qlthumbnailgenerator.md)
  An object that generates thumbnail images based on provided requirements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailrepresentation)*