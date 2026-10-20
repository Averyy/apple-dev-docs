# SFError

**Framework**: Safari Services  
**Kind**: struct  
**Role**: Structure

A content blocker or Safari app extension error.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- visionOS 1.0+

## Declaration

```swift
struct SFError
```

## Topics

### Error Codes
- [static var loadingInterrupted: SFError.Code](./sferror/loadinginterrupted.md)
- [static var noAttachmentFound: SFError.Code](./sferror/noattachmentfound.md)
- [static var noExtensionFound: SFError.Code](./sferror/noextensionfound.md)
- [SFError.Code](./sferror/code.md)
  Messages that describe a content blocker or Safari app extension error.
### Error Domain
- [static var errorDomain: String](./sferror/errordomain.md)
- [let SFErrorDomain: String](./sferrordomain.md)
  The domain for content blocker or Safari app extension errors.
### Type Properties
- [static var internalError: SFError.Code](./sferror/internalerror.md)
- [static var maximumAttemptsExceeded: SFError.Code](./sferror/maximumattemptsexceeded.md)
- [static var missingEntitlement: SFError.Code](./sferror/missingentitlement.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/customnserror.md)
- [Equatable](../Swift/equatable.md)
- [Error](../Swift/error.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Miscellaneous errors
- [SFError.Code](./sferror/code.md)
  Messages that describe a content blocker or Safari app extension error.
- [let SFErrorDomain: String](./sferrordomain.md)
  The domain for content blocker or Safari app extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferror)*