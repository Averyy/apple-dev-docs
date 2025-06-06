# titleVisibility

**Framework**: MapKit JS  
**Kind**: property

A value that determines the behavior of the title’s visibility.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string titleVisibility;
```

#### Discussion

The title visibility controls the title that renders below the balloon part of the marker. The default value is [`Adaptive`](mapkit.featurevisibility/adaptive.md).

For adaptive visibility, the title is always visible in the normal state, by default. When the user selects the marker, the title is visible unless the marker’s selected state requires a callout.

## See Also

- [subtitleVisibility](mapkit.markerannotation/subtitlevisibility.md)
  A value that determines the behavior of the subtitle’s visibility.
- [mapkit.FeatureVisibility](mapkit.featurevisibility.md)
  Constants indicating the visibility of different adaptive map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.markerannotation/titlevisibility)*