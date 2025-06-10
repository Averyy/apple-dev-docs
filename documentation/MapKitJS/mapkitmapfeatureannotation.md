# mapkit.MapFeatureAnnotation

**Framework**: MapKit JS  
**Kind**: class

An object that represents a map feature that the user selects.

**Availability**:
- MapKit JS 5.74+

## Declaration

```swift
interface mapkit.MapFeatureAnnotation
```

#### Overview

MapKit JS creates a `MapFeatureAnnotation` when you set [`selectableMapFeatures`](mapkit.map/selectablemapfeatures.md), and when a person taps a map feature. The instance is available from the [`selectedAnnotation`](mapkit.map/selectedannotation.md) property when a person selects a map feature and MapKit JS passes it to the [`annotationForMapFeature`](mapkit.map/annotationformapfeature.md) delegate method.

MapKit JS removes the annotation as soon as a person deselects the map feature.

## Topics

### Annotation properties
- [title](mapkit.mapfeatureannotation/title.md)
  The title of the feature.
- [featureType](mapkit.mapfeatureannotation/featuretype.md)
  A value that describes the type of place the feature represents.
- [pointOfInterestCategory](mapkit.mapfeatureannotation/pointofinterestcategory.md)
  The point-of-interest category of the feature.
- [id](mapkit.mapfeatureannotation/id.md)
  The Place ID referencing the feature.
- [color](mapkit.mapfeatureannotation/color.md)
  The color of the map feature.
- [glyphImage](mapkit.mapfeatureannotation/glyphimage.md)
  The glyph image for the feature.
- [selectedGlyphImage](mapkit.mapfeatureannotation/selectedglyphimage.md)
  The glyph image for the selected feature.
### Fetching places
- [fetchPlace](mapkit.mapfeatureannotation/fetchplace.md)
  Fetches the place object associated with the map feature.

## Relationships

### Inherited By
- [mapkit.PlaceAnnotation](mapkit.placeannotation.md)

## See Also

- [mapkit.filterExcludingAllCategories](mapkit/mapkit.filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [mapkit.filterIncludingAllCategories](mapkit/mapkit.filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [mapkit.PointOfInterestFilter](mapkit.pointofinterestfilter.md)
  A filter for determining the points of interest to include or exclude on a map or in a local search.
- [mapkit.PointsOfInterestSearch](mapkit.pointsofinterestsearch.md)
  An object that fetches points of interest within a specified region.
- [mapkit.MapFeatureAnnotationGlyphImage](mapkit.mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [mapkit.PointOfInterestCategory](mapkit.pointofinterestcategory.md)
  Point-of-interest categories.
- [mapkit.MapFeatureType](mapkit.mapfeaturetype.md)
  Values that describe the feature type of a point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapkit.mapfeatureannotation)*