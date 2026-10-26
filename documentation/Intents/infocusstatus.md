# INFocusStatus

**Framework**: Intents  
**Kind**: class  
**Role**: Class

The user’s preference for receiving notifications.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class INFocusStatus
```

```objc
@interface INFocusStatus : NSObject
```

#### Overview

When a user wants to focus, they can choose to prevent or delay notifications from most apps. Use this information to display that the user is in a focus to other people in your communication service.

## Topics

### Creating a Status
- [convenience init(isFocused: Bool?)](./infocusstatus/init%28isfocused%29.md)
  Creates an object that indicates the user’s focus status.
### Accessing the User’s Status
- [var isFocused: Bool?](./infocusstatus/isfocused-8ytve.md)
  The user’s preference for receiving communication notifications.
### Initializers
- [init?(coder: NSCoder)](./infocusstatus/init%28coder%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
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
- [class INShareFocusStatusIntentResponse](./insharefocusstatusintentresponse.md)
  Your app’s response to an intent that shares the user’s focus status.
- [enum INShareFocusStatusIntentResponseCode](./insharefocusstatusintentresponsecode.md)
  A constant that indicates your app’s ability to handle an intent to share the user’s focus status.
- [class INFocusStatusCenter](./infocusstatuscenter.md)
  An object that maintains the user’s current focus status and your app’s ability to access it.
- [enum INFocusStatusAuthorizationStatus](./infocusstatusauthorizationstatus.md)
  A constant that indicates whether your app has authorization to access the user’s focus status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/infocusstatus)*