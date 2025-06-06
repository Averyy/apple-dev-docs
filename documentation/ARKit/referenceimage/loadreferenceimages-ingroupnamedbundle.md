# loadReferenceImages(inGroupNamed:bundle:)

**Framework**: ARKit  
**Kind**: method

Creates multiple reference images based on their group name in an asset catalog.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
static func loadReferenceImages(inGroupNamed groupName: String, bundle: Bundle? = nil) -> [ReferenceImage]
```

#### Return Value

An array of reference images loaded from the group you specify.

## Parameters

- `groupName`: The name of the group of assets in an asset catalog.
- `bundle`: The bundle that contains the image assets. If  , this method loads reference images from the main bundle.

## See Also

- [init(cgimage: CGImage, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](referenceimage/init(cgimage:physicalsize:orientation:).md)
  Creates a reference image from a Core Graphics image.
- [init(pixelBuffer: CVPixelBuffer, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](referenceimage/init(pixelbuffer:physicalsize:orientation:).md)
  Creates a reference image from a pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceimage/loadreferenceimages(ingroupnamed:bundle:))*