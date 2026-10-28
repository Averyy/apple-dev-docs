# UIPrintInfo.Orientation

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

Constants that describe the orientation of printing on a page.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Orientation
```

```c
enum UIPrintInfoOrientation : NSInteger;
```

## Overview

You use these constants when setting the value of the [`orientation`](./orientation-swift.property.md) property of a `UIPrintInfo` object.

> **Note**:  UIKit ignores the [`orientation`](./orientation-swift.property.md) property when printable content is assigned to the `printingItem` or `printingItems` properties of the shared [`UIPrintInteractionController`](../uiprintinteractioncontroller.md) object. It determines the orientation based on the type of content.

## Topics

### Constants
- [UIPrintInfo.Orientation.portrait](./orientation-swift.enum/portrait.md)
  Pages are printed in portrait orientation.
- [UIPrintInfo.Orientation.landscape](./orientation-swift.enum/landscape.md)
  Pages are printed in landscape orientation.
### Initializers
- [init?(rawValue: Int)](./orientation-swift.enum/init%28rawvalue%29.md)

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
- [UIPrintInfo.Duplex](./duplex-swift.enum.md)
  Constants that describe the duplex mode of a selected printer.
- [var jobName: String](./jobname.md)
  The name of the print job.
- [var orientation: UIPrintInfo.Orientation](./orientation-swift.property.md)
  The orientation of the printed content, portrait or landscape.
- [var outputType: UIPrintInfo.OutputType](./outputtype-swift.property.md)
  The kind of printable content.
- [UIPrintInfo.OutputType](./outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [var printerID: String?](./printerid.md)
  An identifier of the printer to use for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/orientation-swift.enum)*