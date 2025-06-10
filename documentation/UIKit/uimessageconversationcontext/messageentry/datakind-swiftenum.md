# UIMessageConversationContext.MessageEntry.DataKind

**Framework**: UIKit  
**Kind**: enum

A list of options that represent the kinds of data a message can contain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
enum DataKind
```

## Topics

### Kinds of data in a message
- [UIMessageConversationContext.MessageEntry.DataKind.attachment](uimessageconversationcontext/messageentry/datakind-swift.enum/attachment.md)
  The message contains an attachment, such as an image or file.
- [UIMessageConversationContext.MessageEntry.DataKind.other](uimessageconversationcontext/messageentry/datakind-swift.enum/other.md)
  The message contains other data, such as data that represents a sticker or a payment.
- [UIMessageConversationContext.MessageEntry.DataKind.text](uimessageconversationcontext/messageentry/datakind-swift.enum/text.md)
  The message contains text.
### Initializers
- [init?(rawValue: Int)](uimessageconversationcontext/messageentry/datakind-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var dataKind: UIMessageConversationContext.MessageEntry.DataKind](uimessageconversationcontext/messageentry/datakind-swift.property.md)
  An item that represents the kind of data the message contains.
- [var wasSentBySelf: Bool](uimessageconversationcontext/messageentry/wassentbyself.md)
  A Boolean value that indicates whether the current user sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimessageconversationcontext/messageentry/datakind-swift.enum)*