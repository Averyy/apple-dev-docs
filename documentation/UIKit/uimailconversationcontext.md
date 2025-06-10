# UIMailConversationContext

**Framework**: UIKit  
**Kind**: class

A class that represents an email conversation.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class UIMailConversationContext
```

## Mentions

- [Adopting Smart Reply in your messaging or email app](adopting-smart-reply-in-your-messaging-or-email-app.md)

## Topics

### Getting message details
- [var responseSubject: String](uimailconversationcontext/responsesubject.md)
  A string that contains the subject line of an intended response.
- [var responseHasCustomSignature: Bool](uimailconversationcontext/responsehascustomsignature.md)
  A Boolean value that indicates whether the intended response contains a custom signature.
- [var responseSecondaryRecipientIdentifiers: Set<String>](uimailconversationcontext/responsesecondaryrecipientidentifiers.md)
  A set of strings that identifies the secondary recipients of the message, such as those in CC or BCC messages.

## Relationships

### Inherits From
- [UIConversationContext](uiconversationcontext.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uimailconversationcontext)*