# cgImage

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Instance Property

A thumbnail in the form of a Core Graphics image object.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var cgImage: CGImage { get }
```

```objc
@property (nonatomic, readonly) CGImageRef CGImage;
```

## See Also

### Thumbnail Images
- [var nsImage: NSImage](./nsimage.md)
  A thumbnail in the form of an AppKit image object.
- [var uiImage: UIImage](./uiimage.md)
  A thumbnail in the form of a UIKit image object.
- [var type: QLThumbnailRepresentation.RepresentationType](./type.md)
  The type of thumbnail.
- [var contentRect: CGRect](./contentrect.md)
  The rectangle within the thumbnail image of the document that represents its contents.
- [QLThumbnailRepresentation.RepresentationType](./representationtype.md)
  The different types of thumbnails that you can create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailrepresentation/cgimage)*