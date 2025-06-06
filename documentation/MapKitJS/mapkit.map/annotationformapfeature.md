# annotationForMapFeature

**Framework**: MapKit JS  
**Kind**: method

The method MapKit JS calls when the framework creates a map feature annotation.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
void annotationForMapFeature(
	mapkit.MapFeatureAnnotation mapFeatureAnnotation
);
```

#### Discussion

You can choose to return the annotation the method provides with modified properties, or provide a new annotation to represent the map feature. If an annotation doesn’t return, MapKit JS uses the default annotation.

## See Also

- [selectableMapFeatures](mapkit.map/selectablemapfeatures.md)
  An array of map features that users can select from the map.
- [selectableMapFeatureSelectionAccessory](mapkit.map/selectablemapfeatureselectionaccessory.md)
  An accessory for displaying place information when a person selects a map feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.map/annotationformapfeature)*