# jobName

**Framework**: UIKit  
**Kind**: property

The name of the print job.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var jobName: String { get set }
```

#### Discussion

The name of the print job appears in the Print Center when the job is printing. An app should set this property to a name appropriate to the content that’s printing. The default job name is the app name.

## See Also

- [var duplex: UIPrintInfo.Duplex](uiprintinfo/duplex-swift.property.md)
  The duplex mode to use for the print job.
- [UIPrintInfo.Duplex](uiprintinfo/duplex-swift.enum.md)
  Constants that describe the duplex mode of a selected printer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/jobname)*