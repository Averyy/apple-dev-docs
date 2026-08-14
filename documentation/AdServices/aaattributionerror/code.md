# AAAttributionError.Code

**Framework**: AdServices  
**Kind**: enum

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

## Topics

### Creating an error code
- [init?(rawValue: Int)](aaattributionerror/code/init(rawvalue:).md)
  Creates an error code structure with the specified raw value.
### Determining the cause of an error
- [AAAttributionError.Code.internalError](aaattributionerror/code/internalerror.md)
  The server is unable to provide a token because of an internal error.
- [AAAttributionError.Code.networkError](aaattributionerror/code/networkerror.md)
  The server is unable to provide a token because the internet isn’t available.
- [AAAttributionError.Code.platformNotSupported](aaattributionerror/code/platformnotsupported.md)
  The server is unable to provide a token because of an unsupported operating system.
### Getting information about error codes
- [var localizedDescription: String](../swift/error/localizeddescription.md)
  Retrieve the localized description for this error.
### Comparing errors
- [func != ((), ()) -> Bool](../swift/!=(_:_:)-18co7.md)
  Returns a Boolean value indicating whether any corresponding components of the two tuples are not equal.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [struct AAAttributionError](aaattributionerror.md)
  The error code that the parent class issues.
- [let AAAttributionErrorDomain: String](aaattributionerrordomain.md)
  The framework attribution error domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/adservices/aaattributionerror/code)*