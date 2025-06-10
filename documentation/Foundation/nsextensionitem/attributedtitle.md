# attributedTitle

**Framework**: Foundation  
**Kind**: property

An optional title for the item.

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
var attributedTitle: NSAttributedString? { get set }
```

#### Discussion

> ❗ **Important**:  Alternatively, you can set attributed content in the [`userInfo`](nsextensionitem/userinfo.md) dictionary using the [`NSExtensionItemAttributedTitleKey`](nsextensionitemattributedtitlekey.md) key. However, setting the [`userInfo`](nsextensionitem/userinfo.md) dictionary after setting [`attributedTitle`](nsextensionitem/attributedtitle.md) overrides this property.

## See Also

- [App Extension Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)
- [var userInfo: [AnyHashable : Any]?](nsextensionitem/userinfo.md)
  An optional dictionary of keys and values corresponding to the extension item’s properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitem/attributedtitle)*