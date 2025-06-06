# center

**Framework**: Core Location  
**Kind**: property

The center point of the region.

**Availability**:
- macOS 10.7+
- watchOS 2.0+

## Declaration

```swift
var center: CLLocationCoordinate2D { get }
```

#### Discussion

In iOS, use a [`CLCircularRegion`](clcircularregion.md) object to manage geographic regions.

## See Also

- [init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](clregion/init(circularregionwithcenter:radius:identifier:).md)
  Initializes and returns a region object defining a circular area.
- [func contains(CLLocationCoordinate2D) -> Bool](clregion/contains(_:).md)
  Returns a Boolean value indicating whether the region contains the specified coordinate.
- [var radius: CLLocationDistance](clregion/radius.md)
  The radius (measured in meters) that defines the region’s outer boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/center)*