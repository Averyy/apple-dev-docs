# subtitleVisibility

**Framework**: MapKit JS  
**Kind**: property

A value that determines the behavior of the subtitle’s visibility.

**Availability**:
- MapKit JS 5.0+

## Declaration

```swift
attribute string subtitleVisibility;
```

#### Discussion

The subtitle visibility controls the subtitle that renders below the balloon part of the marker. The default value is [`Adaptive`](mapkit.featurevisibility/adaptive.md).

For adaptive visibility, the subtitle is always hidden in the normal state, by default. In the selected state, the subtitle follows the same rules as the title.

## See Also

- [titleVisibility](mapkit.markerannotation/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.
- [mapkit.FeatureVisibility](mapkit.featurevisibility.md)
  Constants indicating the visibility of different adaptive map features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.markerannotation/subtitlevisibility)*