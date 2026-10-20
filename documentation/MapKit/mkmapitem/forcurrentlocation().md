# forCurrentLocation()

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (MKMapItem *) mapItemForCurrentLocation;
```

#### Return Value

An `MKMapItem` object representing the user’s location.

#### Discussion

For privacy reasons, and because the user’s location can change, the map item that this method returns doesn’t contain any coordinate data. When you need the actual location of the user, use the Core Location framework to retrieve it.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Creating map items
- [init(placemark: MKPlacemark)](./init%28placemark%29.md)
  Creates and returns a map item object using the specified placemark object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/forcurrentlocation())*