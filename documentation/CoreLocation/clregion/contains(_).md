# contains(_:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Returns a Boolean value indicating whether the region contains the specified coordinate.

**Availability**:
- macOS 10.7+ - Deprecated in 10.10
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`contains(_:)`](../clcircularregion/contains%28_%29.md) in [`CLCircularRegion`](../clcircularregion.md) instead.

## Declaration

```swift
func contains(_ coordinate: CLLocationCoordinate2D) -> Bool
```

```objc
- (BOOL) containsCoordinate:(CLLocationCoordinate2D) coordinate;
```

#### Return Value

[`true`](../../Swift/true.md) if the coordinate lies within the region’s boundaries or [`false`](../../Swift/false.md) if it does not.

#### Discussion

In iOS, use a [`CLCircularRegion`](../clcircularregion.md) object to manage geographic regions.

## Parameters

- `coordinate`: The coordinate to test against the region.

## See Also

### Deprecated
- [init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](./init%28circularregionwithcenter,radius,identifier%29.md)
  Initializes and returns a region object defining a circular area.
- [var center: CLLocationCoordinate2D](./center.md)
  The center point of the region.
- [var radius: CLLocationDistance](./radius.md)
  The radius (measured in meters) that defines the region’s outer boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/contains(_:))*