# location

**Framework**: MapKit  
**Kind**: property

The location of the device.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var location: CLLocation? { get }
```

## Mentions

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)

#### Discussion

This property contains `nil` if the map view isn’t showing the user’s location, or if the map view is still determining the user’s location.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [var isUpdating: Bool](mkuserlocation/isupdating.md)
  A Boolean value that indicates whether the map view is updating the user’s location.
- [var heading: CLHeading?](mkuserlocation/heading.md)
  The heading of the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkuserlocation/location)*