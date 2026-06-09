# previousMessagesLimit

**Framework**: Suggested Actions  
**Kind**: property

The maximum number of previous messages that contribute to generating suggested actions.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
static var previousMessagesLimit: Int { get }
```

#### Discussion

When you pass an array of [`SuggestedActionsMessage`](suggestedactionsmessage.md) values to the `previousMessages` parameter of [`init(message:previousMessages:)`](suggestedactionsview/init(message:previousmessages:).md) or [`generate(message:previousMessages:)`](suggestedactionsview/generate(message:previousmessages:).md), the framework only considers a limited number of provided previous messages. `previousMessagesLimit` represents this limit. The framework ignores any older messages that exceed it.

The value of `previousMessagesLimit` may change between OS releases. Read it at runtime rather than hardcoding a limit to avoid constructing [`SuggestedActionsMessage`](suggestedactionsmessage.md) instances that the framework doesn’t use, as shown in the following example:

```swift
let previousMessages = allPreviousMessages
    .suffix(SuggestedActionsMessage.previousMessagesLimit)
    .map(\.suggestedActionsMessage)

SuggestedActionsView(
    message: message.suggestedActionsMessage,
    previousMessages: previousMessages
)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/suggestedactions/suggestedactionsmessage/previousmessageslimit)*