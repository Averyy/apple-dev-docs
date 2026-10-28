# resolveBookingDateComponents(for:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the date of the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func resolveBookingDateComponents(for intent: INBookRestaurantReservationIntent, completion: @escaping @Sendable (INDateComponentsResolutionResult) -> Void)
```

```swift
optional func resolveBookingDateComponents(for intent: INBookRestaurantReservationIntent) async -> INDateComponentsResolutionResult
```

```objc
- (void) resolveBookingDateComponentsForBookRestaurantReservation:(INBookRestaurantReservationIntent *) intent withCompletion:(void (^)(INDateComponentsResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve the date associated with the reservation.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value contains the date you plan to use when booking the reservation.

## See Also

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INBookRestaurantReservationIntent, completion: (INRestaurantResolutionResult) -> Void)](./resolverestaurant%28for,completion%29.md)
  Resolves the restaurant associated with the reservation.
- [func resolvePartySize(for: INBookRestaurantReservationIntent, completion: (INIntegerResolutionResult) -> Void)](./resolvepartysize%28for,completion%29.md)
  Resolves the number of people in the user’s party.
- [func resolveGuest(for: INBookRestaurantReservationIntent, completion: (INRestaurantGuestResolutionResult) -> Void)](./resolveguest%28for,completion%29.md)
  Resolves the identity of the guest associated with the reservation.
- [func resolveGuestProvidedSpecialRequestText(for: INBookRestaurantReservationIntent, completion: (INStringResolutionResult) -> Void)](./resolveguestprovidedspecialrequesttext%28for,completion%29.md)
  Resolves any special requests made in connection with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintenthandling/resolvebookingdatecomponents(for:completion:))*