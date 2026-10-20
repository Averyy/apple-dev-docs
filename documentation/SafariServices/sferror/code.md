# SFError.Code

**Framework**: Safari Services  
**Kind**: enum  
**Role**: Enumeration

Messages that describe a content blocker or Safari app extension error.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
enum Code
```

*Mac Catalyst, macOS*

```swift
enum SFErrorCode
```

```c
enum SFErrorCode : NSInteger;
```

## Topics

### Error Codes
- [SFError.Code.loadingInterrupted](./code/loadinginterrupted.md)
  There was an error loading the content blocker extension.
- [SFError.Code.noAttachmentFound](./code/noattachmentfound.md)
  The Content Blocker extension returned an [`NSExtensionItem`](../../Foundation/nsextensionitem.md) that did not include an attachment.
- [SFError.Code.noExtensionFound](./code/noextensionfound.md)
  A Content Blocker or Safari app extension with the specified bundle identifier was not found, or the bundle identifier specified an extension that was not owned by you.
### Enumeration Cases
- [SFError.Code.internalError](./code/internalerror.md)
- [SFError.Code.maximumAttemptsExceeded](./code/maximumattemptsexceeded.md)
- [SFError.Code.missingEntitlement](./code/missingentitlement.md)
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

### Miscellaneous errors
- [struct SFError](../sferror.md)
  A content blocker or Safari app extension error.
- [let SFErrorDomain: String](../sferrordomain.md)
  The domain for content blocker or Safari app extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferror/code)*