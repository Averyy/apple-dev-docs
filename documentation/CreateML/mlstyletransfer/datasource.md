# MLStyleTransfer.DataSource

**Framework**: Create ML  
**Kind**: enum

A data source for a style transfer model.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum DataSource
```

## Topics

### Creating a data source
- [case images(styleImage: URL, contentDirectory: URL, processingOption: VNImageCropAndScaleOption?)](mlstyletransfer/datasource/images(styleimage:contentdirectory:processingoption:).md)
  The locations of a style-image file and content-image directory in the file system.
### Stylizing images
- [func processImages(textelDensity: Int, styleImageDestination: URL?, contentImagesDestination: URL?) throws -> (processedStyleImage: URL, processedContentImages: URL)](mlstyletransfer/datasource/processimages(texteldensity:styleimagedestination:contentimagesdestination:).md)
  Converts the content images to square images and saves them to a destination directory.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLStyleTransfer.ModelParameters](mlstyletransfer/modelparameters.md)
  Parameters that affect the training process of a style transfer model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlstyletransfer/datasource)*