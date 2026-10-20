# init(mapRect:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a camera boundary using the provided map rectangle.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(mapRect: MKMapRect)
```

```objc
- (instancetype) initWithMapRect:(MKMapRect) mapRect;
```

## Parameters

- `mapRect`: The [`MKMapRect`](../../mkmaprect.md) that describes the camera boundary.

## See Also

### Creating a camera boundary
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a camera boundary using the provided coder.
- [init?(coordinateRegion: MKCoordinateRegion)](./init%28coordinateregion%29.md)
  Creates a camera boundary using the provided coordinate region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class/init(maprect:))*