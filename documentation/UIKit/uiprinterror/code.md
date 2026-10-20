# UIPrintError.Code

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

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

```c
enum UIPrintErrorCode : NSInteger;
```

## Topics

### Error codes
- [UIPrintError.Code.notAvailable](./code/notavailable.md)
  The device doesn’t support printing.
- [UIPrintError.Code.noContent](./code/nocontent.md)
  UIKit hasn’t assigned a print formatter, page renderer, or printing item to print.
- [UIPrintError.Code.unknownImageFormat](./code/unknownimageformat.md)
  An image is in a format that UIKit doesn’t recognize for printing.
- [UIPrintError.Code.jobFailed](./code/jobfailed.md)
  An internal error occurred with the print job.
### Global variables
- [Print error global variables](../print-error-global-variables.md)
  Global variables associated with print errors.
### Initializers
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Handling printing errors
- [let UIPrintErrorDomain: String](../uiprinterrordomain.md)
  The string constant that defines the UIKit printing error domain.
- [struct UIPrintError](../uiprinterror.md)
  A structure that contains information about a printing error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiprinterror/code)*