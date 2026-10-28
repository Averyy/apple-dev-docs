# INGetReservationDetailsIntentResponse

**Framework**: Intents  
**Kind**: class  
**Role**: Class

Your app’s response to a request for reservation details.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class INGetReservationDetailsIntentResponse
```

```objc
@interface INGetReservationDetailsIntentResponse : INIntentResponse
```

## Mentions

- [Donating Reservations](../SiriKit/donating-reservations.md)

## Overview

Use an [`INGetReservationDetailsIntentResponse`](./ingetreservationdetailsintentresponse.md) object to specify the results of a user requesting reservation details in your app. After getting the reservation details action using the criteria specified in the [`INGetReservationDetailsIntent`](./ingetreservationdetailsintent.md) object, create an instance of this class with the results of the action. Siri can then use this information for system integrations, such as populating the calendar with an event.

## Topics

### Initializing the Response Object
- [init(code: INGetReservationDetailsIntentResponseCode, userActivity: NSUserActivity?)](./ingetreservationdetailsintentresponse/init%28code,useractivity%29.md)
  Creates the response object with the specified code and user activity object.
### Accessing the Reservations
- [var reservations: [INReservation]?](./ingetreservationdetailsintentresponse/reservations.md)
  An array containing reservations reqeusted by the user.
### Getting the Response Code
- [var code: INGetReservationDetailsIntentResponseCode](./ingetreservationdetailsintentresponse/code.md)
  The code that indicates whether your app successfully handled the intent.
- [enum INGetReservationDetailsIntentResponseCode](./ingetreservationdetailsintentresponsecode.md)
  Constants that indicate the status of the request for reservations details.

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

### Reservation Details
- [class INGetReservationDetailsIntent](./ingetreservationdetailsintent.md)
  A request for details about one or more reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetreservationdetailsintentresponse)*