# contentRect

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Instance Property

The rectangle within the thumbnail image of the document that represents its contents.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var contentRect: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect contentRect;
```

#### Discussion

In icon mode, the content rectangle is the undecorated rectangle, or frame, that the image sits in.

## See Also

### Thumbnail Images
- [var cgImage: CGImage](./cgimage.md)
  A thumbnail in the form of a Core Graphics image object.
- [var nsImage: NSImage](./nsimage.md)
  A thumbnail in the form of an AppKit image object.
- [var uiImage: UIImage](./uiimage.md)
  A thumbnail in the form of a UIKit image object.
- [var type: QLThumbnailRepresentation.RepresentationType](./type.md)
  The type of thumbnail.
- [QLThumbnailRepresentation.RepresentationType](./representationtype.md)
  The different types of thumbnails that you can create.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailrepresentation/contentrect)*