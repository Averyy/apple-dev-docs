# UIMailConversationContext.MailEntry

**Framework**: UIKit  
**Kind**: class

A class that represents a specific email in an email thread.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class MailEntry
```

## Mentions

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)

## Topics

### Categorizing the email
- [var kind: UIMailConversationContext.MailEntry.Kind](uimailconversationcontext/mailentry/kind-swift.property.md)
  An item that reflects the category that describes an email.
- [UIMailConversationContext.MailEntry.Kind](uimailconversationcontext/mailentry/kind-swift.enum.md)
  A set of categories for an email.
### Identifying secondary recipients
- [var responseSecondaryRecipientIdentifiers: Set<String>](uimailconversationcontext/mailentry/responsesecondaryrecipientidentifiers.md)
  A set of strings that identifies the secondary recipients of the message, such as those in CC or BCC messages.

## Relationships

### Inherits From
- [UIConversationContext.Entry](uiconversationcontext/entry.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)
  Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [class UIConversationContext](uiconversationcontext.md)
  A base class that represents a conversation between participants, such as in an email or messaging app.
- [UIConversationContext.Entry](uiconversationcontext/entry.md)
  A base class that represents a message in a conversation.
- [class UIMailConversationContext](uimailconversationcontext.md)
  A class that represents an email conversation.
- [class UIMessageConversationContext](uimessageconversationcontext.md)
  A class that represents a message conversation.
- [UIMessageConversationContext.MessageEntry](uimessageconversationcontext/messageentry.md)
  A class that represents a message in a message conversation.
- [class UIInputSuggestion](uiinputsuggestion.md)
  A base class you use to handle suggestions from the keyboard or system.
- [class UISmartReplySuggestion](uismartreplysuggestion.md)
  A class you use to handle a Smart Reply suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimailconversationcontext/mailentry)*