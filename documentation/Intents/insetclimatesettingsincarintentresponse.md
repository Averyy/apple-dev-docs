# INSetClimateSettingsInCarIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a set climate settings in car intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetClimateSettingsInCarIntentResponse
```

```objc
@interface INSetClimateSettingsInCarIntentResponse : INIntentResponse
```

## Overview

An [`INSetClimateSettingsInCarIntentResponse`](./insetclimatesettingsincarintentresponse.md) object contains the status of changing the climate control settings in the user’s vehicle. You create instances of this class when confirming or handling a set climate settings in car intent.

You create an [`INSetClimateSettingsInCarIntentResponse`](./insetclimatesettingsincarintentresponse.md) object in the [`confirm(intent:completion:)`](./insetclimatesettingsincarintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insetclimatesettingsincarintenthandling/handle%28intent,completion%29.md) methods of your set climate settings in car handler object. For more information about implementing your handler object, see [`INSetClimateSettingsInCarIntentHandling`](./insetclimatesettingsincarintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSetClimateSettingsInCarIntentResponseCode, userActivity: NSUserActivity?)](./insetclimatesettingsincarintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSetClimateSettingsInCarIntentResponseCode](./insetclimatesettingsincarintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSetClimateSettingsInCarIntentResponseCode](./insetclimatesettingsincarintentresponsecode.md)
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

### CarPlay Climate Settings
- [protocol INSetClimateSettingsInCarIntentHandling](./insetclimatesettingsincarintenthandling.md)
  The handler interface for changing a vehicle’s climate control settings.
- [class INSetClimateSettingsInCarIntent](./insetclimatesettingsincarintent.md)
  A request to change the climate settings in a CarPlay-enabled vehicle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetclimatesettingsincarintentresponse)*