# send(_:)

**Framework**: Foundation Models  
**Kind**: method

Performs a send on the channel.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
(nonsending) func send(_ event: some LanguageModelExecutorGenerationChannel.Event) async
```

## Parameters

- `event`: The event to send.

## See Also

- [LanguageModelExecutorGenerationChannel.Event](languagemodelexecutorgenerationchannel/event.md)
  A typed event that can be sent on a generation channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/send(_:))*