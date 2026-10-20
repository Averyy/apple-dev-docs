# UIMailConversationContext.MailEntry.Kind

**Framework**: UIKit  
**Kind**: enum  
**Role**: Enumeration

A set of categories for an email.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+

## Declaration

```swift
enum Kind
```

```c
enum UIMailConversationEntryKind : NSInteger;
```

## Topics

### Kinds of email
- [UIMailConversationContext.MailEntry.Kind.news](./kind-swift.enum/news.md)
  The email is related to news or current events.
- [UIMailConversationContext.MailEntry.Kind.none](./kind-swift.enum/none.md)
  The email does not fit in a specific category.
- [UIMailConversationContext.MailEntry.Kind.personal](./kind-swift.enum/personal.md)
  The email is personal correspondence.
- [UIMailConversationContext.MailEntry.Kind.promotion](./kind-swift.enum/promotion.md)
  The email contains a promotional offer.
- [UIMailConversationContext.MailEntry.Kind.social](./kind-swift.enum/social.md)
  The email is related to social media.
- [UIMailConversationContext.MailEntry.Kind.transaction](./kind-swift.enum/transaction.md)
  The email is related to a purchase or transaction.
### Initializers
- [init?(rawValue: Int)](./kind-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../../Swift/bitwisecopyable.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [RawRepresentable](../../../Swift/rawrepresentable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Categorizing the email
- [var kind: UIMailConversationContext.MailEntry.Kind](./kind-swift.property.md)
  An item that reflects the category that describes an email.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimailconversationcontext/mailentry/kind-swift.enum)*