# INSetCarLockStatusIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to lock or unlock the car.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INSetCarLockStatusIntentResponse
```

```objc
@interface INSetCarLockStatusIntentResponse : INIntentResponse
```

## Overview

Use an `INSetCarLockStatusIntentResponse` object to specify the result of a request to lock or unlock the user’s car. You create instances of this class when confirming or handling a set car lock intent. Use this object to confirm that the request is valid and communicate whether the car was successfully locked or unlocked, or to report any errors that occur.

You create an `INSetCarLockStatusIntentResponse` object in the [`confirm(intent:completion:)`](./insetcarlockstatusintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./insetcarlockstatusintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INSetCarLockStatusIntentHandling`](./insetcarlockstatusintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INSetCarLockStatusIntentResponseCode, userActivity: NSUserActivity?)](./insetcarlockstatusintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity.
### Getting the Response Code
- [var code: INSetCarLockStatusIntentResponseCode](./insetcarlockstatusintentresponse/code.md)
  The code indicating success or failure when confirming or handling an intent.
- [enum INSetCarLockStatusIntentResponseCode](./insetcarlockstatusintentresponsecode.md)
  Constants indicating the status of the response.

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

### Set Car Lock Status
- [protocol INSetCarLockStatusIntentHandling](./insetcarlockstatusintenthandling.md)
  The handler interface for requesting to lock or unlock a car.
- [class INSetCarLockStatusIntent](./insetcarlockstatusintent.md)
  A request to lock or unlock the user’s car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/insetcarlockstatusintentresponse)*