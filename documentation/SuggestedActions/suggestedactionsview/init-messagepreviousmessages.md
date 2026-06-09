# init(message:previousMessages:)

**Framework**: Suggested Actions  
**Kind**: init

Creates a view that shows suggested actions for the specified message.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
@MainActor
init(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage] = [])
```

#### Discussion

Use this initializer to present suggested actions that the framework generates for a provided message. The Suggested Actions framework analyzes the message, and previous messages you provide as additional context, then shows relevant actions that a person can take.

If you call [`generate(message:previousMessages:)`](suggestedactionsview/generate(message:previousmessages:).md) to generate suggested actions for future use, and later pass a [`SuggestedActionsMessage`](suggestedactionsmessage.md), the Suggested Actions framework checks for suggested actions it already generated and cached. If it finds a message with a matching `id`, the `SuggestedActionsView` uses the cached result and renders the suggested actions immediately.

The following example shows how an app might show a `SuggestedActionsView` with information from previous messages:

```swift
struct ChatView: View {
    @Binding
    var messages: [ChatMessage]

    var body: some View {
        ForEach(messages) { message in
            ChatBubble(message)

            SuggestedActionsView(
                message: message.suggestedActionsMessage,
                previousMessages: message.previousMessages
                    .suffix(SuggestedActionsMessage.previousMessagesLimit)
                    .map(\.suggestedActionsMessage)
            )
        }
    }
}
```

## Parameters

- `message`: The message that you want to generate suggested actions for.
- `previousMessages`: An array of messages that precede the provided `message`. The Suggested Actions framework uses them as context to generate suggested actions for the `message`. The system limits the number of previous messages it considers to the value of [`previousMessagesLimit`](suggestedactionsmessage/previousmessageslimit.md). This parameter defaults to an empty array if you don’t include previous messages.

## See Also

- [static func generate(message: SuggestedActionsMessage, previousMessages: [SuggestedActionsMessage]) async](suggestedactionsview/generate(message:previousmessages:).md)
  Fetches and caches suggested actions for the provided message.
- [struct SuggestedActionsMessage](suggestedactionsmessage.md)
  A representation of the message you use as context for suggested actions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsview/init(message:previousmessages:))*