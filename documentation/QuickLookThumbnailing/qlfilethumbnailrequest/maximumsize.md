# maximumSize

**Framework**: Quick Look Thumbnailing  
**Kind**: property

The maximum accepted size of a thumbnail.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var maximumSize: CGSize { get }
```

#### Discussion

The `maximumSize` accepted is also the preferred size of the thumbnail that you need to create. Your generated thumbnail’s width or height should match the `width` or `height` of the `maximumSize`, or, ideally, both.

## See Also

- [var minimumSize: CGSize](qlfilethumbnailrequest/minimumsize.md)
  The minimum accepted size of a thumbnail.
- [var scale: CGFloat](qlfilethumbnailrequest/scale.md)
  The scale of the requested thumbnail.
- [var fileURL: URL](qlfilethumbnailrequest/fileurl.md)
  The URL of the image file to use for the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlfilethumbnailrequest/maximumsize)*