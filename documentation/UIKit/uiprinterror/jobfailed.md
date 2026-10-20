# jobFailed

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

An internal error occurred with the print job.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
static var jobFailed: UIPrintError.Code { get }
```

## See Also

### Accessing error codes
- [UIPrintError.Code](./code.md)
  Constants that specify the print error code.
- [static var notAvailable: UIPrintError.Code](./notavailable.md)
  The device doesn’t support printing.
- [static var noContent: UIPrintError.Code](./nocontent.md)
  UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [static var unknownImageFormat: UIPrintError.Code](./unknownimageformat.md)
  An image is in a format that UIKit doesn’t recognize for printing.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterror/jobfailed)*