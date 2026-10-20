# init(mapItem:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a LookAround scene with the location described by the specified map item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(mapItem: MKMapItem)
```

```objc
- (instancetype) initWithMapItem:(MKMapItem *) mapItem;
```

## Parameters

- `mapItem`: An [`MKMapItem`](../mkmapitem.md) that describes the location for the LookAround scene.

## See Also

### Creating a LookAround scene
- [init(coordinate: CLLocationCoordinate2D)](./init%28coordinate%29.md)
  Creates a LookAround scene at the specified coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mklookaroundscenerequest/init(mapitem:))*