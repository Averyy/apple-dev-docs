# SFError.Code.noExtensionFound

**Framework**: Safari Services  
**Kind**: case

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

## See Also

- [SFError.Code.loadingInterrupted](sferrorcode/loadinginterrupted.md)
  There was an error loading the content blocker extension.
- [SFError.Code.noAttachmentFound](sferrorcode/noattachmentfound.md)
  The Content Blocker extension returned an [`NSExtensionItem`](https://developer.apple.com/documentation/Foundation/NSExtensionItem) that did not include an attachment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/safariservices/sferrorcode/noextensionfound)*