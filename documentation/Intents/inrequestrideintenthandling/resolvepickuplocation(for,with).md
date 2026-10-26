# resolvePickupLocation(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the pickup location for the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolvePickupLocation(for intent: INRequestRideIntent, with completion: @escaping @Sendable (INPlacemarkResolutionResult) -> Void)
```

```swift
optional func resolvePickupLocation(for intent: INRequestRideIntent) async -> INPlacemarkResolutionResult
```

```objc
- (void) resolvePickupLocationForRequestRide:(INRequestRideIntent *) intent withCompletion:(void (^)(INPlacemarkResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to verify that you can pick up the user at the specified location. You may specify a pickup location that is different than the one requested by the user. For example, you might specify a dedicated pickup spot or an easy to spot point of interest that is near the user’s location. If you do not implement this method, SiriKit assumes that you are able to start the ride at the specified location.

If the pickup location is outside of your service area, return a successful resolution from this method and then create an appropriate response object with the [`INRequestRideIntentResponseCode.failureRequiringAppLaunchNoServiceInArea`](../inrequestrideintentresponsecode/failurerequiringapplaunchnoserviceinarea.md) code in your [`confirm(intent:completion:)`](./confirm%28intent,completion%29.md) method.

Maps does not call this method. The Maps interface lets the user specify the pickup location explicitly, making resolution of that value unnecessary.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing information about your proposed resolution. For successful resolutions, create a resolution object whose value contains the [`CLPlacemark`](../../CoreLocation/clplacemark.md) object you plan to use for the pickup location. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveScheduledPickupTime(for: INRequestRideIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvescheduledpickuptime%28for,with%29.md)
  Resolves the pickup time for the ride.
- [func resolveDropOffLocation(for: INRequestRideIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvedropofflocation%28for,with%29.md)
  Resolves the drop-off location for the ride.
- [func resolveRideOptionName(for: INRequestRideIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolverideoptionname%28for,with%29.md)
  Resolves the user’s selected ride option.
- [func resolvePartySize(for: INRequestRideIntent, with: (INIntegerResolutionResult) -> Void)](./resolvepartysize%28for,with%29.md)
  Resolves the number of passengers for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintenthandling/resolvepickuplocation(for:with:))*