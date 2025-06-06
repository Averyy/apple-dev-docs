# init(cgimage:physicalSize:orientation:)

**Framework**: ARKit  
**Kind**: init

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

- [init(pixelBuffer: CVPixelBuffer, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](referenceimage/init(pixelbuffer:physicalsize:orientation:).md)
  Creates a reference image from a pixel buffer.
- [static func loadReferenceImages(inGroupNamed: String, bundle: Bundle?) -> [ReferenceImage]](referenceimage/loadreferenceimages(ingroupnamed:bundle:).md)
  Creates multiple reference images based on their group name in an asset catalog.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceimage/init(cgimage:physicalsize:orientation:))*