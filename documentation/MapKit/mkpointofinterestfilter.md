# MKPointOfInterestFilter

**Framework**: MapKit  
**Kind**: class

A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class MKPointOfInterestFilter
```

#### Overview

You can apply a point of interest filter in a map view ([`pointOfInterestFilter`](mkmapview/pointofinterestfilter.md)), a local search request ([`pointOfInterestFilter`](mklocalsearchcompleter/pointofinterestfilter.md)), a search completer ([`pointOfInterestFilter`](mklocalsearchcompleter/pointofinterestfilter.md)), and in snapshot options ([`pointOfInterestFilter`](mkmapsnapshotter/options/pointofinterestfilter.md)).

## Topics

### Creating filters
- [class var excludingAll: MKPointOfInterestFilter](mkpointofinterestfilter/excludingall.md)
  A filter that excludes all point of interest categories.
- [class var includingAll: MKPointOfInterestFilter](mkpointofinterestfilter/includingall.md)
  A filter that includes all point of interest categories.
- [init(excluding: [MKPointOfInterestCategory])](mkpointofinterestfilter/init(excluding:).md)
  Initialize the point of interest filter with a list of categories to exclude.
- [init(including: [MKPointOfInterestCategory])](mkpointofinterestfilter/init(including:).md)
  Initialize the point of interest filter with a list of categories to include.
### Querying filter behavior
- [func excludes(MKPointOfInterestCategory) -> Bool](mkpointofinterestfilter/excludes(_:).md)
  Returns a Boolean value indicating whether the filter excludes the point of interest category.
- [func includes(MKPointOfInterestCategory) -> Bool](mkpointofinterestfilter/includes(_:).md)
  Returns a Boolean value indicating whether the filter includes the point of interest category.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapFeatureAnnotation](mkmapfeatureannotation.md)
  A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [struct MKMapFeatureOptions](mkmapfeatureoptions.md)
  A structure you use to tell the map which kinds of features users can interact with.
- [class MKMapItemRequest](mkmapitemrequest.md)
  A utility class you use to request additional information about a map feature.
- [class MKIconStyle](mkiconstyle.md)
  A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [struct MKPointOfInterestCategory](mkpointofinterestcategory.md)
  A point of interest category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter)*