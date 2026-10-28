# mapRect

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

The map rectangle that describes the camera boundary.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var mapRect: MKMapRect { get }
```

```objc
@property (nonatomic, readonly) MKMapRect mapRect;
```

## Discussion

Both the [`mapRect`](./maprect.md) and the [`region`](./region.md) represent the same camera boundary.

## See Also

### Accessing the boundary
- [var region: MKCoordinateRegion](./region.md)
  The coordinate region that describes the camera boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class/maprect)*