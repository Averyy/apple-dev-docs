# INGetAvailableRestaurantReservationBookingDefaultsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a get available restaurant reservation booking defaults intent.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetAvailableRestaurantReservationBookingDefaultsIntentResponse
```

```objc
@interface INGetAvailableRestaurantReservationBookingDefaultsIntentResponse : INIntentResponse
```

## Overview

An [`INGetAvailableRestaurantReservationBookingDefaultsIntentResponse`](./ingetavailablerestaurantreservationbookingdefaultsintentresponse.md) object contains the default values to use when booking a reservation at a restaurant. You create instances of this class when confirming or handling an [`INGetAvailableRestaurantReservationBookingDefaultsIntent`](./ingetavailablerestaurantreservationbookingdefaultsintent.md) object.

The system uses the information to improve the overall user experience. Restaurants may have requirements for the minimum or maximum size of a party. Similarly, your service might be able to provide a default date that reflects the first time when reservations are available. The system uses this information both to gather an initial set of valid reservation options and to show the user what requirements the restaurant may impose. Although providing default values is not required, it is highly recommended.

You create an [`INGetAvailableRestaurantReservationBookingDefaultsIntentResponse`](./ingetavailablerestaurantreservationbookingdefaultsintentresponse.md) object in the [`confirm(getAvailableRestaurantReservationBookingDefaults:completion:)`](./ingetavailablerestaurantreservationbookingdefaultsintenthandling/confirm%28getavailablerestaurantreservationbookingdefaults,completion%29.md) and [`handle(getAvailableRestaurantReservationBookingDefaults:completion:)`](./ingetavailablerestaurantreservationbookingdefaultsintenthandling/handle%28getavailablerestaurantreservationbookingdefaults,completion%29.md) methods of handler object. For more information about implementing your handler object, see [`INGetAvailableRestaurantReservationBookingDefaultsIntentHandling`](./ingetavailablerestaurantreservationbookingdefaultsintenthandling.md).

## Topics

### Initializing the Response Object
- [init(defaultPartySize: Int, defaultBooking: Date, code: INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode, userActivity: NSUserActivity?)](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/init%28defaultpartysize,defaultbooking,code,useractivity%29.md)
  Initializes the response object with the specified information and user activity object.
### Getting the Response Code
- [var code: INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/code.md)
  The code indicating whether you successfully handled the intent.
- [enum INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode](./ingetavailablerestaurantreservationbookingdefaultsintentresponsecode.md)
  Constants indicating the state of the response.
### Specifying the Default Values
- [var defaultBookingDate: Date](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/defaultbookingdate.md)
  The default booking date to use when placing the initial reservations request.
- [var defaultPartySize: Int](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/defaultpartysize.md)
  The party size to use when placing the initial reservations request.
- [var maximumPartySize: NSNumber?](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/maximumpartysize.md)
  The maximum party size allowed by the restaurant.
- [var minimumPartySize: NSNumber?](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/minimumpartysize.md)
  The minimum party size allowed by the restaurant.
- [var providerImage: INImage](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/providerimage.md)
  An image representing your app.
### Initializers
- [init(defaultPartySize: Int, defaultBookingDate: Date, code: INGetAvailableRestaurantReservationBookingDefaultsIntentResponseCode, userActivity: NSUserActivity?)](./ingetavailablerestaurantreservationbookingdefaultsintentresponse/init%28defaultpartysize,defaultbookingdate,code,useractivity%29.md)

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

### Get Available Restaurant Reservation Booking Defaults
- [protocol INGetAvailableRestaurantReservationBookingDefaultsIntentHandling](./ingetavailablerestaurantreservationbookingdefaultsintenthandling.md)
  The handler interface for providing default values to the system when pre-fetching an initial set of possible reservation times.
- [class INGetAvailableRestaurantReservationBookingDefaultsIntent](./ingetavailablerestaurantreservationbookingdefaultsintent.md)
  A request for the default values to use when fetching potential reservation options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintentresponse)*