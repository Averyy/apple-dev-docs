# INEditMessageIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol INEditMessageIntentHandling : NSObjectProtocol
```

```objc
@protocol INEditMessageIntentHandling <NSObject>
```

## Mentions

- [Improving interactions between Siri and your messaging app](../SiriKit/improving-interactions-between-siri-and-your-messaging-app.md)

## Topics

### Instance Methods
- [func confirm(intent: INEditMessageIntent, completion: (INEditMessageIntentResponse) -> Void)](./ineditmessageintenthandling/confirm%28intent,completion%29.md)
- [func handle(intent: INEditMessageIntent, completion: (INEditMessageIntentResponse) -> Void)](./ineditmessageintenthandling/handle%28intent,completion%29.md)
- [func resolveEditedContent(for: INEditMessageIntent, with: (INStringResolutionResult) -> Void)](./ineditmessageintenthandling/resolveeditedcontent%28for,with%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Editing a Message
- [class INEditMessageIntent](./ineditmessageintent.md)
- [class INEditMessageIntentResponse](./ineditmessageintentresponse.md)
- [enum INEditMessageIntentResponseCode](./ineditmessageintentresponsecode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ineditmessageintenthandling)*