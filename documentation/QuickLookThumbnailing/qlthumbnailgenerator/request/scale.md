# scale

**Framework**: Quick Look Thumbnailing  
**Kind**: property

The pixel density of the display on the intended device.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
var scale: CGFloat { get }
```

#### Discussion

This property represents the scale factor, or pixel density, of the device’s display as described in [`Image Size and Resolution`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/). For example, the value for a device with a `@2x` display is `2.0`.

You can pass the initializer a screen scale that isn’t the current device’s screen scale. For example, you can create thumbnails for different scales, upload them to a server, and download them later on devices with a different screen scale.

## See Also

- [var size: CGSize](qlthumbnailgenerator/request/size.md)
  The size of the thumbnails.
- [var contentType: UTType!](qlthumbnailgenerator/request/contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](qlthumbnailgenerator/request/minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](qlthumbnailgenerator/request/iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](qlthumbnailgenerator/request/representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/scale)*