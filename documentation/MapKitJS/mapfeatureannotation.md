# MapFeatureAnnotation

**Framework**: MapKit JS  
**Kind**: class

An object that represents a map feature that the user selects.

**Availability**:
- MapKit JS 5.74.1+

## Declaration

```swift
class MapFeatureAnnotation extends PlaceAnnotation
```

#### Overview

MapKit JS creates a `MapFeatureAnnotation` when you set [`selectableMapFeatures`](map/selectablemapfeatures.md), and when a person taps a map feature. The instance is available from the [`selectedAnnotation`](map/selectedannotation.md) property when a person selects a map feature and MapKit JS passes it to the [`annotationForMapFeature`](map/annotationformapfeature.md) delegate method.

MapKit JS removes the annotation as soon as a person deselects the map feature.

## Topics

### Annotation properties
- [title](mapfeatureannotation/title.md)
  The title of the feature.
- [featureType](mapfeatureannotation/featuretype.md)
  A value that describes the type of place the feature represents.
- [pointOfInterestCategory](mapfeatureannotation/pointofinterestcategory.md)
  The point-of-interest category of the feature.
- [color](placeannotation/color.md)
  The color of the place.
- [glyphImage](placeannotation/glyphimage.md)
  The glyph image for the place.
- [selectedGlyphImage](placeannotation/selectedglyphimage.md)
  The selected glyph image for the place.
### Fetching places
- [fetchPlace(callback)](mapfeatureannotation/fetchplace.md)
  Fetches the place object associated with the map feature.
### Instance Properties
- [accessibilityLabel](mapfeatureannotation/accessibilitylabel.md)
  The accessibility label for the annotation.
- [collisionMode](mapfeatureannotation/collisionmode.md)
  A value that determines how the map handles collisions between annotations.
- [map](mapfeatureannotation/map.md)
  The map that the annotation is on.
- [subtitle](mapfeatureannotation/subtitle.md)
  The subtitle of the feature.
- [subtitleVisibility](mapfeatureannotation/subtitlevisibility.md)
  A value that determines the subtitle’s visibility.
- [titleVisibility](mapfeatureannotation/titlevisibility.md)
  A value that determines the behavior of the title’s visibility.

## Relationships

### Inherits From
- [PlaceAnnotation](placeannotation.md)

## See Also

- [filterExcludingAllCategories](mapkit/filterexcludingallcategories.md)
  A value that excludes all point-of-interest categories.
- [filterIncludingAllCategories](mapkit/filterincludingallcategories.md)
  A value that includes all point-of-interest categories.
- [class PointOfInterestFilter](pointofinterestfilter.md)
  A filter for determining the points of interest to include or exclude on a map or in a local search.
- [class PointsOfInterestSearch](pointsofinterestsearch.md)
  An object that fetches points of interest within a specified region.
- [class MapFeatureAnnotationGlyphImage](mapfeatureannotationglyphimage.md)
  An object that describes map feature annotation images.
- [const PointOfInterestCategory](pointofinterestcategory.md)
  Point-of-interest categories.
- [const MapFeatureType](mapfeaturetype.md)
  Values that describe the feature type of a point of interest.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/mapfeatureannotation)*