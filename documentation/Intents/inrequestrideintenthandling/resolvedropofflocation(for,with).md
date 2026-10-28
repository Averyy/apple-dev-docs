# resolveDropOffLocation(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the drop-off location for the ride.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolveDropOffLocation(for intent: INRequestRideIntent, with completion: @escaping @Sendable (INPlacemarkResolutionResult) -> Void)
```

```swift
optional func resolveDropOffLocation(for intent: INRequestRideIntent) async -> INPlacemarkResolutionResult
```

```objc
- (void) resolveDropOffLocationForRequestRide:(INRequestRideIntent *) intent withCompletion:(void (^)(INPlacemarkResolutionResult *resolutionResult)) completion;
```

## Discussion

Implement this method to verify that you can drop off the user at the specified location. You may specify a drop-off location that is different than the one requested by the user. For example, you might specify a dedicated drop-off spot or an easy to spot point of interest that is near the user’s requested drop-off location. If you do not implement this method, SiriKit assumes that you are able to end the ride at the specified location.

If the drop-off location is outside of your service area, return a successful resolution from this method and then create an appropriate response object with the [`INRequestRideIntentResponseCode.failureRequiringAppLaunchNoServiceInArea`](../inrequestrideintentresponsecode/failurerequiringapplaunchnoserviceinarea.md) code in your [`confirm(intent:completion:)`](./confirm%28intent,completion%29.md) method.

Maps does not call this method. The Maps interface lets the user specify the drop-off location explicitly, making resolution of that value unnecessary.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information, if any, provided by the user.
- `completion`: The handler block to execute with the resolution. You must execute this handler at some point during your implementation of this method. This handler has no return value and takes the following parameter:

  - **resolutionResult**: The resolution result object containing information about your proposed resolution. For successful resolutions, create a resolution object whose value contains the [`CLPlacemark`](../../CoreLocation/clplacemark.md) object you plan to use for the drop-off location. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolvePickupLocation(for: INRequestRideIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvepickuplocation%28for,with%29.md)
  Resolves the pickup location for the ride.
- [func resolveScheduledPickupTime(for: INRequestRideIntent, with: (INDateComponentsRangeResolutionResult) -> Void)](./resolvescheduledpickuptime%28for,with%29.md)
  Resolves the pickup time for the ride.
- [func resolveRideOptionName(for: INRequestRideIntent, with: (INSpeakableStringResolutionResult) -> Void)](./resolverideoptionname%28for,with%29.md)
  Resolves the user’s selected ride option.
- [func resolvePartySize(for: INRequestRideIntent, with: (INIntegerResolutionResult) -> Void)](./resolvepartysize%28for,with%29.md)
  Resolves the number of passengers for the ride.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inrequestrideintenthandling/resolvedropofflocation(for:with:))*