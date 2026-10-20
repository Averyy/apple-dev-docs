# outputType

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The kind of printable content.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var outputType: UIPrintInfo.OutputType { get set }
```

```objc
@property (nonatomic) UIPrintInfoOutputType outputType;
```

#### Discussion

The output type can be general, photo, or grayscale. An application can set this property to a value thats appropriate to the printable content. The default is [`UIPrintInfo.OutputType.general`](./outputtype-swift.enum/general.md).  See the descriptions of the [`UIPrintInfo.OutputType`](./outputtype-swift.enum.md) constants for more information.

The output type controls the quality and default paper size used in printing. For example, if your application only prints black text, setting this property to [`UIPrintInfo.OutputType.grayscale`](./outputtype-swift.enum/grayscale.md) can result in better performance in many cases. See [`UIPrintPaper`](../uiprintpaper.md) for details.

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
- [UIPrintInfo.Orientation](./orientation-swift.enum.md)
  Constants that describe the orientation of printing on a page.
- [UIPrintInfo.OutputType](./outputtype-swift.enum.md)
  Constants that describe the output type, which is an indication of the type of content the app is drawing or providing.
- [var printerID: String?](./printerid.md)
  An identifier of the printer to use for the print job.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprintinfo/outputtype-swift.property)*