# CustomNSError

**Framework**: Foundation  
**Kind**: protocol

A specialized error that provides a domain, error code, and user-info dictionary.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
protocol CustomNSError : Error
```

## Topics

### Instance Properties
- [var errorCode: Int](customnserror/errorcode.md)
- [var errorUserInfo: [String : Any]](customnserror/erroruserinfo.md)
### Type Properties
- [static var errorDomain: String](customnserror/errordomain.md)

## Relationships

### Inherits From
- [Error](../Swift/Error.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
### Conforming Types
- [CocoaError](cocoaerror.md)
- [MachError](macherror.md)
- [POSIXError](posixerror.md)
- [URLError](urlerror.md)

## See Also

- [protocol Error : Sendable](../Swift/Error.md)
  A type representing an error value that can be thrown.
- [class NSError](nserror.md)
  Information about an error condition including a domain, a domain-specific error code, and application-specific information.
- [protocol LocalizedError](localizederror.md)
  A specialized error that provides localized messages describing the error and why it occurred.
- [protocol RecoverableError](recoverableerror.md)
  A specialized error that may be recoverable by presenting several potential recovery options to the user.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/customnserror)*