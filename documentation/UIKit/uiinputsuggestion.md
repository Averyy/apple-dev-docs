# UIInputSuggestion

**Framework**: UIKit  
**Kind**: class

A base class you use to handle suggestions from the keyboard or system.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+

## Declaration

```swift
class UIInputSuggestion
```

#### Discussion

To handle photo search suggestions from Smart Actions, use [`UIPhotoSearchSuggestion`](uiphotosearchsuggestion.md), which provides the filter metadata you need to present a pre-populated photo picker or build a custom photo search. To handle Smart Reply suggestions, use [`UISmartReplySuggestion`](uismartreplysuggestion.md), which provides the reply text the person selected to guide a long-form response.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [UIPhotoSearchSuggestion](uiphotosearchsuggestion.md)
- [UISmartReplySuggestion](uismartreplysuggestion.md)
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
- [UIMessageConversationContext.MessageEntry](uimessageconversationcontext/messageentry.md)
  A class that represents a message in a message conversation.
- [class UIPhotoSearchSuggestion](uiphotosearchsuggestion.md)
  An input suggestion that carries photo search metadata for people, subjects, locations, and time periods.
- [class UISmartReplySuggestion](uismartreplysuggestion.md)
  A class you use to handle a Smart Reply suggestion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiinputsuggestion)*