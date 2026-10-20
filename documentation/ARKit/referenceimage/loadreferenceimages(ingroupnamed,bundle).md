# loadReferenceImages(inGroupNamed:bundle:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Type Method

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
- `bundle`: The bundle that contains the image assets. If `nil`, this method loads reference images from the main bundle.

## See Also

### Creating a reference image
- [init(cgimage: CGImage, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](./init%28cgimage,physicalsize,orientation%29.md)
  Creates a reference image from a Core Graphics image.
- [init(pixelBuffer: CVPixelBuffer, physicalSize: CGSize, orientation: CGImagePropertyOrientation)](./init%28pixelbuffer,physicalsize,orientation%29.md)
  Creates a reference image from a pixel buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/referenceimage/loadreferenceimages(ingroupnamed:bundle:))*