# init(coordinateRegion:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a camera boundary using the provided coordinate region.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init?(coordinateRegion region: MKCoordinateRegion)
```

```objc
- (instancetype) initWithCoordinateRegion:(MKCoordinateRegion) region;
```

## Parameters

- `region`: The [`MKCoordinateRegion`](../../mkcoordinateregion.md) region that describes the camera boundary.

## See Also

### Creating a camera boundary
- [init?(coder: NSCoder)](./init%28coder%29.md)
  Creates a camera boundary using the provided coder.
- [init?(mapRect: MKMapRect)](./init%28maprect%29.md)
  Creates a camera boundary using the provided map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview/cameraboundary-swift.class/init(coordinateregion:))*