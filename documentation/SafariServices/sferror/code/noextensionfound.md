# SFError.Code.noExtensionFound

**Framework**: Safari Services  
**Kind**: case  
**Role**: Case

A Content Blocker or Safari app extension with the specified bundle identifier was not found, or the bundle identifier specified an extension that was not owned by you.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.4+
- macOS 10.12+
- visionOS 1.0+

## Declaration

```swift
case noExtensionFound
```

```c
SFErrorNoExtensionFound
```

## See Also

### Error Codes
- [SFError.Code.loadingInterrupted](./loadinginterrupted.md)
  There was an error loading the content blocker extension.
- [SFError.Code.noAttachmentFound](./noattachmentfound.md)
  The Content Blocker extension returned an [`NSExtensionItem`](../../../Foundation/nsextensionitem.md) that did not include an attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferror/code/noextensionfound)*