# MKMapFeatureAnnotation

**Framework**: MapKit  
**Kind**: class

A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class MKMapFeatureAnnotation
```

## Topics

### Customizing the annotation
- [var featureType: MKMapFeatureAnnotation.FeatureType](mkmapfeatureannotation/featuretype-swift.property.md)
  The type of map feature this annotation represents.
- [MKMapFeatureAnnotation.FeatureType](mkmapfeatureannotation/featuretype-swift.enum.md)
  Values that describe the kinds of features visible on the map.
- [var iconStyle: MKIconStyle?](mkmapfeatureannotation/iconstyle.md)
  The icon style of a feature annotation.
- [var pointOfInterestCategory: MKPointOfInterestCategory?](mkmapfeatureannotation/pointofinterestcategory.md)
  The feature annotation’s point of interest category.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MKAnnotation](mkannotation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [struct MKMapFeatureOptions](mkmapfeatureoptions.md)
  A structure you use to tell the map which kinds of features users can interact with.
- [class MKMapItemRequest](mkmapitemrequest.md)
  A utility class you use to request additional information about a map feature.
- [class MKIconStyle](mkiconstyle.md)
  A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [class MKPointOfInterestFilter](mkpointofinterestfilter.md)
  A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.
- [struct MKPointOfInterestCategory](mkpointofinterestcategory.md)
  A point of interest category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapfeatureannotation)*