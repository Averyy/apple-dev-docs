# INGetAvailableRestaurantReservationBookingDefaultsIntent

**Framework**: Intents  
**Kind**: class  
**Role**: Class

A request for the default values to use when fetching potential reservation options.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
class INGetAvailableRestaurantReservationBookingDefaultsIntent
```

```objc
@interface INGetAvailableRestaurantReservationBookingDefaultsIntent : INIntent
```

#### Overview

An [`INGetAvailableRestaurantReservationBookingDefaultsIntent`](./ingetavailablerestaurantreservationbookingdefaultsintent.md) object asks you to provide the set of default options to use when fetching possible reservation times for the specified restaurant. Because restaurants may have different requirements for booking reservations, this intent lets you provide a set of reasonable default values that reflect any restaurant-specific requirements or user tendencies. For example, you use this intent to return the minimum or maximum party size supported by the restaurant.

To handle this intent, the handler object in your Intents extension must adopt the [`INGetAvailableRestaurantReservationBookingDefaultsIntentHandling`](./ingetavailablerestaurantreservationbookingdefaultsintenthandling.md) protocol. Your handler should resolve and confirm any parameters and create an [`INGetAvailableRestaurantReservationBookingDefaultsIntentResponse`](./ingetavailablerestaurantreservationbookingdefaultsintentresponse.md) object with the found results.

##### Additional Intent Attributes

The following table lists additional attributes of this intent object:

| Attribute | Description |
| --- | --- |
| Supported by | Maps |
| Always requires unlocked device | Yes |

## Topics

### Initializing the Intent Object
- [init(restaurant: INRestaurant?)](./ingetavailablerestaurantreservationbookingdefaultsintent/init%28restaurant%29.md)
  Initializes the intent object with the specified restaurant.
### Accessing the Restaurant Details
- [var restaurant: INRestaurant?](./ingetavailablerestaurantreservationbookingdefaultsintent/restaurant.md)
  The restaurant to use when determining any default values.

## Relationships

### Inherits From
- [INIntent](./inintent.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [INIntentSetImageKeyPath](./inintentsetimagekeypath.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Get Available Restaurant Reservation Booking Defaults
- [protocol INGetAvailableRestaurantReservationBookingDefaultsIntentHandling](./ingetavailablerestaurantreservationbookingdefaultsintenthandling.md)
  The handler interface for providing default values to the system when pre-fetching an initial set of possible reservation times.
- [class INGetAvailableRestaurantReservationBookingDefaultsIntentResponse](./ingetavailablerestaurantreservationbookingdefaultsintentresponse.md)
  Your app’s response to a get available restaurant reservation booking defaults intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingdefaultsintent)*