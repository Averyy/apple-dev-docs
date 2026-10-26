# INShareFocusStatusIntentResponseCode

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

A constant that indicates your app’s ability to handle an intent to share the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum INShareFocusStatusIntentResponseCode
```

```c
enum INShareFocusStatusIntentResponseCode : NSInteger;
```

## Topics

### Confirming the Intent
- [INShareFocusStatusIntentResponseCode.ready](./insharefocusstatusintentresponsecode/ready.md)
  Your intent handler is ready to handle the intent.
### Handling the Intent
- [INShareFocusStatusIntentResponseCode.success](./insharefocusstatusintentresponsecode/success.md)
  Your intent handler successfully updated the user’s communication status.
- [INShareFocusStatusIntentResponseCode.inProgress](./insharefocusstatusintentresponsecode/inprogress.md)
  Your intent handler is handling the intent, but it may take some time.
### Reporting a Problem
- [INShareFocusStatusIntentResponseCode.failure](./insharefocusstatusintentresponsecode/failure.md)
  Your intent handler is unable to handle the intent.
- [INShareFocusStatusIntentResponseCode.failureRequiringAppLaunch](./insharefocusstatusintentresponsecode/failurerequiringapplaunch.md)
  The user needs to launch your app to update their focus status.
- [INShareFocusStatusIntentResponseCode.unspecified](./insharefocusstatusintentresponsecode/unspecified.md)
  An unspecified response code.
### Initializers
- [init?(rawValue: Int)](./insharefocusstatusintentresponsecode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Sharing the User’s Focus Status
- [protocol INShareFocusStatusIntentHandling](./insharefocusstatusintenthandling.md)
  A set of methods an object implements to process intents that share the user’s focus status.
- [class INShareFocusStatusIntent](./insharefocusstatusintent.md)
  An object that indicates the user’s focus status is changing.
- [class INShareFocusStatusIntentResponse](./insharefocusstatusintentresponse.md)
  Your app’s response to an intent that shares the user’s focus status.
- [class INFocusStatus](./infocusstatus.md)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](./infocusstatuscenter.md)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](./infocusstatusauthorizationstatus.md)
  A constant that indicates whether your app has authorization to access the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insharefocusstatusintentresponsecode)*