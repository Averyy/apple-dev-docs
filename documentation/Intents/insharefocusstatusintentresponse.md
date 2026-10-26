# INShareFocusStatusIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to an intent that shares the user’s focus status.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class INShareFocusStatusIntentResponse
```

```objc
@interface INShareFocusStatusIntentResponse : INIntentResponse
```

## Topics

### Creating a Response
- [init(code: INShareFocusStatusIntentResponseCode, userActivity: NSUserActivity?)](./insharefocusstatusintentresponse/init%28code,useractivity%29.md)
  Creates a response with the specified response code and user activity.
### Accessing the Response Code
- [var code: INShareFocusStatusIntentResponseCode](./insharefocusstatusintentresponse/code.md)
  Your app’s ability to handle an intent that shares the user’s focus status.

## Relationships

### Inherits From
- [INIntentResponse](./inintentresponse.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Sharing the User’s Focus Status
- [protocol INShareFocusStatusIntentHandling](./insharefocusstatusintenthandling.md)
  A set of methods an object implements to process intents that share the user’s focus status.
- [class INShareFocusStatusIntent](./insharefocusstatusintent.md)
  An object that indicates the user’s focus status is changing.
- [enum INShareFocusStatusIntentResponseCode](./insharefocusstatusintentresponsecode.md)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
- [class INFocusStatus](./infocusstatus.md)
  The user’s preference for receiving notifications.
- [class INFocusStatusCenter](./infocusstatuscenter.md)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](./infocusstatusauthorizationstatus.md)
  A constant that indicates whether your app has authorization to access the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insharefocusstatusintentresponse)*