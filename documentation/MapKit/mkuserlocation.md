# MKUserLocation

**Framework**: MapKit  
**Kind**: class

An annotation that reflects the user’s location on the map.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
class MKUserLocation
```

## Mentions

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)

#### Overview

You don’t create instances of this class directly. Instead, you retrieve an existing `MKUserLocation` object from the [`userLocation`](mkmapview/userlocation.md) property of the map view that displays in your app.

## Topics

### Determining the user’s location
- [var location: CLLocation?](mkuserlocation/location.md)
  The location of the device.
- [var isUpdating: Bool](mkuserlocation/isupdating.md)
  A Boolean value that indicates whether the map view is updating the user’s location.
- [var heading: CLHeading?](mkuserlocation/heading.md)
  The heading of the user’s location.
### Accessing the user’s location annotation
- [var title: String?](mkuserlocation/title.md)
  The title to display for the user’s location annotation.
- [var subtitle: String?](mkuserlocation/subtitle.md)
  The subtitle to display for the user’s location annotation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [class MKUserLocationView](mkuserlocationview.md)
  A configurable annotation that shows the user’s location using the default MapKit style.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkuserlocation)*