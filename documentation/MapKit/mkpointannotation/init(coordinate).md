# init(coordinate:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates a point annotation at the specified coordinate on the map.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
convenience init(coordinate: CLLocationCoordinate2D)
```

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate;
```

## Parameters

- `coordinate`: The coordinate containing the latitude and longitude values for the desired point.

## See Also

### Creating a Point Annotation
- [init()](./init%28%29.md)
  Creates a map annotation that shows a title string at a point on a map.
- [convenience init(coordinate: CLLocationCoordinate2D, title: String?, subtitle: String?)](./init%28coordinate,title,subtitle%29.md)
  Creates a point annotation displaying a title and subtitle string at the specified coordinate on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointannotation/init(coordinate:))*