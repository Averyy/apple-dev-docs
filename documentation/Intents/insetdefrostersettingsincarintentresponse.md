# INSetDefrosterSettingsInCarIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a set defroster settings in car intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetDefrosterSettingsInCarIntentResponse
```

```objc
@interface INSetDefrosterSettingsInCarIntentResponse : INIntentResponse
```

## Overview

An [`INSetDefrosterSettingsInCarIntentResponse`](./insetdefrostersettingsincarintentresponse.md) object contains the status of changing the defroster settings in the user’s vehicle. You create instances of this class when confirming or handling a set defroster settings in car intent.

You create an [`INSetDefrosterSettingsInCarIntentResponse`](./insetdefrostersettingsincarintentresponse.md) object in the [`confirm(intent:completion:)`](./insetdefrostersettingsincarintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insetdefrostersettingsincarintenthandling/handle%28intent,completion%29.md) methods of your set defroster settings in car handler object. For more information about implementing your handler object, see [`INSetDefrosterSettingsInCarIntentHandling`](./insetdefrostersettingsincarintenthandling.md).

## Topics

### Initializing the Response
- [init(code: INSetDefrosterSettingsInCarIntentResponseCode, userActivity: NSUserActivity?)](./insetdefrostersettingsincarintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSetDefrosterSettingsInCarIntentResponseCode](./insetdefrostersettingsincarintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSetDefrosterSettingsInCarIntentResponseCode](./insetdefrostersettingsincarintentresponsecode.md)
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

### CarPlay Defroster Settings
- [protocol INSetDefrosterSettingsInCarIntentHandling](./insetdefrostersettingsincarintenthandling.md)
  The handler interface for changing a vehicle’s defroster settings.
- [class INSetDefrosterSettingsInCarIntent](./insetdefrostersettingsincarintent.md)
  A request to change the defroster settings in a CarPlay-enabled vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetdefrostersettingsincarintentresponse)*