# equals(anotherPoint)

**Framework**: MapKit JS  
**Kind**: method

Indicates whether two map points are equal.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
equals(anotherPoint: MapPoint): boolean;
```

#### Return Value

Returns `true` if the `x` and `y` values of the map point exactly match the corresponding values of `anotherPoint`. Returns `false` if the values aren’t an exact match.

## Parameters

- `anotherPoint`: A map location to use for comparison.

## See Also

- [copy()](mappoint/copy.md)
  Returns a copy of the location.
- [toCoordinate()](mappoint/tocoordinate.md)
  Converts a map point into a coordinate with latitude and longitude.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mappoint/equals)*