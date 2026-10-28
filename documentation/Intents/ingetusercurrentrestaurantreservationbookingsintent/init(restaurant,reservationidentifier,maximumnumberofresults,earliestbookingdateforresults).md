# init(restaurant:reservationIdentifier:maximumNumberOfResults:earliestBookingDateForResults:)

**Framework**: Intents  
**Kind**: init  
**Role**: Initializer

Initializes the intent object with the specified reservation information.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
init(restaurant: INRestaurant?, reservationIdentifier: String?, maximumNumberOfResults: NSNumber?, earliestBookingDateForResults: Date?)
```

```objc
- (instancetype) initWithRestaurant:(INRestaurant *) restaurant reservationIdentifier:(NSString *) reservationIdentifier maximumNumberOfResults:(NSNumber *) maximumNumberOfResults earliestBookingDateForResults:(NSDate *) earliestBookingDateForResults;
```

## Return Value

An initialized intent object or `nil` if the object could not be created.

## Discussion

Normally, you do not create instances of this class yourself. Instead, SiriKit creates instances when Maps asks you to provide the user’s current list of reservations. However, you can use this method during testing to create intent objects in order to validate your intent handling code paths.

## Parameters

- `restaurant`: A restaurant to use as a filter when searching for reservations.
- `reservationIdentifier`: An identifier to use when searching for the user’s reservations.
- `maximumNumberOfResults`: The maximum number of reservations to include in your response object.
- `earliestBookingDateForResults`: The earliest date to be associated with any reservations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetusercurrentrestaurantreservationbookingsintent/init(restaurant:reservationidentifier:maximumnumberofresults:earliestbookingdateforresults:))*