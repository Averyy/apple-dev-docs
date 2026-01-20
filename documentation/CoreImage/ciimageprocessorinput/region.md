# region

**Framework**: Core Image  
**Kind**: property  
**Required**: Yes

The rectangular region of the input image that your Core Image Processor Kernel can use to provide the output.

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

#### Discussion

> **Note**: This will contain but may be larger than the rect returned by ‘roiCallback’.

## See Also

- [var bytesPerRow: Int](ciimageprocessorinput/bytesperrow.md)
  The bytes per row of the CPU memory that your Core Image Processor Kernel can read pixelsfrom.
- [var format: CIFormat](ciimageprocessorinput/format.md)
  The pixel format of the CPU memory that your Core Image Processor Kernel can read pixels from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreimage/ciimageprocessorinput/region)*