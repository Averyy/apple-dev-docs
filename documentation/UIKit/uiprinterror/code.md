# UIPrintError.Code

**Framework**: UIKit  
**Kind**: enum

Constants that specify the print error code.

**Availability**:
- iOS 4.2+
- iPadOS 4.2+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error codes
- [UIPrintError.Code.notAvailable](uiprinterror/code/notavailable.md)
  The device doesn’t support printing.
- [UIPrintError.Code.noContent](uiprinterror/code/nocontent.md)
  UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [UIPrintError.Code.unknownImageFormat](uiprinterror/code/unknownimageformat.md)
  An image is in a format that UIKit doesn’t recognize for printing.
- [UIPrintError.Code.jobFailed](uiprinterror/code/jobfailed.md)
  An internal error occurred with the print job.
### Global variables
- [Print error global variables](print-error-global-variables.md)
  Global variables associated with print errors.
### Initializers
- [init?(rawValue: Int)](uiprinterror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [let UIPrintErrorDomain: String](uiprinterrordomain.md)
  The string constant that defines the UIKit printing error domain.
- [struct UIPrintError](uiprinterror.md)
  A structure that contains information about a printing error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterror/code)*