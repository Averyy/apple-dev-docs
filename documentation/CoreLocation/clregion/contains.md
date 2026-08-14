# contains(_:)

**Framework**: Core Location  
**Kind**: method

Returns a Boolean value indicating whether the region contains the specified coordinate.

**Availability**:
- macOS 10.7+
- watchOS 2.0+

## Declaration

```swift
func contains(_ coordinate: CLLocationCoordinate2D) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if the coordinate lies within the region’s boundaries or [`false`](https://developer.apple.com/documentation/swift/false) if it does not.

#### Discussion

In iOS, use a [`CLCircularRegion`](clcircularregion.md) object to manage geographic regions.

## Parameters

- `coordinate`: The coordinate to test against the region.

## See Also

- [init(circularRegionWithCenter: CLLocationCoordinate2D, radius: CLLocationDistance, identifier: String)](clregion/init(circularregionwithcenter:radius:identifier:).md)
  Initializes and returns a region object defining a circular area.
- [var center: CLLocationCoordinate2D](clregion/center.md)
  The center point of the region.
- [var radius: CLLocationDistance](clregion/radius.md)
  The radius (measured in meters) that defines the region’s outer boundary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clregion/contains(_:))*