# items

**Framework**: UIKit  
**Kind**: property

The dynamic items connected by the attachment behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var items: [any UIDynamicItem] { get }
```

#### Discussion

Contains two elements when used for an attachment behavior of type [`UIAttachmentBehavior.AttachmentType.items`](uiattachmentbehavior/attachmenttype/items.md); contains one element when used for an attachment behavior of type [`UIAttachmentBehavior.AttachmentType.anchor`](uiattachmentbehavior/attachmenttype/anchor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/items)*