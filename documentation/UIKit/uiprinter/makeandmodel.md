# makeAndModel

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A string that contains the manufacturer’s name and the model name of the printer.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var makeAndModel: String? { get }
```

```objc
@property (copy, readonly, nullable) NSString * makeAndModel;
```

## Discussion

The string in this property is provided by the printer and usually consists of the manufacturer’s name, the model name of the printer, and the model number of the printer.

For printers you create yourself using the [`init(url:)`](./init%28url%29-1mibn.md) method, the value of this property is `nil` until you successfully connect to the printer using the [`contactPrinter(_:)`](./contactprinter%28_%29.md) method.

## See Also

### Getting the printer information
- [var displayName: String](./displayname.md)
  The human-readable printer name.
- [var displayLocation: String?](./displaylocation.md)
  The human-readable text that describes the location of the printer.
- [var supportedJobTypes: UIPrinter.JobTypes](./supportedjobtypes.md)
  The capabilities of the printer.
- [UIPrinter.JobTypes](./jobtypes.md)
  Constants that indicate the types of jobs that the printer supports.
- [var supportsColor: Bool](./supportscolor.md)
  A Boolean value that indicates whether the printer supports color printing.
- [var supportsDuplex: Bool](./supportsduplex.md)
  A Boolean value that indicates whether the printer supports printing on both sides of a sheet of paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinter/makeandmodel)*