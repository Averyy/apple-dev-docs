# region

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The rectangular region of the output image that your Core Image Processor Kernel must provide.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var region: CGRect { get }
```

```objc
@property (nonatomic, readonly) CGRect region;
```

#### Discussion

> **Note**: This may be different (larger or smaller) than the `extent` that was passed to `/CIImageProcessorKernel/applyWithExtent:inputs:arguments:error:`.

## See Also

### Getting Supplemental Information for Image Processing
- [var metalCommandBuffer: (any MTLCommandBuffer)?](./metalcommandbuffer.md)
  Returns a Metal command buffer object that can be used for encoding commands.
- [var bytesPerRow: Int](./bytesperrow.md)
  The bytes per row of the CPU memory that your Core Image Processor Kernel can write pixels to.
- [var format: CIFormat](./format.md)
  The pixel format of the CPU memory that your Core Image Processor Kernel can write pixels to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/region)*