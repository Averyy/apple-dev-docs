# INGetCarLockStatusIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to get the car’s lock status.

**Availability**:
- iOS 10.3+
- iPadOS 10.3+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
class INGetCarLockStatusIntentResponse
```

```objc
@interface INGetCarLockStatusIntentResponse : INIntentResponse
```

#### Overview

Use an `INGetCarLockStatusIntentResponse` object to specify the result of a request for a car’s current lock status. You create instances of this class when confirming or handling a get lock status intent. Use this object to confirm that the request is valid and communicate whether the app retrieved the lock status, or to report any errors that occur.

You create an `INGetCarLockStatusIntentResponse` object in the [`confirm(intent:completion:)`](./ingetcarlockstatusintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./ingetcarlockstatusintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INGetCarLockStatusIntentHandling`](./ingetcarlockstatusintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INGetCarLockStatusIntentResponseCode, userActivity: NSUserActivity?)](./ingetcarlockstatusintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity.
### Getting the Response Code
- [var code: INGetCarLockStatusIntentResponseCode](./ingetcarlockstatusintentresponse/code.md)
  The code indicating success or failure when confirming or handling an intent.
- [enum INGetCarLockStatusIntentResponseCode](./ingetcarlockstatusintentresponsecode.md)
  Constants indicating the status of the response.
### Providing the Locked Status
- [var locked: Bool?](./ingetcarlockstatusintentresponse/locked-357ju.md)
  A Boolean value indicating the status of the car’s locks.
- [locked](./ingetcarlockstatusintentresponse/locked-1eacd.md)
  A Boolean value indicating the status of the car’s locks.

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

### Get Car Lock Status
- [protocol INGetCarLockStatusIntentHandling](./ingetcarlockstatusintenthandling.md)
  The handler interface for requesting the current status of the car’s locks.
- [class INGetCarLockStatusIntent](./ingetcarlockstatusintent.md)
  A request to get the lock status of the user’s car.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetcarlockstatusintentresponse)*