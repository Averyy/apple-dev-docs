# INBookRestaurantReservationIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a book restaurant reservation intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INBookRestaurantReservationIntentResponse
```

```objc
@interface INBookRestaurantReservationIntentResponse : INIntentResponse
```

## Overview

An [`INBookRestaurantReservationIntentResponse`](./inbookrestaurantreservationintentresponse.md) object contains final reservation booking information. You create an instance of this class when confirming or handling an [`INBookRestaurantReservationIntent`](./inbookrestaurantreservationintent.md) object, which contains the details of the reservation that you need to book.

You create an [`INBookRestaurantReservationIntentResponse`](./inbookrestaurantreservationintentresponse.md) object in the [`confirm(bookRestaurantReservation:completion:)`](./inbookrestaurantreservationintenthandling/confirm%28bookrestaurantreservation,completion%29.md) and [`handle(bookRestaurantReservation:completion:)`](./inbookrestaurantreservationintenthandling/handle%28bookrestaurantreservation,completion%29.md) methods of your handler object. For more information about implementing your handler object, see [`INBookRestaurantReservationIntentHandling`](./inbookrestaurantreservationintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INBookRestaurantReservationIntentCode, userActivity: NSUserActivity?)](./inbookrestaurantreservationintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Accessing the Response Information
- [var code: INBookRestaurantReservationIntentCode](./inbookrestaurantreservationintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INBookRestaurantReservationIntentCode](./inbookrestaurantreservationintentcode.md)
  Constants indicating the state of the response.
- [var userBooking: INRestaurantReservationUserBooking?](./inbookrestaurantreservationintentresponse/userbooking.md)
  The detailed information about the reservation.

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

### Book Restaurant Reservation
- [protocol INBookRestaurantReservationIntentHandling](./inbookrestaurantreservationintenthandling.md)
  The handler interface booking a reservation that the user selected.
- [class INBookRestaurantReservationIntent](./inbookrestaurantreservationintent.md)
  A request to create a reservation at the specified restaurant.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintentresponse)*