# attributedTitle

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedTitle;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSAttributedString * attributedTitle;
```

#### Discussion

> ❗ **Important**:  Alternatively, you can set attributed content in the [`userInfo`](./userinfo.md) dictionary using the [`NSExtensionItemAttributedTitleKey`](../nsextensionitemattributedtitlekey.md) key. However, setting the [`userInfo`](./userinfo.md) dictionary after setting [`attributedTitle`](./attributedtitle.md) overrides this property.

## See Also

### Related Documentation
- [App Extension Programming Guide](https://developer.apple.com/library/archive/documentation/General/Conceptual/ExtensibilityPG/index.html#//apple_ref/doc/uid/TP40014214)
### Identifying the Item
- [var userInfo: [AnyHashable : Any]?](./userinfo.md)
  An optional dictionary of keys and values corresponding to the extension item’s properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitem/attributedtitle)*