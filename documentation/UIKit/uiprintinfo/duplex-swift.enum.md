# UIPrintInfo.Duplex

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIPrintInfoDuplex : NSInteger;
```

## Overview

You use these constants when setting the value of the [`duplex`](./duplex-swift.property.md) property of a `UIPrintInfo` object.

## Topics

### Constants
- [UIPrintInfo.Duplex.none](./duplex-swift.enum/none.md)
  No double-sided (duplex) printing; single-sided printing only.
- [UIPrintInfo.Duplex.longEdge](./duplex-swift.enum/longedge.md)
  Duplex printing that flips the back page along the long edge of the paper.
- [UIPrintInfo.Duplex.shortEdge](./duplex-swift.enum/shortedge.md)
  Duplex print that flips the back page along the short edge of the paper.
### Initializers
- [init?(rawValue: Int)](./duplex-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Managing print-job attributes
- [var duplex: UIPrintInfo.Duplex](./duplex-swift.property.md)
  The duplex mode to use for the print job.
- [var jobName: String](./jobname.md)
  The name of the print job.
- [var orientation: UIPrintInfo.Orientation](./orientation-swift.property.md)
  The orientation of the printed content, portrait or landscape.
- [UIPrintInfo.Orientation](./orientation-swift.enum.md)
  Constants that describe the orientation of printing on a page.
- [var outputType: UIPrintInfo.OutputType](./outputtype-swift.property.md)
  The kind of printable content.
- [UIPrintInfo.OutputType](./outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [var printerID: String?](./printerid.md)
  An identifier of the printer to use for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/duplex-swift.enum)*