# SFError.Code.loadingInterrupted

**Framework**: Safari Services  
**Kind**: case  
**Role**: Case

There was an error loading the content blocker extension.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
case loadingInterrupted
```

```c
SFErrorLoadingInterrupted
```

## See Also

### Error Codes
- [SFError.Code.noAttachmentFound](./noattachmentfound.md)
  The Content Blocker extension returned an [`NSExtensionItem`](../../../Foundation/nsextensionitem.md) that did not include an attachment.
- [SFError.Code.noExtensionFound](./noextensionfound.md)
  A Content Blocker or Safari app extension with the specified bundle identifier was not found, or the bundle identifier specified an extension that was not owned by you.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferror/code/loadinginterrupted)*