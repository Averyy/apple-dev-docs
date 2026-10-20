# init(coordinate:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a LookAround scene at the specified coordinates.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D)
```

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate;
```

## Parameters

- `coordinate`: A [`CLLocationCoordinate2D`](../../CoreLocation/cllocationcoordinate2d.md) coordinate that indicates the location for the LookAround scene.

## See Also

### Creating a LookAround scene
- [init(mapItem: MKMapItem)](./init%28mapitem%29.md)
  Creates a LookAround scene with the location described by the specified map item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundscenerequest/init(coordinate:))*