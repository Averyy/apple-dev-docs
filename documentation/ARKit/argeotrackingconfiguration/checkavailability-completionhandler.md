# checkAvailability(completionHandler:)

**Framework**: ARKit  
**Kind**: method

Determines if geotracking supports the user’s current location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+

## Declaration

```swift
class func checkAvailability(completionHandler: @escaping (Bool, (any Error)?) -> Void)
```

#### Discussion

This function returns [`false`](https://developer.apple.com/documentation/Swift/false) under the following circumstances:

- ARKit lacks localization imagery for the user’s geographic position.
- A network connection is unavailable to download localization imagery.
- The device lacks cellular (GPS) capability.

To determine availability at a different location than the device’s current location, call [`checkAvailability(at:completionHandler:)`](argeotrackingconfiguration/checkavailability(at:completionhandler:).md) instead.

For a list of supported areas and cities, see [`ARGeoTrackingConfiguration`](argeotrackingconfiguration.md).

## Parameters

- `completionHandler`: Code you supply that runs after the function returns. The closure takes a Boolean argument that indicates whether geotracking is available.

## See Also

- [class func checkAvailability(at: CLLocationCoordinate2D, completionHandler: (Bool, (any Error)?) -> Void)](argeotrackingconfiguration/checkavailability(at:completionhandler:).md)
  Determines if geotracking supports a particular location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/argeotrackingconfiguration/checkavailability(completionhandler:))*