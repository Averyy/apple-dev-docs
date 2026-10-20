# init(cgimage:physicalSize:orientation:)

**Framework**: ARKit  
**Kind**: init  
**Role**: Initializer

Creates a reference image from a Core Graphics image.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
init(cgimage: CGImage, physicalSize: CGSize, orientation: CGImagePropertyOrientation = .up)
```

## Parameters

- `cgimage`: The image to use as a reference during tracking.
- `physicalSize`: The size of the image in meters.
- `orientation`: The orientation of the image asset.

## See Also

### Creating a reference image
- [init(pixelBuffer: CVPixelBuffer, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](./init%28pixelbuffer,physicalsize,orientation%29.md)
  Creates a reference image from a pixel buffer.
- [static func loadReferenceImages(inGroupNamed: String, bundle: Bundle?) -> [ReferenceImage]](./loadreferenceimages%28ingroupnamed,bundle%29.md)
  Creates multiple reference images based on their group name in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceimage/init(cgimage:physicalsize:orientation:))*