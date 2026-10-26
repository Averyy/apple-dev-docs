# INSaveProfileInCarIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a save profile in car intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSaveProfileInCarIntentResponse
```

```objc
@interface INSaveProfileInCarIntentResponse : INIntentResponse
```

#### Overview

An [`INSaveProfileInCarIntentResponse`](./insaveprofileincarintentresponse.md) object contains the status of saving one or more environment settings to the designated profile. You create instances of this class when confirming or handling a save profile in car intent.

You create an [`INSaveProfileInCarIntentResponse`](./insaveprofileincarintentresponse.md) object in the [`confirm(intent:completion:)`](./insaveprofileincarintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insaveprofileincarintenthandling/handle%28intent,completion%29.md) methods of your save profile in car handler object. For more information about implementing your handler object, see [`INSaveProfileInCarIntentHandling`](./insaveprofileincarintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSaveProfileInCarIntentResponseCode, userActivity: NSUserActivity?)](./insaveprofileincarintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSaveProfileInCarIntentResponseCode](./insaveprofileincarintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSaveProfileInCarIntentResponseCode](./insaveprofileincarintentresponsecode.md)
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

### CarPlay Profile Saving
- [protocol INSaveProfileInCarIntentHandling](./insaveprofileincarintenthandling.md)
  The handler interface for saving vehicle environment settings to a user-specified profile.
- [class INSaveProfileInCarIntent](./insaveprofileincarintent.md)
  A request to save the user’s vehicle environment settings in a CarPlay-enabled vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insaveprofileincarintentresponse)*