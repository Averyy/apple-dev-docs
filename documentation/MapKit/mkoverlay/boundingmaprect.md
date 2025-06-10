# boundingMapRect

**Framework**: MapKit  
**Kind**: property  
**Required**: Yes

The projected rectangle that encompasses the overlay.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var boundingMapRect: MKMapRect { get }
```

#### Discussion

This property contains the smallest rectangle that completely encompasses the overlay. Implementers of this protocol need to set this area when implementing their overlay class, and after setting it, not change it. Specify the rectangle using projected coordinates — that is, coordinates you obtain by projecting the globe onto a two-dimensional surface.

## See Also

- [var coordinate: CLLocationCoordinate2D](mkoverlay/coordinate.md)
  The approximate center point of the overlay area.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkoverlay/boundingmaprect)*