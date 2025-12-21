# minimumZ

**Framework**: MapKit JS  
**Kind**: property

The minimum zoom level for a tile overlay.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
get minimumZ(): number | null;
set minimumZ(minimumZ: number | null);
```

#### Discussion

By default, the minimum zoom level for a tile overlay is the same as the minimum zoom level for MapKit JS built-in tiles. MapKit JS requests the overlay tiles when the map is above or at this zoom level.

The default value is `null`.

## See Also

- [opacity](tileoverlay/opacity.md)
  A number that indicates a tile’s opacity.
- [maximumZ](tileoverlay/maximumz.md)
  The maximum zoom level for a tile overlay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/tileoverlay/minimumz)*