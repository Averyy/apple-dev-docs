# UIDocumentBrowserError.Code

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

The error codes for document browser errors.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum UIDocumentBrowserErrorCode : NSInteger;
```

## Topics

### Error codes
- [UIDocumentBrowserError.Code.generic](./code/generic.md)
  An unspecified error.
- [UIDocumentBrowserError.Code.noLocationAvailable](./code/nolocationavailable.md)
  An error indicating that no location exists.
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

### Related Documentation
- [class UIDocumentBrowserViewController](../uidocumentbrowserviewcontroller.md)
  A view controller for browsing and performing actions on documents that you store locally and in the cloud.
### Handling errors
- [struct UIDocumentBrowserError](../uidocumentbrowsererror.md)
  A structure that contains information about document browser errors.
- [let UIDocumentBrowserErrorDomain: String](../uidocumentbrowsererrordomain.md)
  The error domain for document browser errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocumentbrowsererror/code)*