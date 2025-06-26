# SFError.Code

**Framework**: Safari Services  
**Kind**: enum

Messages that describe a content blocker or Safari app extension error.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
enum Code
```

## Topics

### Error Codes
- [SFError.Code.loadingInterrupted](sferrorcode/loadinginterrupted.md)
  There was an error loading the content blocker extension.
- [SFError.Code.noAttachmentFound](sferrorcode/noattachmentfound.md)
  The Content Blocker extension returned an [`NSExtensionItem`](https://developer.apple.com/documentation/Foundation/NSExtensionItem) that did not include an attachment.
- [SFError.Code.noExtensionFound](sferrorcode/noextensionfound.md)
  A Content Blocker or Safari app extension with the specified bundle identifier was not found, or the bundle identifier specified an extension that was not owned by you.
### Enumeration Cases
- [SFError.Code.internalError](sferrorcode/internalerror.md)
- [SFError.Code.missingEntitlement](sferrorcode/missingentitlement.md)
### Initializers
- [init?(rawValue: Int)](sferrorcode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct SFError](sferror.md)
  A content blocker or Safari app extension error.
- [let SFErrorDomain: String](sferrordomain.md)
  The domain for content blocker or Safari app extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferrorcode)*