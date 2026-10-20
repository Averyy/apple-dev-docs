# attachments

**Framework**: Quick Look UI  
**Kind**: property  
**Role**: Instance Property

The attachments for a preview reply that provide additional data for the system to display the preview.

**Availability**:
- macOS 12.0+

## Declaration

```swift
var attachments: [String : QLPreviewReplyAttachment] { get set }
```

```objc
@property (copy) NSDictionary<NSString *,QLPreviewReplyAttachment *> * attachments;
```

#### Discussion

When providing an HTML reply, use the string associated with the [`QLPreviewReplyAttachment`](../qlpreviewreplyattachment.md) prefixed with `cid:` to reference the content within the HTML.

## See Also

### Inspecting a preview reply
- [var title: String](./title.md)
  The title for the system to display with the preview.
- [var stringEncoding: String.Encoding](./stringencoding-8ahm8.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/quicklookui/qlpreviewreply/attachments)*