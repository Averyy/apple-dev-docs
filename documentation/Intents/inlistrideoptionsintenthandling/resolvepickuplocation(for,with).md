# resolvePickupLocation(for:with:)

**Framework**: Intents  
**Kind**: method  
**Role**: Instance Method

Resolves the user’s pickup location.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- visionOS 1.0+
- watchOS 3.2+

## Declaration

```swift
optional func resolvePickupLocation(for intent: INListRideOptionsIntent, with completion: @escaping @Sendable (INPlacemarkResolutionResult) -> Void)
```

```swift
optional func resolvePickupLocation(for intent: INListRideOptionsIntent) async -> INPlacemarkResolutionResult
```

```objc
- (void) resolvePickupLocationForListRideOptions:(INListRideOptionsIntent *) intent withCompletion:(void (^)(INPlacemarkResolutionResult *resolutionResult)) completion;
```

#### Discussion

Implement this method to verify that you are able to pick up the user at the specified location. If you are unable to pick up the user at the requested location, you can provide a nearby location and ask the user to confirm the new value. You can also provide other resolutions as appropriate.

If you do not implement this method, SiriKit assumes you are able to pick up the user at the specified location.

Maps does not call this method. The Maps interface lets the user specify the pickup location explicitly, making resolution of that value unnecessary.

## Parameters

- `intent`: The intent object containing details about the user’s request. Use this object to get the initial information provided by the user.
- `completion`: The block to execute with the resolution. This block has no return value and takes the following parameter:

  - **resolutionResult**: The object containing the details of your proposed resolution. For successful resolutions, create a resolution object with the [`CLPlacemark`](../../CoreLocation/clplacemark.md) object with the user’s requested pickup location. This parameter must not be `nil`.

## See Also

### Resolving the Intent Parameters
- [func resolveDropOffLocation(for: INListRideOptionsIntent, with: (INPlacemarkResolutionResult) -> Void)](./resolvedropofflocation%28for,with%29.md)
  Resolves the user’s drop-off location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inlistrideoptionsintenthandling/resolvepickuplocation(for:with:))*