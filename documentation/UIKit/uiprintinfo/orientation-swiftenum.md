# UIPrintInfo.Orientation

**Framework**: UIKit  
**Kind**: enum

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

#### Overview

You use these constants when setting the value of the [`orientation`](uiprintinfo/orientation-swift.property.md) property of a `UIPrintInfo` object.

> **Note**:  UIKit ignores the [`orientation`](uiprintinfo/orientation-swift.property.md) property when printable content is assigned to the `printingItem` or `printingItems` properties of the shared [`UIPrintInteractionController`](uiprintinteractioncontroller.md) object. It determines the orientation based on the type of content.

 UIKit ignores the [`orientation`](uiprintinfo/orientation-swift.property.md) property when printable content is assigned to the `printingItem` or `printingItems` properties of the shared [`UIPrintInteractionController`](uiprintinteractioncontroller.md) object. It determines the orientation based on the type of content.

## Topics

### Constants
- [UIPrintInfo.Orientation.portrait](uiprintinfo/orientation-swift.enum/portrait.md)
  Pages are printed in portrait orientation.
- [UIPrintInfo.Orientation.landscape](uiprintinfo/orientation-swift.enum/landscape.md)
  Pages are printed in landscape orientation.
### Initializers
- [init?(rawValue: Int)](uiprintinfo/orientation-swift.enum/init(rawvalue:).md)

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
- [var outputType: UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.property.md)
  The kind of printable content.
- [UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [var printerID: String?](uiprintinfo/printerid.md)
  An identifier of the printer to use for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/orientation-swift.enum)*