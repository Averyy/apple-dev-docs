# UIMessageConversationContext.MessageEntry

**Framework**: UIKit  
**Kind**: class

A class that represents a message in a message conversation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class MessageEntry
```

## Mentions

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)

## Topics

### Categorizing the entry
- [var dataKind: UIMessageConversationContext.MessageEntry.DataKind](uimessageconversationcontext/messageentry/datakind-swift.property.md)
  An item that represents the kind of data the message contains.
- [UIMessageConversationContext.MessageEntry.DataKind](uimessageconversationcontext/messageentry/datakind-swift.enum.md)
  A list of options that represent the kinds of data a message can contain.
- [var wasSentBySelf: Bool](uimessageconversationcontext/messageentry/wassentbyself.md)
  A Boolean value that indicates whether the current user sent the message.

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

## See Also

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)
  Generate reply suggestions by using Apple Intelligence and put selected text into your text UI.
- [class UIConversationContext](uiconversationcontext.md)
  A base class that represents a conversation between participants, such as in an email or messaging app.
- [UIConversationContext.Entry](uiconversationcontext/entry.md)
  A base class that represents a message in a conversation.
- [class UIMailConversationContext](uimailconversationcontext.md)
  A class that represents an email conversation.
- [UIMailConversationContext.MailEntry](uimailconversationcontext/mailentry.md)
  A class that represents a specific email in an email thread.
- [class UIMessageConversationContext](uimessageconversationcontext.md)
  A class that represents a message conversation.
- [class UIInputSuggestion](uiinputsuggestion.md)
  A base class you use to handle suggestions from the keyboard or system.
- [class UISmartReplySuggestion](uismartreplysuggestion.md)
  A class you use to handle a Smart Reply suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimessageconversationcontext/messageentry)*