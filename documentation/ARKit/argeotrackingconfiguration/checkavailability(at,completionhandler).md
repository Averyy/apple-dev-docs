# checkAvailability(at:completionHandler:)

**Framework**: ARKit  
**Kind**: method  
**Role**: Type Method

Determines if geotracking supports a particular location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+

## Declaration

```swift
class func checkAvailability(at coordinate: CLLocationCoordinate2D, completionHandler: @escaping (Bool, (any Error)?) -> Void)
```

```objc
+ (void) checkAvailabilityAtCoordinate:(CLLocationCoordinate2D) coordinate completionHandler:(void (^)(BOOL isAvailable, NSError *error)) completionHandler;
```

#### Discussion

This function returns [`false`](../../Swift/false.md) under the following circumstances:

- ARKit lacks localization imagery for the argument GPS coordinate.
- A network connection is unavailable to download localization imagery.
- The device lacks cellular (GPS) capability.

To determine availability at the user’s GPS coordinate, use [`checkAvailability(completionHandler:)`](./checkavailability%28completionhandler%29.md) instead.

For a list of supported areas and cities, see [`ARGeoTrackingConfiguration`](../argeotrackingconfiguration.md).

## Parameters

- `coordinate`: The GPS location that the framework checks for availability.
- `completionHandler`: Code you supply that runs after the function returns. The closure takes a  Boolean argument that indicates whether geotracking is available.

## See Also

### Checking availability
- [class func checkAvailability(completionHandler: (Bool, (any Error)?) -> Void)](./checkavailability%28completionhandler%29.md)
  Determines if geotracking supports the user’s current location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration/checkavailability(at:completionhandler:))*