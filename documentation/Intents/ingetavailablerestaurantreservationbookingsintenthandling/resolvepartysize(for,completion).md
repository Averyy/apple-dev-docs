# resolvePartySize(for:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the party size to use when generating the reservation times.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func resolvePartySize(for intent: INGetAvailableRestaurantReservationBookingsIntent, completion: @escaping @Sendable (INIntegerResolutionResult) -> Void)
```

```swift
optional func resolvePartySize(for intent: INGetAvailableRestaurantReservationBookingsIntent) async -> INIntegerResolutionResult
```

```objc
- (void) resolvePartySizeForGetAvailableRestaurantReservationBookings:(INGetAvailableRestaurantReservationBookingsIntent *) intent withCompletion:(void (^)(INIntegerResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the party size for the reservation.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value contains the number of people you plan to use when generating the list of reservation times. If you cannot create a reservation for the specified number of people, create a resolution object indicating that the current value is unsupported.

## See Also

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INGetAvailableRestaurantReservationBookingsIntent, completion: (INRestaurantResolutionResult) -> Void)](./resolverestaurant%28for,completion%29.md)
  Resolves the restaurant to use when gathering reservation times.
- [func resolvePreferredBookingDateComponents(for: INGetAvailableRestaurantReservationBookingsIntent, completion: (INDateComponentsResolutionResult) -> Void)](./resolvepreferredbookingdatecomponents%28for,completion%29.md)
  Resolves the date to use when generating the reservation times.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/ingetavailablerestaurantreservationbookingsintenthandling/resolvepartysize(for:completion:))*