# init(device:histogramInfo:)

**Framework**: Metal Performance Shaders  
**Kind**: init  
**Role**: Initializer

Initializes a histogram with specific information.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
init(device: any MTLDevice, histogramInfo: UnsafePointer<MPSImageHistogramInfo>)
```

```objc
- (instancetype) initWithDevice:(id<MTLDevice>) device histogramInfo:(const MPSImageHistogramInfo *) histogramInfo;
```

#### Return Value

An initialized histogram object.

## Parameters

- `device`: The Metal device the filter will run on.
- `histogramInfo`: A pointer to a structure describing the histogram content.

## See Also

### Methods
- [struct MPSImageHistogramInfo](../mpsimagehistograminfo.md)
  The information used to compute the histogram channels of an image.
- [func encode(to: any MTLCommandBuffer, sourceTexture: any MTLTexture, histogram: any MTLBuffer, histogramOffset: Int)](./encode%28to,sourcetexture,histogram,histogramoffset%29.md)
  Encodes the filter to a command buffer using a compute command encoder.
- [func histogramSize(forSourceFormat: MTLPixelFormat) -> Int](./histogramsize%28forsourceformat%29.md)
  The amount of space the histogram will take up in the output buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsimagehistogram/init(device:histograminfo:))*