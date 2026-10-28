# resolveGuestProvidedSpecialRequestText(for:completion:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves any special requests made in connection with the reservation.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
optional func resolveGuestProvidedSpecialRequestText(for intent: INBookRestaurantReservationIntent, completion: @escaping @Sendable (INStringResolutionResult) -> Void)
```

```swift
optional func resolveGuestProvidedSpecialRequestText(for intent: INBookRestaurantReservationIntent) async -> INStringResolutionResult
```

```objc
- (void) resolveGuestProvidedSpecialRequestTextForBookRestaurantReservation:(INBookRestaurantReservationIntent *) intent withCompletion:(void (^)(INStringResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to resolve any special requests for the reservation. For example, the guest requires a booster seat for a child or one of the guests has a food allergy.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The block to execute with the resolution. You must execute this block at some point during your implementation of this method. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object whose value contains a string with the text you plan to send to the restaurant when communicating special requests.

## See Also

### Resolving the Intent Parameters
- [func resolveRestaurant(for: INBookRestaurantReservationIntent, completion: (INRestaurantResolutionResult) -> Void)](./resolverestaurant%28for,completion%29.md)
  Resolves the restaurant associated with the reservation.
- [func resolveBookingDateComponents(for: INBookRestaurantReservationIntent, completion: (INDateComponentsResolutionResult) -> Void)](./resolvebookingdatecomponents%28for,completion%29.md)
  Resolves the date of the reservation.
- [func resolvePartySize(for: INBookRestaurantReservationIntent, completion: (INIntegerResolutionResult) -> Void)](./resolvepartysize%28for,completion%29.md)
  Resolves the number of people in the user’s party.
- [func resolveGuest(for: INBookRestaurantReservationIntent, completion: (INRestaurantGuestResolutionResult) -> Void)](./resolveguest%28for,completion%29.md)
  Resolves the identity of the guest associated with the reservation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbookrestaurantreservationintenthandling/resolveguestprovidedspecialrequesttext(for:completion:))*