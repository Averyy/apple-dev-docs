# supportsColor

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the printer supports color printing.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var supportsColor: Bool { get }
```

```objc
@property (readonly) BOOL supportsColor;
```

#### Discussion

The value of this property is [`true`](../../Swift/true.md) if the printer supports color printing or [`false`](../../Swift/false.md) if it does not. For printers you create yourself using the [`init(url:)`](./init%28url%29-1mibn.md) method, the value of this property is [`false`](../../Swift/false.md) until you successfully connect to the printer using the [`contactPrinter(_:)`](./contactprinter%28_%29.md) method.

## See Also

### Getting the printer information
- [var displayName: String](./displayname.md)
  The human-readable printer name.
- [var displayLocation: String?](./displaylocation.md)
  The human-readable text that describes the location of the printer.
- [var makeAndModel: String?](./makeandmodel.md)
  A string that contains the manufacturer’s name and the model name of the printer.
- [var supportedJobTypes: UIPrinter.JobTypes](./supportedjobtypes.md)
  The capabilities of the printer.
- [UIPrinter.JobTypes](./jobtypes.md)
  Constants that indicate the types of jobs that the printer supports.
- [var supportsDuplex: Bool](./supportsduplex.md)
  A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/supportscolor)*