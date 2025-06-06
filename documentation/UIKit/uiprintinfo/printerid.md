# printerID

**Framework**: UIKit  
**Kind**: property

An identifier of the printer to use for the print job.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var printerID: String? { get set }
```

#### Discussion

This property is set through user selection in the printing user interface. You may provide a printer ID as a hint (for example, the last printer used from a particular print job). The default value is `nil`.

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
- [UIPrintInfo.OutputType](uiprintinfo/outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/printerid)*