# apply(withTiledExtent:inputs:arguments:)

**Framework**: Core Image  
**Kind**: method

Call this method on your Core Image Processor Kernel subclass to create a new image based on an array of tile extents that together cover the output.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
class func apply(withTiledExtent tileExtents: [CIVector], inputs: [CIImage]?, arguments args: [String : Any]?) throws -> CIImage
```

#### Return Value

 An autoreleased [`CIImage`](ciimage.md)

#### Discussion

Each tile is a CGRect encoded as a CIVector using +[CIVector vectorWithCGRect:]. The overall output extent is computed as the union of all tile extents.

This method will return `nil` and an error if:

- calling [`outputFormat`](ciimageprocessorkernel/outputformat.md) on your subclass returns an unsupported format.
- calling [`formatForInput(at:)`](ciimageprocessorkernel/formatforinput(at:).md) on your subclass returns an unsupported format.
- your subclass does not implement [`process(with:arguments:output:)`](ciimageprocessorkernel/process(with:arguments:output:).md)

## Parameters

- `tileExtents`: The array of bounding rectangles that the `CIImageProcessorKernel` can produce. Each rectangle in the array is an object created using `/CIVector/vectorWithCGRect:` This method will return `CIImage.emptyImage` if the rectangles in the array have gaps or overlaps.
- `inputs`: An array of [`CIImage`](ciimage.md) objects to use as input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withtiledextent:inputs:arguments:))*