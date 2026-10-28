# attachments

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

An optional array of media data associated with the extension item.

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
var attachments: [NSItemProvider]? { get set }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, nullable) NSArray<NSItemProvider *> * attachments;
```

*macOS*

```objc
@property (atomic, copy, nullable) NSArray<NSItemProvider *> * attachments;
```

## Discussion

Populate this array with images, videos, URLs, and so on. It’s not meant to be an array of alternative data formats or types, but is instead a collection to include in a social media post, for example. These items are always typed [`NSItemProvider`](../nsitemprovider.md).

> ❗ **Important**:  Alternatively, you can set attachments in the [`userInfo`](./userinfo.md) dictionary using the [`NSExtensionItemAttachmentsKey`](../nsextensionitemattachmentskey.md) key. However, setting the [`userInfo`](./userinfo.md) dictionary after setting [`attachments`](./attachments.md) will override this property.

## See Also

### Item Contents
- [var attributedContentText: NSAttributedString?](./attributedcontenttext.md)
  An optional string describing the extension item content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsextensionitem/attachments)*