# SFError

**Framework**: Safari Services  
**Kind**: struct

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
- [static var loadingInterrupted: SFError.Code](sferror/loadinginterrupted.md)
- [static var noAttachmentFound: SFError.Code](sferror/noattachmentfound.md)
- [static var noExtensionFound: SFError.Code](sferror/noextensionfound.md)
- [SFError.Code](sferror/code.md)
  Messages that describe a content blocker or Safari app extension error.
### Error Domain
- [let SFErrorDomain: String](sferrordomain.md)
  The domain for content blocker or Safari app extension errors.
### Type Properties
- [static var errorDomain: String](sferror/errordomain.md)

## Relationships

### Conforms To
- [CustomNSError](../Foundation/CustomNSError.md)
- [Equatable](../Swift/Equatable.md)
- [Error](../Swift/Error.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [SFError.Code](sferror/code.md)
  Messages that describe a content blocker or Safari app extension error.
- [let SFErrorDomain: String](sferrordomain.md)
  The domain for content blocker or Safari app extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferror)*