# init(origin:size:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates the map rectangle with the specified point and size.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
init(origin: MKMapPoint, size: MKMapSize)
```

## Parameters

- `origin`: The origin of the map rectangle as an [`MKMapPoint`](../mkmappoint.md).
- `size`: The size of the map rectangle as an [`MKMapSize`](../mkmapsize.md).

## See Also

### Creating a map rectangle
- [init()](./init%28%29.md)
  Creates the rectangle with an empty region.
- [init(x: Double, y: Double, width: Double, height: Double)](./init%28x,y,width,height%29.md)
  Creates a new map rectangle structure from the specified values.
- [init(MKMapRect)](../mkcoordinateregion/init%28_%29.md)
  Returns the region that corresponds to the specified map rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmaprect/init(origin:size:))*