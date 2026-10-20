# UIMessageConversationContext.MessageEntry.DataKind

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A list of options that represent the kinds of data a message can contain.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
enum DataKind
```

```c
enum UIMessageConversationEntryDataKind : NSInteger;
```

## Topics

### Kinds of data in a message
- [UIMessageConversationContext.MessageEntry.DataKind.attachment](./datakind-swift.enum/attachment.md)
  The message contains an attachment, such as an image or file.
- [UIMessageConversationContext.MessageEntry.DataKind.other](./datakind-swift.enum/other.md)
  The message contains other data, such as data that represents a sticker or a payment.
- [UIMessageConversationContext.MessageEntry.DataKind.text](./datakind-swift.enum/text.md)
  The message contains text.
### Initializers
- [init?(rawValue: Int)](./datakind-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Categorizing the entry
- [var dataKind: UIMessageConversationContext.MessageEntry.DataKind](./datakind-swift.property.md)
  An item that represents the kind of data the message contains.
- [var wasSentBySelf: Bool](./wassentbyself.md)
  A Boolean value that indicates whether the current user sent the message.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimessageconversationcontext/messageentry/datakind-swift.enum)*