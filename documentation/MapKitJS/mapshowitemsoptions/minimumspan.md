# minimumSpan

**Framework**: MapKit JS  
**Kind**: property

The minimum longitudinal and latitudinal span the map displays.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
minimumSpan?: CoordinateSpan;
```

#### Discussion

Set this value to ensure that [`showItems(items, options)`](map/showitems.md) sets a map region no smaller than the minimum span specified.

## See Also

- [animate](mapshowitemsoptions/animate.md)
  A Boolean value that determines whether the map animates as the map region changes to show the items.
- [padding](mapshowitemsoptions/padding.md)
  Spacing that the framework adds around the computed map region when showing items.
- [cameraDistance](mapshowitemsoptions/cameradistance.md)
  The distance from the center of the map to the camera, when showing the items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapshowitemsoptions/minimumspan)*