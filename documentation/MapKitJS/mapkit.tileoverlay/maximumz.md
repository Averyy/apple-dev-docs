# maximumZ

**Framework**: MapKit JS  
**Kind**: property

The maximum zoom level for a tile overlay.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute number maximumZ;
```

#### Discussion

The `maximumZ` value defaults to the maximum zoom level of MapKit JS tiles. The zoom level can go higher and expands the map’s zoom range, if necessary. MapKit JS requests the overlay tiles when the map is below or at this zoom level.

The default value is `null`.

## See Also

- [opacity](mapkit.tileoverlay/opacity.md)
  A number that indicates a tile’s opacity.
- [minimumZ](mapkit.tileoverlay/minimumz.md)
  The minimum zoom level for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.tileoverlay/maximumz)*