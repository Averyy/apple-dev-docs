# orientation

**Framework**: Uikit  
**Kind**: property

The orientation of the printed content, portrait or landscape.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var orientation: UIPrintInfo.Orientation { get set }
```

#### Discussion

An application can set this property to a value thats appropriate to the printable content or it can put up a user interface that enables users to pick the printing orientation. The default value is [`UIPrintInfo.Orientation.portrait`](uiprintinfo/orientation-swift.enum/portrait.md). See the descriptions of the [`UIPrintInfo.Orientation`](uiprintinfo/orientation-swift.enum.md) constants for more information.

> **Note**:  UIKit ignores this property when printable content is assigned to the `printingItem` or `printingItems` properties of the shared [`UIPrintInteractionController`](uiprintinteractioncontroller.md) object. It determines the orientation based on the type of content.

## See Also

- [var duplex: UIPrintInfo.Duplex](uiprintinfo/duplex-swift.property.md)
  The duplex mode to use for the print job.
- [UIPrintInfo.Duplex](uiprintinfo/duplex-swift.enum.md)
  Constants that describe the duplex mode of a selected printer.
- [var jobName: String](uiprintinfo/jobname.md)
  The name of the print job.
- [UIPrintInfo.Orientation](uiprintinfo/orientation-swift.enum.md)
  Constants that describe the orientation of printing on a page.
- [var outputType: UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.property.md)
  The kind of printable content.
- [UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [var printerID: String?](uiprintinfo/printerid.md)
  An identifier of the printer to use for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/orientation-swift.property)*