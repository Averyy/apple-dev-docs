# INSetMessageAttributeIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

An interface that handles modifying message attributes.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
protocol INSetMessageAttributeIntentHandling : NSObjectProtocol
```

```objc
@protocol INSetMessageAttributeIntentHandling <NSObject>
```

## Mentions

- [Dispatching intents to handlers](../SiriKit/dispatching-intents-to-handlers.md)

#### Overview

Use the methods of the [`INSetMessageAttributeIntentHandling`](./insetmessageattributeintenthandling.md) protocol to resolve, confirm, and handle requests to modify attributes of a user’s messages. Adopt this protocol in an object of your Intents extension that is capable of updating the state of messages, such as whether a user has read or flagged the message.

Siri delivers an [`INSetMessageAttributeIntent`](./insetmessageattributeintent.md) object to your handler when the user asks to modify one or more messages. The provided intent object contains the identifier strings for the messages to modify and information about which attributes to set. Use the methods of this protocol to resolve whether you can modify the messages in the intended way and to make the modifications.

## Topics

### Resolving the Intent Parameters
- [func resolveAttribute(for: INSetMessageAttributeIntent, with: (INMessageAttributeResolutionResult) -> Void)](./insetmessageattributeintenthandling/resolveattribute%28for,with%29.md)
  Resolves the attribute to apply to the messages.
### Confirming the Response
- [func confirm(intent: INSetMessageAttributeIntent, completion: (INSetMessageAttributeIntentResponse) -> Void)](./insetmessageattributeintenthandling/confirm%28intent,completion%29.md)
  Confirms that you can modify the attributes.
### Handling the Intent
- [func handle(intent: INSetMessageAttributeIntent, completion: (INSetMessageAttributeIntentResponse) -> Void)](./insetmessageattributeintenthandling/handle%28intent,completion%29.md)
  Handles modifying the message attributes.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
### Inherited By
- [INMessagesDomainHandling](./inmessagesdomainhandling.md)

## See Also

### Setting Message Attributes
- [class INSetMessageAttributeIntent](./insetmessageattributeintent.md)
  A request to modify the attributes of a message.
- [class INSetMessageAttributeIntentResponse](./insetmessageattributeintentresponse.md)
  Your app’s response to a set message attribute intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetmessageattributeintenthandling)*