# center

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The center point of the region.

**Availability**:
- macOS 10.7+ - Deprecated in 10.10
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`center`](../clcircularregion/center.md) in [`CLCircularRegion`](../clcircularregion.md) instead.

## Declaration

```swift
var center: CLLocationCoordinate2D { get }
```

```objc
@property (atomic, readonly) CLLocationCoordinate2D center;
```

## Discussion

In iOS, use a [`CLCircularRegion`](../clcircularregion.md) object to manage geographic regions.

## See Also

### Deprecated
- [init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](./init%28circularregionwithcenter,radius,identifier%29.md)
  Initializes and returns a region object defining a circular area.
- [func contains(CLLocationCoordinate2D) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the region contains the specified coordinate.
- [var radius: CLLocationDistance](./radius.md)
  The radius (measured in meters) that defines the region’s outer boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/center)*