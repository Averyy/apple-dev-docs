# items

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The dynamic items connected by the attachment behavior.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var items: [any UIDynamicItem] { get }
```

```objc
@property (nonatomic, copy, readonly) NSArray<id<UIDynamicItem>> * items;
```

#### Discussion

Contains two elements when used for an attachment behavior of type [`UIAttachmentBehavior.AttachmentType.items`](./attachmenttype/items.md); contains one element when used for an attachment behavior of type [`UIAttachmentBehavior.AttachmentType.anchor`](./attachmenttype/anchor.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiattachmentbehavior/items)*