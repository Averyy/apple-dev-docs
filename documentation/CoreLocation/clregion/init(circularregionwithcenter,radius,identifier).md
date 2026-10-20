# init(circularRegionWithCenter:radius:identifier:)

**Framework**: Core Location  
**Kind**: init  
**Role**: Initializer

Initializes and returns a region object defining a circular area.

**Availability**:
- macOS 10.7+ - Deprecated in 10.10
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`init(center:radius:identifier:)`](../clcircularregion/init%28center,radius,identifier%29.md) in [`CLCircularRegion`](../clcircularregion.md) instead.

## Declaration

```swift
init(circularRegionWithCenter center: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)
```

```objc
- (instancetype) initCircularRegionWithCenter:(CLLocationCoordinate2D) center radius:(CLLocationDistance) radius identifier:(NSString *) identifier;
```

#### Return Value

An initialized region object.

#### Discussion

In iOS, use a [`CLCircularRegion`](../clcircularregion.md) object to manage geographic regions.

## Parameters

- `center`: The center point of the region.
- `radius`: The distance (measured in meters) from the center point that marks the boundary of the region.
- `identifier`: A unique identifier to associate with the region object. You use this identifier to differentiate regions within your application. This value must not be `nil`.

## See Also

### Deprecated
- [func contains(CLLocationCoordinate2D) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the region contains the specified coordinate.
- [var center: CLLocationCoordinate2D](./center.md)
  The center point of the region.
- [var radius: CLLocationDistance](./radius.md)
  The radius (measured in meters) that defines the region’s outer boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/init(circularregionwithcenter:radius:identifier:))*