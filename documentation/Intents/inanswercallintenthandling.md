# INAnswerCallIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 16.2+
- iPadOS 16.2+
- Mac Catalyst 16.2+
- macOS 13.1+
- visionOS 1.0+
- watchOS 9.2+

## Declaration

```swift
protocol INAnswerCallIntentHandling : NSObjectProtocol
```

```objc
@protocol INAnswerCallIntentHandling <NSObject>
```

## Topics

### Instance Methods
- [func confirm(intent: INAnswerCallIntent, completion: (INAnswerCallIntentResponse) -> Void)](./inanswercallintenthandling/confirm%28intent,completion%29.md)
- [func handle(intent: INAnswerCallIntent, completion: (INAnswerCallIntentResponse) -> Void)](./inanswercallintenthandling/handle%28intent,completion%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Answering a Call
- [class INAnswerCallIntent](./inanswercallintent.md)
- [class INAnswerCallIntentResponse](./inanswercallintentresponse.md)
- [enum INAnswerCallIntentResponseCode](./inanswercallintentresponsecode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inanswercallintenthandling)*