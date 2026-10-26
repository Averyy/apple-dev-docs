# INSetProfileInCarIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a set profile in car intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetProfileInCarIntentResponse
```

```objc
@interface INSetProfileInCarIntentResponse : INIntentResponse
```

#### Overview

An [`INSetProfileInCarIntentResponse`](./insetprofileincarintentresponse.md) object contains the status of restoring one or more environment settings from a designated profile. You create instances of this class when confirming or handling a set profile in car intent.

You create an [`INSetProfileInCarIntentResponse`](./insetprofileincarintentresponse.md) object in the [`confirm(intent:completion:)`](./insetprofileincarintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insetprofileincarintenthandling/handle%28intent,completion%29.md) methods of your set profile in car handler object. For more information about implementing your handler object, see [`INSetProfileInCarIntentHandling`](./insetprofileincarintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSetProfileInCarIntentResponseCode, userActivity: NSUserActivity?)](./insetprofileincarintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSetProfileInCarIntentResponseCode](./insetprofileincarintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSetProfileInCarIntentResponseCode](./insetprofileincarintentresponsecode.md)
  Constants indicating the state of the response.

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

### CarPlay Profile Settings
- [protocol INSetProfileInCarIntentHandling](./insetprofileincarintenthandling.md)
  The handler interface for restoring vehicle environment settings from a user-specified profile.
- [class INSetProfileInCarIntent](./insetprofileincarintent.md)
  A request to change the user’s vehicle environment settings to the ones from the specified profile.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetprofileincarintentresponse)*