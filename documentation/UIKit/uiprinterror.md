# UIPrintError

**Framework**: UIKit  
**Kind**: struct

A structure that contains information about a printing error.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
struct UIPrintError
```

## Topics

### Accessing error codes
- [UIPrintError.Code](uiprinterror/code.md)
  Constants that specify the print error code.
- [static var notAvailable: UIPrintError.Code](uiprinterror/notavailable.md)
  The device doesn’t support printing.
- [static var noContent: UIPrintError.Code](uiprinterror/nocontent.md)
  UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [static var unknownImageFormat: UIPrintError.Code](uiprinterror/unknownimageformat.md)
  An image is in a format that UIKit doesn’t recognize for printing.
- [static var jobFailed: UIPrintError.Code](uiprinterror/jobfailed.md)
  An internal error occurred with the print job.
### Getting error information
- [static var errorDomain: String](uiprinterror/errordomain.md)
  The printing error domain.

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let UIPrintErrorDomain: String](uiprinterrordomain.md)
  The string constant that defines the UIKit printing error domain.
- [UIPrintError.Code](uiprinterror/code.md)
  Constants that specify the print error code.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterror)*