# apply(tiledExtent:inputs:arguments:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Call this method on your Core Image Processor Kernel subclass to create a new image based on an array of tile extents that together cover the output.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
class func apply(tiledExtent tileExtents: [CIVector], inputs: [CIImage]?, arguments args: [String : Any]?) throws -> CIImage
```

```objc
+ (CIImage *) applyWithTiledExtent:(NSArray<CIVector *> *) tileExtents inputs:(NSArray<CIImage *> *) inputs arguments:(NSDictionary<NSString *,id> *) args error:(NSError **) error;
```

#### Return Value

 An autoreleased [`CIImage`](../ciimage.md)

#### Discussion

Each tile is a CGRect encoded as a CIVector using +[CIVector vectorWithCGRect:]. The overall output extent is computed as the union of all tile extents.

This method will return `nil` and an error if:

- calling [`outputFormat`](./outputformat.md) on your subclass returns an unsupported format.
- calling [`formatForInput(at:)`](./formatforinput%28at%29.md) on your subclass returns an unsupported format.
- your subclass does not implement [`process(with:arguments:output:)`](./process%28with,arguments,output%29.md)

## Parameters

- `tileExtents`: The array of bounding rectangles that the `CIImageProcessorKernel` can produce. Each rectangle in the array is an object created using `/CIVector/vectorWithCGRect:` This method will return `CIImage.emptyImage` if the rectangles in the array have gaps or overlaps.
- `inputs`: An array of [`CIImage`](../ciimage.md) objects to use as input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(tiledextent:inputs:arguments:))*