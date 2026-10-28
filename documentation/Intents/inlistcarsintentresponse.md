# INListCarsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request to list the user’s electric vehicles.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class INListCarsIntentResponse
```

```objc
@interface INListCarsIntentResponse : INIntentResponse
```

## Overview

Use an `INListCarsIntentResponse` to specify the result of a request from Maps for a list of the user’s electric vehicles. You create instances of this class when confirming or handling a List Cars intent. Use this object to confirm the request is valid and return a list of the user’s cars, or to report any errors that occur. Each entry in the [`cars`](./inlistcarsintentresponse/cars.md) array provides information about one of the user’s electric vehicles, including its unique car identifier and model information, such as name and year.

When creating a response that requires the system to launch your host app, always provide a relevant [`NSUserActivity`](../Foundation/nsuseractivity.md) object. This ensures your host app has the context it needs to handle the operation.

You create an `INListCarsIntentResponse` in the [`confirm(intent:completion:)`](./inlistcarsintenthandling/confirm%28intent,completion%29.md) and [`handle(intent:completion:)`](./inlistcarsintenthandling/handle%28intent,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INListCarsIntentHandling`](./inlistcarsintenthandling.md).

## Topics

### Creating a Response
- [init(code: INListCarsIntentResponseCode, userActivity: NSUserActivity?)](./inlistcarsintentresponse/init%28code,useractivity%29.md)
  Creates a response object with the specified code and user activity.
### Getting the Response Code
- [var code: INListCarsIntentResponseCode](./inlistcarsintentresponse/code.md)
  The code that indicates success or failure when confirming or handling the intent.
- [enum INListCarsIntentResponseCode](./inlistcarsintentresponsecode.md)
  Constants that represent the status of a response.
### Providing a List of Cars
- [var cars: [INCar]?](./inlistcarsintentresponse/cars.md)
  An array of the user’s electric vehicles.
- [class INCar](./incar.md)
  A specific electric vehicle that Maps uses during route planning and navigation.

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

### List Cars
- [protocol INListCarsIntentHandling](./inlistcarsintenthandling.md)
  The handler interface for requesting a list of the user’s electric vehicles.
- [class INListCarsIntent](./inlistcarsintent.md)
  An intent for retrieving a list of the user’s electric vehicles.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistcarsintentresponse)*