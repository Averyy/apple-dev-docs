# UIPrintInfo.OutputType

**Framework**: UIKit  
**Kind**: enum

Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum OutputType
```

#### Overview

You use these constants when setting the value of the [`outputType`](uiprintinfo/outputtype-swift.property.md) property of a `UIPrintInfo` object.

## Topics

### Constants
- [UIPrintInfo.OutputType.general](uiprintinfo/outputtype-swift.enum/general.md)
  Specifies that the printed content consists of mixed text, graphics, and images. The default paper is Letter, A4, or similar locale-specific designation. Output is normal quality, duplex.
- [UIPrintInfo.OutputType.photo](uiprintinfo/outputtype-swift.enum/photo.md)
  Specifies that the printed content consists of black-and-white or color images. The default paper is 4x6, A6, or similar locale-specific designation. Output is high quality, simplex.
- [UIPrintInfo.OutputType.grayscale](uiprintinfo/outputtype-swift.enum/grayscale.md)
  Specifies that the printed content is grayscale. Set the output type to this value when your printable content contains no color—for example, it’s black text only. The default paper is Letter/A4. Output is grayscale quality, duplex. This content type can produce a performance improvement in some cases.
- [UIPrintInfo.OutputType.photoGrayscale](uiprintinfo/outputtype-swift.enum/photograyscale.md)
  Specifies that the printed content is a grayscale image. Set the output type to this value when your printable content contains no color—for example, it’s black text only. The default paper is Letter/A4. Output is high quality grayscale, duplex.
### Initializers
- [init?(rawValue: Int)](uiprintinfo/outputtype-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var duplex: UIPrintInfo.Duplex](uiprintinfo/duplex-swift.property.md)
  The duplex mode to use for the print job.
- [UIPrintInfo.Duplex](uiprintinfo/duplex-swift.enum.md)
  Constants that describe the duplex mode of a selected printer.
- [var jobName: String](uiprintinfo/jobname.md)
  The name of the print job.
- [var orientation: UIPrintInfo.Orientation](uiprintinfo/orientation-swift.property.md)
  The orientation of the printed content, portrait or landscape.
- [UIPrintInfo.Orientation](uiprintinfo/orientation-swift.enum.md)
  Constants that describe the orientation of printing on a page.
- [var outputType: UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.property.md)
  The kind of printable content.
- [var printerID: String?](uiprintinfo/printerid.md)
  An identifier of the printer to use for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype-swift.enum)*