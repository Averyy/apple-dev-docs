# apply(withExtents:inputs:arguments:)

**Framework**: Core Image  
**Kind**: method  
**Role**: Type Method

Call this method on your multiple-output Core Image Processor Kernel subclass to create an array of new image objects given the specified array of extents.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+

## Declaration

```swift
class func apply(withExtents extents: [CIVector], inputs: [CIImage]?, arguments: [String : Any]?) throws -> [CIImage]
```

```objc
+ (NSArray<CIImage *> *) applyWithExtents:(NSArray<CIVector *> *) extents inputs:(NSArray<CIImage *> *) inputs arguments:(NSDictionary<NSString *,id> *) arguments error:(NSError **) error;
```

#### Return Value

 An autoreleased [`CIImage`](../ciimage.md)

#### Discussion

The inputs and arguments will be retained so that your subclass can be called when the image is drawn.

This method will return `nil` and an error if:

- calling [`outputFormat(at:arguments:)`](./outputformat%28at,arguments%29.md) on your subclass returns an unsupported format.
- calling [`formatForInput(at:)`](./formatforinput%28at%29.md) on your subclass returns an unsupported format.
- your subclass does not implement [`process(with:arguments:output:)`](./process%28with,arguments,output%29.md)

## Parameters

- `extents`: The array of bounding rectangles that the `CIImageProcessorKernel` can produce. Each rectangle in the array is an object created using `/CIVector/vectorWithCGRect:` This method will return `CIImage.emptyImage` if a rectangle in the array is empty.
- `inputs`: An array of [`CIImage`](../ciimage.md) objects to use as input.
- `arguments`: This dictionary contains any additional parameters that the processor needs to produce its output. The argument objects can be of any type but in order for CoreImage to cache intermediates, they must be of the following immutable types: `NSArray`, `NSDictionary`, `NSNumber`, `NSValue`, `NSData`, `NSString`, `NSNull`, [`CIVector`](../civector.md), [`CIColor`](../cicolor.md), `CGImage`, `CGColorSpace`, or `MLModel`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorkernel/apply(withextents:inputs:arguments:))*