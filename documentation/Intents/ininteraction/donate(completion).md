# donate(completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Donates this interaction object to the system.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
func donate(completion: (@Sendable ((any Error)?) -> Void)? = nil)
```

```swift
func donate() async throws
```

```objc
- (void) donateInteractionWithCompletion:(void (^)(NSError *error)) completion;
```

## Mentions

- [Donating Reservations](../../SiriKit/donating-reservations.md)
- [Donating Shortcuts](../../SiriKit/donating-shortcuts.md)

## Discussion

Call this method from your app when you want to donate a SiriKit interaction to the system to help improve search results. If you provide a block in the `completion` parameter, the system executes your block asynchronously with the results.

> ❗ **Important**:  Do not donate multiple interaction object representing the same user interaction. Each donated interaction should represent a single event that was handled by your app. For example, when sending a message to multiple recipients, a messaging app should donate only one interaction object, and the [`INSendMessageIntent`](../insendmessageintent.md) object included in that interaction should contain the complete list of recipients. The app should not donate separate interactions for each recipient.

## Parameters

- `completion`: A block to execute with the results. Provide a block if you want to know whether the interaction was donated successfully. The block has no return value and takes the following parameter.

  - **error**: An error object indicating a problem occurred. On success, this parameter is `nil`. If there was an error, this parameter contains an error object describing what happened.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ininteraction/donate(completion:))*