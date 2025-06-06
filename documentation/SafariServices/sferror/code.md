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
- [SFError.Code.loadingInterrupted](sferror/code/loadinginterrupted.md)
  There was an error loading the content blocker extension.
- [SFError.Code.noAttachmentFound](sferror/code/noattachmentfound.md)
  The Content Blocker extension returned an [`NSExtensionItem`](https://developer.apple.com/documentation/Foundation/NSExtensionItem) that did not include an attachment.
- [SFError.Code.noExtensionFound](sferror/code/noextensionfound.md)
  A Content Blocker or Safari app extension with the specified bundle identifier was not found, or the bundle identifier specified an extension that was not owned by you.
### Initializers
- [init?(rawValue: Int)](sferror/code/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct SFError](sferror.md)
  A content blocker or Safari app extension error.
- [let SFErrorDomain: String](sferrordomain.md)
  The domain for content blocker or Safari app extension errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferror/code)*