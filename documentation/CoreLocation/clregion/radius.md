# radius

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The radius (measured in meters) that defines the region’s outer boundary.

**Availability**:
- macOS 10.7+ - Deprecated in 10.10
- watchOS 2.0+ - Deprecated in 2.0

> **Deprecated**: Use [`radius`](../clcircularregion/radius.md) in [`CLCircularRegion`](../clcircularregion.md) instead.

## Declaration

```swift
var radius: CLLocationDistance { get }
```

```objc
@property (atomic, readonly) CLLocationDistance radius;
```

#### Discussion

In iOS, use a [`CLCircularRegion`](../clcircularregion.md) object to manage geographic regions.

## See Also

### Deprecated
- [init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](./init%28circularregionwithcenter,radius,identifier%29.md)
  Initializes and returns a region object defining a circular area.
- [func contains(CLLocationCoordinate2D) -> Bool](./contains%28_%29.md)
  Returns a Boolean value indicating whether the region contains the specified coordinate.
- [var center: CLLocationCoordinate2D](./center.md)
  The center point of the region.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/radius)*