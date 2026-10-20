# attributedContentText

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSAttributedString * attributedContentText;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSAttributedString * attributedContentText;
```

#### Discussion

> ❗ **Important**:  Alternatively, you can set attributed content in the [`userInfo`](./userinfo.md) dictionary using the [`NSExtensionItemAttributedContentTextKey`](../nsextensionitemattributedcontenttextkey.md) key. However, setting the [`userInfo`](./userinfo.md) dictionary after setting [`attributedContentText`](./attributedcontenttext.md) overrides this property.

## See Also

### Item Contents
- [var attachments: [NSItemProvider]?](./attachments.md)
  An optional array of media data associated with the extension item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitem/attributedcontenttext)*