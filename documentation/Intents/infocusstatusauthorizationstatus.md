# INFocusStatusAuthorizationStatus

**Framework**: Intents  
**Kind**: enum  
**Role**: Enumeration

A constant that indicates whether your app has authorization to access the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum INFocusStatusAuthorizationStatus
```

```c
enum INFocusStatusAuthorizationStatus : NSInteger;
```

## Topics

### Constants
- [INFocusStatusAuthorizationStatus.notDetermined](./infocusstatusauthorizationstatus/notdetermined.md)
  The user hasn’t chosen whether to grant your app access to their focus status yet.
- [INFocusStatusAuthorizationStatus.restricted](./infocusstatusauthorizationstatus/restricted.md)
  A restriction prevents your app from accessing the user’s focus status.
- [INFocusStatusAuthorizationStatus.denied](./infocusstatusauthorizationstatus/denied.md)
  The user has denied your app access to their focus status.
- [INFocusStatusAuthorizationStatus.authorized](./infocusstatusauthorizationstatus/authorized.md)
  Your app has authorization to access the user’s focus status.
### Initializers
- [init?(rawValue: Int)](./infocusstatusauthorizationstatus/init%28rawvalue%29.md)

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
- [enum INShareFocusStatusIntentResponseCode](./insharefocusstatusintentresponsecode.md)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
- [class INFocusStatus](./infocusstatus.md)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](./infocusstatuscenter.md)
  An object that maintains the user’s current focus status and your app’s ability to access it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatusauthorizationstatus)*