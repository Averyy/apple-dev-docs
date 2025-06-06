# UIConversationContext

**Framework**: UIKit  
**Kind**: class

A base class that represents a conversation between participants, such as in an email or messaging app.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class UIConversationContext
```

## Topics

### Identifying the conversation
- [var threadIdentifier: String](uiconversationcontext/threadidentifier.md)
  A string that uniquely identifies a conversation. This identifier is persistent for the life of the conversation.
### Getting messages from the conversation
- [var entries: [UIConversationContext.Entry]](uiconversationcontext/entries.md)
  An array of messages in the conversation.
### Getting conversation participants
- [var selfIdentifiers: Set<String>](uiconversationcontext/selfidentifiers.md)
  A set of strings that identifies the active person in the conversation on the current device.
- [var responsePrimaryRecipientIdentifiers: Set<String>](uiconversationcontext/responseprimaryrecipientidentifiers.md)
  A dictionary that relates participant identifiers to participant names.
- [var participantNameByIdentifier: [String : PersonNameComponents]](uiconversationcontext/participantnamebyidentifier.md)
  A dictionary that relates participant identifiers to participant names.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIMailConversationContext](uimailconversationcontext.md)
- [UIMessageConversationContext](uimessageconversationcontext.md)
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
- [UIConversationContext.Entry](uiconversationcontext/entry.md)
  A base class that represents a message in a conversation.
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiconversationcontext)*