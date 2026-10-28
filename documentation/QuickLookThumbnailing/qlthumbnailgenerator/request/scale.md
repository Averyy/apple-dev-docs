# scale

**Framework**: Quick Look Thumbnailing  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (nonatomic, readonly) CGFloat scale;
```

## Discussion

This property represents the scale factor, or pixel density, of the device’s display as described in [Image Size and Resolution](https://developer.apple.com/design/human-interface-guidelines/ios/icons-and-images/image-size-and-resolution/). For example, the value for a device with a `@2x` display is `2.0`.

You can pass the initializer a screen scale that isn’t the current device’s screen scale. For example, you can create thumbnails for different scales, upload them to a server, and download them later on devices with a different screen scale.

## See Also

### Describing the Requested Thumbnail
- [var size: CGSize](./size.md)
  The size of the thumbnails.
- [var contentType: UTType!](./contenttype.md)
  The content type of the source data for the thumbnail request.
- [var representationTypes: QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.property.md)
  The thumbnail sizes that you provide for a thumbnail request.
- [var minimumDimension: CGFloat](./minimumdimension.md)
  The minimum height or width for a generated thumbnail.
- [var iconMode: Bool](./iconmode.md)
  A Boolean value indicating whether the generated thumbnail request should include icon decorations.
- [QLThumbnailGenerator.Request.RepresentationTypes](./representationtypes-swift.struct.md)
  The various types of thumbnails that you can request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookthumbnailing/qlthumbnailgenerator/request/scale)*