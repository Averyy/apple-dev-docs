# INSetRadioStationIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a set radio station intent.

**Availability**:
- iOS 10.0+ - Deprecated in 15.0
- iPadOS 10.0+ - Deprecated in 15.0
- Mac Catalyst 13.1+ - Deprecated in 15.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: This intent is no longer available. You may define a custom intent instead. For more information, see [Deprecated SiriKit Intent Domains](https://developer.apple.com/support/deprecated-sirikit-intent-domains).

## Declaration

```swift
class INSetRadioStationIntentResponse
```

```objc
@interface INSetRadioStationIntentResponse : INIntentResponse
```

## Overview

An [`INSetRadioStationIntentResponse`](./insetradiostationintentresponse.md) object contains the status of changing the currently playing radio station. You create instances of this class when confirming or handling a set radio station intent.

You create an [`INSetRadioStationIntentResponse`](./insetradiostationintentresponse.md) object in the [`confirm(intent:completion:)`](./insetradiostationintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insetradiostationintenthandling/handle%28intent,completion%29.md) methods of your set seat settings in car handler object. For more information about implementing your handler object, see [`INSetRadioStationIntentHandling`](./insetradiostationintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSetRadioStationIntentResponseCode, userActivity: NSUserActivity?)](./insetradiostationintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INSetRadioStationIntentResponseCode](./insetradiostationintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INSetRadioStationIntentResponseCode](./insetradiostationintentresponsecode.md)
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

### CarPlay Radio Station Settings
- [protocol INSetRadioStationIntentHandling](./insetradiostationintenthandling.md)
  The handler interface for changing a radio station.
- [class INSetRadioStationIntent](./insetradiostationintent.md)
  A request to change the current radio station.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetradiostationintentresponse)*