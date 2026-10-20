# AAAttributionError.Code

**Framework**: AdServices  
**Kind**: enum  
**Role**: Enumeration

The error code that the parent class issues.

**Availability**:
- iOS 14.3+
- iPadOS 14.3+
- Mac Catalyst 14.3+
- macOS 11.1+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

```c
enum AAAttributionErrorCode : NSInteger;
```

## Topics

### Creating an error code
- [init?(rawValue: Int)](./code/init%28rawvalue%29.md)
  Creates an error code structure with the specified raw value.
### Determining the cause of an error
- [AAAttributionError.Code.internalError](./code/internalerror.md)
  The server is unable to provide a token because of an internal error.
- [AAAttributionError.Code.networkError](./code/networkerror.md)
  The server is unable to provide a token because the internet isn’t available.
- [AAAttributionError.Code.platformNotSupported](./code/platformnotsupported.md)
  The server is unable to provide a token because of an unsupported operating system.
### Getting information about error codes
- [var localizedDescription: String](../../Swift/error/localizeddescription.md)
  Retrieve the localized description for this error.
### Comparing errors
- [func != ((), ()) -> Bool](../../Swift/noteq%28_,_%29-18co7.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Errors
- [struct AAAttributionError](../aaattributionerror.md)
  The error code that the parent class issues.
- [let AAAttributionErrorDomain: String](../aaattributionerrordomain.md)
  The framework attribution error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adservices/aaattributionerror/code)*