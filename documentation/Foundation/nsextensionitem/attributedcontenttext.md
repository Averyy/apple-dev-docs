# attributedContentText

**Framework**: Foundation  
**Kind**: property

An optional string describing the extension item content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
@NSCopying
var attributedContentText: NSAttributedString? { get set }
```

#### Discussion

> ❗ **Important**:  Alternatively, you can set attributed content in the [`userInfo`](nsextensionitem/userinfo.md) dictionary using the [`NSExtensionItemAttributedContentTextKey`](nsextensionitemattributedcontenttextkey.md) key. However, setting the [`userInfo`](nsextensionitem/userinfo.md) dictionary after setting [`attributedContentText`](nsextensionitem/attributedcontenttext.md) overrides this property.

 Alternatively, you can set attributed content in the [`userInfo`](nsextensionitem/userinfo.md) dictionary using the [`NSExtensionItemAttributedContentTextKey`](nsextensionitemattributedcontenttextkey.md) key. However, setting the [`userInfo`](nsextensionitem/userinfo.md) dictionary after setting [`attributedContentText`](nsextensionitem/attributedcontenttext.md) overrides this property.

## See Also

- [var attachments: [NSItemProvider]?](nsextensionitem/attachments.md)
  An optional array of media data associated with the extension item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitem/attributedcontenttext)*