# INGetRestaurantGuestIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a get restaurant guest intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetRestaurantGuestIntentResponse
```

```objc
@interface INGetRestaurantGuestIntentResponse : INIntentResponse
```

#### Overview

An [`INGetRestaurantGuestIntentResponse`](./ingetrestaurantguestintentresponse.md) object contains the information about the current user along with preferences about whether to associate that user with any new reservations. You create this response when handling or confirming an [`INGetUserCurrentRestaurantReservationBookingsIntent`](./ingetusercurrentrestaurantreservationbookingsintent.md) object. Your response should contain information about the current user and information about how to display that user’s information in the interface used to make reservations.

You create an [`INGetRestaurantGuestIntentResponse`](./ingetrestaurantguestintentresponse.md) object in the [`confirm(getRestaurantGuest:completion:)`](./ingetrestaurantguestintenthandling/confirm%28getrestaurantguest,completion%29.md) and [`handle(getRestaurantGuest:completion:)`](./ingetrestaurantguestintenthandling/handle%28getrestaurantguest,completion%29.md) methods of handler object. For more information about implementing your handler object, see [`INGetRestaurantGuestIntentHandling`](./ingetrestaurantguestintenthandling.md).

## Topics

### Initializing the Response Object
- [init(code: INGetRestaurantGuestIntentResponseCode, userActivity: NSUserActivity?)](./ingetrestaurantguestintentresponse/init%28code,useractivity%29.md)
  Initializes the response object with the specified code and user activity object.
### Getting the Response Code
- [var code: INGetRestaurantGuestIntentResponseCode](./ingetrestaurantguestintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INGetRestaurantGuestIntentResponseCode](./ingetrestaurantguestintentresponsecode.md)
  Constants indicating the state of the response.
### Specifying the Response Details
- [var guest: INRestaurantGuest?](./ingetrestaurantguestintentresponse/guest.md)
  The identity of the person making the reservation.
- [var guestDisplayPreferences: INRestaurantGuestDisplayPreferences?](./ingetrestaurantguestintentresponse/guestdisplaypreferences.md)
  The options for specifying how you want guest information conveyed to the user.

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

### Get Restaurant Guest
- [protocol INGetRestaurantGuestIntentHandling](./ingetrestaurantguestintenthandling.md)
  The handler interface for fetching information about the person making a reservation.
- [class INGetRestaurantGuestIntent](./ingetrestaurantguestintent.md)
  A request for information about the guest who is making reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetrestaurantguestintentresponse)*