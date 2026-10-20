# bytesPerRow

**Framework**: Core Image  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The bytes per row of the CPU memory that your Core Image Processor Kernel can read pixelsfrom.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var bytesPerRow: Int { get }
```

```objc
@property (nonatomic, readonly) size_t bytesPerRow;
```

## See Also

### Getting Supplemental Information for Image Processing
- [var region: CGRect](./region.md)
  The rectangular region of the input image that your Core Image Processor Kernel can use to provide the output.
- [var format: CIFormat](./format.md)
  The pixel format of the CPU memory that your Core Image Processor Kernel can read pixels from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/bytesperrow)*