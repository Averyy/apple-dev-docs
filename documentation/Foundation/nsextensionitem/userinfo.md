# userInfo

**Framework**: Foundation  
**Kind**: property

An optional dictionary of keys and values corresponding to the extension item’s properties.

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
var userInfo: [AnyHashable : Any]? { get set }
```

#### Discussion

If applicable to a particular extension type, additional information may be available in the `userInfo` dictionary. For example, in the context of an Action extension, the `userInfo` dictionary may contain values for the keys [`NSExtensionItemAttachmentsKey`](nsextensionitemattachmentskey.md), [`NSExtensionItemAttributedContentTextKey`](nsextensionitemattributedcontenttextkey.md), and [`NSExtensionItemAttributedTitleKey`](nsextensionitemattributedtitlekey.md).

> ❗ **Important**:  Setting the [`userInfo`](nsextensionitem/userinfo.md) dictionary after setting [`attachments`](nsextensionitem/attachments.md), [`attributedContentText`](nsextensionitem/attributedcontenttext.md), or [`attributedTitle`](nsextensionitem/attributedtitle.md) overrides those properties.

## See Also

- [var attributedTitle: NSAttributedString?](nsextensionitem/attributedtitle.md)
  An optional title for the item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitem/userinfo)*