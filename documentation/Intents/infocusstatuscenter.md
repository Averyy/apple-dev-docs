# INFocusStatusCenter

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that maintains the user’s current focus status and your app’s ability to access it.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class INFocusStatusCenter
```

```objc
@interface INFocusStatusCenter : NSObject
```

## Topics

### Accessing the Default Status Center
- [class var `default`: INFocusStatusCenter](./infocusstatuscenter/default.md)
  The systemwide object that holds the user’s focus status.
### Requesting Authorization
- [func requestAuthorization(completionHandler: ((INFocusStatusAuthorizationStatus) -> Void)?)](./infocusstatuscenter/requestauthorization%28completionhandler%29.md)
  Asks the system for access to the user’s focus status.
- [var authorizationStatus: INFocusStatusAuthorizationStatus](./infocusstatuscenter/authorizationstatus.md)
  Returns your app’s current ability to access the user’s focus status.
### Retrieving the User’s Focus Status
- [var focusStatus: INFocusStatus](./infocusstatuscenter/focusstatus.md)
  The user’s ability to receive notifications.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

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
- [enum INFocusStatusAuthorizationStatus](./infocusstatusauthorizationstatus.md)
  A constant that indicates whether your app has authorization to access the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatuscenter)*