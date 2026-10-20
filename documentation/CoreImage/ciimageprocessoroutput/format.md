# format

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The pixel format of the CPU memory that your Core Image Processor Kernel can write pixels to.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var format: CIFormat { get }
```

```objc
@property (nonatomic, readonly) CIFormat format;
```

## See Also

### Getting Supplemental Information for Image Processing
- [var region: CGRect](./region.md)
  The rectangular region of the output image that your Core Image Processor Kernel must provide.
- [var metalCommandBuffer: (any MTLCommandBuffer)?](./metalcommandbuffer.md)
  Returns a Metal command buffer object that can be used for encoding commands.
- [var bytesPerRow: Int](./bytesperrow.md)
  The bytes per row of the CPU memory that your Core Image Processor Kernel can write pixels to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessoroutput/format)*