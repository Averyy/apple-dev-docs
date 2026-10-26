# INHangUpCallIntentHandling

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
protocol INHangUpCallIntentHandling : NSObjectProtocol
```

```objc
@protocol INHangUpCallIntentHandling <NSObject>
```

## Topics

### Instance Methods
- [func confirm(intent: INHangUpCallIntent, completion: (INHangUpCallIntentResponse) -> Void)](./inhangupcallintenthandling/confirm%28intent,completion%29.md)
- [func handle(intent: INHangUpCallIntent, completion: (INHangUpCallIntentResponse) -> Void)](./inhangupcallintenthandling/handle%28intent,completion%29.md)

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Ending a Call
- [class INHangUpCallIntent](./inhangupcallintent.md)
- [class INHangUpCallIntentResponse](./inhangupcallintentresponse.md)
- [enum INHangUpCallIntentResponseCode](./inhangupcallintentresponsecode.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inhangupcallintenthandling)*