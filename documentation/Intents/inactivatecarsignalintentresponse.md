# INActivateCarSignalIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to activate a car’s signals.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INActivateCarSignalIntentResponse
```

```objc
@interface INActivateCarSignalIntentResponse : INIntentResponse
```

## Overview

Use an `INActivateCarSignalIntentResponse` object to specify the result of a request to activate the signal on the user’s car. You create instances of this class when confirming or handling an activate car signal intent. Use this object to confirm that the request is valid and communicate whether the signal was successfully activated, or to report any errors that occur.

You create an `INActivateCarSignalIntentResponse` object in the [`confirm(intent:completion:)`](./inactivatecarsignalintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inactivatecarsignalintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INActivateCarSignalIntentHandling`](./inactivatecarsignalintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INActivateCarSignalIntentResponseCode, userActivity: NSUserActivity?)](./inactivatecarsignalintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity.
### Getting the Response Code
- [var code: INActivateCarSignalIntentResponseCode](./inactivatecarsignalintentresponse/code.md)
  The code indicating success or failure when confirming or handling an intent.
- [enum INActivateCarSignalIntentResponseCode](./inactivatecarsignalintentresponsecode.md)
  Constants indicating the status of the response.
### Providing the Signal Information
- [var signals: INCarSignalOptions](./inactivatecarsignalintentresponse/signals.md)
  The type of signal produced (audible or visual).

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

### Activate Car Signal
- [protocol INActivateCarSignalIntentHandling](./inactivatecarsignalintenthandling.md)
  The handler interface for requesting to activate the car’s signals.
- [class INActivateCarSignalIntent](./inactivatecarsignalintent.md)
  A request to activate the signals on the user’s car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inactivatecarsignalintentresponse)*