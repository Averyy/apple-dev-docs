# INShareFocusStatusIntentHandling

**Framework**: Intents  
**Kind**: protocol  
**Role**: Protocol

A set of methods an object implements to process intents that share the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
protocol INShareFocusStatusIntentHandling : NSObjectProtocol
```

```objc
@protocol INShareFocusStatusIntentHandling <NSObject>
```

## Topics

### Processing the Intent
- [func confirm(intent: INShareFocusStatusIntent, completion: (INShareFocusStatusIntentResponse) -> Void)](./insharefocusstatusintenthandling/confirm%28intent,completion%29.md)
  Confirms the details of the request to share the user’s focus status.
- [func handle(intent: INShareFocusStatusIntent, completion: (INShareFocusStatusIntentResponse) -> Void)](./insharefocusstatusintenthandling/handle%28intent,completion%29.md)
  Handles the intent that shares the user’s focus status.

## Relationships

### Inherits From
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Sharing the User’s Focus Status
- [class INShareFocusStatusIntent](./insharefocusstatusintent.md)
  An object that indicates the user’s focus status is changing.
- [class INShareFocusStatusIntentResponse](./insharefocusstatusintentresponse.md)
  Your app’s response to an intent that shares the user’s focus status.
- [enum INShareFocusStatusIntentResponseCode](./insharefocusstatusintentresponsecode.md)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
- [class INFocusStatus](./infocusstatus.md)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](./infocusstatuscenter.md)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](./infocusstatusauthorizationstatus.md)
  A constant that indicates whether your app has authorization to access the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insharefocusstatusintenthandling)*