# coordinate

**Framework**: MapKit  
**Kind**: property  
**Required**: Yes

The approximate center point of the overlay area.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
var coordinate: CLLocationCoordinate2D { get }
```

#### Discussion

This point is typically set to the center point of the map’s bounding rectangle. The overlay uses it as the anchor point for any callouts that display for the annotation.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [var boundingMapRect: MKMapRect](mkoverlay/boundingmaprect.md)
  The projected rectangle that encompasses the overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlay/coordinate)*