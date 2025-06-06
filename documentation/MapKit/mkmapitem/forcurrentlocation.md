# forCurrentLocation()

**Framework**: MapKit  
**Kind**: method

Creates and returns a singleton map item object representing the user’s location.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func forCurrentLocation() -> MKMapItem
```

#### Return Value

An `MKMapItem` object representing the user’s location.

#### Discussion

For privacy reasons, and because the user’s location can change, the map item that this method returns doesn’t contain any coordinate data. When you need the actual location of the user, use the Core Location framework to retrieve it.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [init(placemark: MKPlacemark)](mkmapitem/init(placemark:).md)
  Creates and returns a map item object using the specified placemark object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/forcurrentlocation())*