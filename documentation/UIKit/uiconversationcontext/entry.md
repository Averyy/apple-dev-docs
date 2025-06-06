# UIConversationContext.Entry

**Framework**: UIKit  
**Kind**: class

A base class that represents a message in a conversation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class Entry
```

## Topics

### Identifying the entry
- [var entryIdentifier: String](uiconversationcontext/entry/entryidentifier.md)
  A string that uniquely identifies this specific entry in the conversation.
- [var replyThreadIdentifier: String?](uiconversationcontext/entry/replythreadidentifier.md)
  An optional string that identifies another message in a conversation, when this entry is a reply to that message.
### Getting entry details
- [var text: String](uiconversationcontext/entry/text.md)
  A string that contains the message’s text.
- [var sentDate: Date](uiconversationcontext/entry/sentdate.md)
  A date that notes when the sender added the message to the conversation.
### Identifying entry participants
- [var senderIdentifier: String](uiconversationcontext/entry/senderidentifier.md)
  A string that identifies the message’s sender.
- [var primaryRecipientIdentifiers: Set<String>](uiconversationcontext/entry/primaryrecipientidentifiers.md)
  A set of strings that identifies the primary recipients of the message.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIMailConversationContext.MailEntry](uimailconversationcontext/mailentry.md)
- [UIMessageConversationContext.MessageEntry](uimessageconversationcontext/messageentry.md)
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
- [class UIMailConversationContext](uimailconversationcontext.md)
  A class that represents an email conversation.
- [UIMailConversationContext.MailEntry](uimailconversationcontext/mailentry.md)
  A class that represents a specific email in an email thread.
- [class UIMessageConversationContext](uimessageconversationcontext.md)
  A class that represents a message conversation.
- [UIMessageConversationContext.MessageEntry](uimessageconversationcontext/messageentry.md)
  A class that represents a message in a message conversation.
- [class UIInputSuggestion](uiinputsuggestion.md)
  A base class you use to handle suggestions from the keyboard or system.
- [class UISmartReplySuggestion](uismartreplysuggestion.md)
  A class you use to handle a Smart Reply suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconversationcontext/entry)*