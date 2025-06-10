# UIPrintInfo.Duplex

**Framework**: UIKit  
**Kind**: enum

Constants that describe the duplex mode of a selected printer.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Duplex
```

#### Overview

You use these constants when setting the value of the [`duplex`](uiprintinfo/duplex-swift.property.md) property of a `UIPrintInfo` object.

## Topics

### Constants
- [UIPrintInfo.Duplex.none](uiprintinfo/duplex-swift.enum/none.md)
  No double-sided (duplex) printing; single-sided printing only.
- [UIPrintInfo.Duplex.longEdge](uiprintinfo/duplex-swift.enum/longedge.md)
  Duplex printing that flips the back page along the long edge of the paper.
- [UIPrintInfo.Duplex.shortEdge](uiprintinfo/duplex-swift.enum/shortedge.md)
  Duplex print that flips the back page along the short edge of the paper.
### Initializers
- [init?(rawValue: Int)](uiprintinfo/duplex-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var duplex: UIPrintInfo.Duplex](uiprintinfo/duplex-swift.property.md)
  The duplex mode to use for the print job.
- [var jobName: String](uiprintinfo/jobname.md)
  The name of the print job.
- [var orientation: UIPrintInfo.Orientation](uiprintinfo/orientation-swift.property.md)
  The orientation of the printed content, portrait or landscape.
- [UIPrintInfo.Orientation](uiprintinfo/orientation-swift.enum.md)
  Constants that describe the orientation of printing on a page.
- [var outputType: UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.property.md)
  The kind of printable content.
- [UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [var printerID: String?](uiprintinfo/printerid.md)
  An identifier of the printer to use for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/duplex-swift.enum)*