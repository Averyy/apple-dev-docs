# resolvePreferredBookingDateComponents(for:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the date to use when generating the reservation times.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func resolvePreferredBookingDateComponents(for intent: INGetAvailableRestaurantReservationBookingsIntent, completion: @escaping @Sendable (INDateComponentsResolutionResult) -> Void)
```

```swift
optional func resolvePreferredBookingDateComponents(for intent: INGetAvailableRestaurantReservationBookingsIntent) async -> INDateComponentsResolutionResult
```

```objc
- (void) resolvePreferredBookingDateComponentsForGetAvailableRestaurantReservationBookings:(INGetAvailableRestaurantReservationBookingsIntent *) intent withCompletion:(void (^)(INDateComponentsResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to resolve the date used when generating the reservation times.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value contains the date you plan to use when generating the list of reservation times. If you cannot create a reservation for the specified date, create a resolution object suggesting the nearest date that is available and ask the user for confirmation.

## See Also

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INGetAvailableRestaurantReservationBookingsIntent, completion: (INRestaurantResolutionResult) -> Void)](./resolverestaurant%28for,completion%29.md)
  Resolves the restaurant to use when gathering reservation times.
- [func resolvePartySize(for: INGetAvailableRestaurantReservationBookingsIntent, completion: (INIntegerResolutionResult) -> Void)](./resolvepartysize%28for,completion%29.md)
  Resolves the party size to use when generating the reservation times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintenthandling/resolvepreferredbookingdatecomponents(for:completion:))*