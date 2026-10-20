# init(pixelBuffer:physicalSize:orientation:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a reference image from a pixel buffer.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(pixelBuffer: CVPixelBuffer, physicalSize: CGSize, orientation: CGImagePropertyOrientation = .up)
```

## Parameters

- `pixelBuffer`: The image to use as a reference during tracking.
- `physicalSize`: The size of the image in meters.
- `orientation`: The orientation of the image asset.

## See Also

### Creating a reference image
- [init(cgimage: CGImage, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](./init%28cgimage,physicalsize,orientation%29.md)
  Creates a reference image from a Core Graphics image.
- [static func loadReferenceImages(inGroupNamed: String, bundle: Bundle?) -> [ReferenceImage]](./loadreferenceimages%28ingroupnamed,bundle%29.md)
  Creates multiple reference images based on their group name in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceimage/init(pixelbuffer:physicalsize:orientation:))*