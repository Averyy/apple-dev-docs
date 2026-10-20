# send(_:)

**Framework**: Foundation Models  
**Kind**: method  
**Role**: Instance Method

Sends a generation event on the channel.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
nonisolated
(nonsending) func send(_ event: LanguageModelExecutorGenerationChannel.Event) async
```

## Parameters

- `event`: The event to send.

## See Also

### Sending an event
- [LanguageModelExecutorGenerationChannel.Event](./event.md)
  A generation event sent on a generation channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelexecutorgenerationchannel/send(_:))*