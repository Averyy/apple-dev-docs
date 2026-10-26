# INShareFocusStatusIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

An object that indicates the user’s focus status is changing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class INShareFocusStatusIntent
```

```objc
@interface INShareFocusStatusIntent : INIntent
```

## Topics

### Creating an Intent
- [init(focusStatus: INFocusStatus?)](./insharefocusstatusintent/init%28focusstatus%29.md)
  Creates an intent with the specified focus status.
### Accessing the Focus Status
- [var focusStatus: INFocusStatus?](./insharefocusstatusintent/focusstatus.md)
  The user’s preference for receiving communication notifications.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Sharing the User’s Focus Status
- [protocol INShareFocusStatusIntentHandling](./insharefocusstatusintenthandling.md)
  A set of methods an object implements to process intents that share the user’s focus status.
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

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insharefocusstatusintent)*