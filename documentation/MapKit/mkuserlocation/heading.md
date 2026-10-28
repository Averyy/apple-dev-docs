# heading

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The heading of the user’s location.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.9+

## Declaration

```swift
var heading: CLHeading? { get }
```

```objc
@property (nonatomic, readonly, nullable) CLHeading * heading;
```

## Discussion

This property is `nil` if the user’s location tracking mode isn’t [`MKUserTrackingMode.followWithHeading`](../mkusertrackingmode/followwithheading.md).

## See Also

### Determining the user’s location
- [var location: CLLocation?](./location.md)
  The location of the device.
- [var isUpdating: Bool](./isupdating.md)
  A Boolean value that indicates whether the map view is updating the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkuserlocation/heading)*