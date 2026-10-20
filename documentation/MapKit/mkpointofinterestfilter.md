# MKPointOfInterestFilter

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class MKPointOfInterestFilter
```

```objc
@interface MKPointOfInterestFilter : NSObject
```

#### Overview

You can apply a point of interest filter in a map view ([`pointOfInterestFilter`](./mkmapview/pointofinterestfilter.md)), a local search request ([`pointOfInterestFilter`](./mklocalsearchcompleter/pointofinterestfilter.md)), a search completer ([`pointOfInterestFilter`](./mklocalsearchcompleter/pointofinterestfilter.md)), and in snapshot options ([`pointOfInterestFilter`](./mkmapsnapshotter/options/pointofinterestfilter.md)).

## Topics

### Creating filters
- [class var excludingAll: MKPointOfInterestFilter](./mkpointofinterestfilter/excludingall.md)
  A filter that excludes all point of interest categories.
- [class var includingAll: MKPointOfInterestFilter](./mkpointofinterestfilter/includingall.md)
  A filter that includes all point of interest categories.
- [init(excluding: [MKPointOfInterestCategory])](./mkpointofinterestfilter/init%28excluding%29.md)
  Initialize the point of interest filter with a list of categories to exclude.
- [init(including: [MKPointOfInterestCategory])](./mkpointofinterestfilter/init%28including%29.md)
  Initialize the point of interest filter with a list of categories to include.
### Querying filter behavior
- [func excludes(MKPointOfInterestCategory) -> Bool](./mkpointofinterestfilter/excludes%28_%29.md)
  Returns a Boolean value indicating whether the filter excludes the point of interest category.
- [func includes(MKPointOfInterestCategory) -> Bool](./mkpointofinterestfilter/includes%28_%29.md)
  Returns a Boolean value indicating whether the filter includes the point of interest category.
### Initializers
- [init?(coder: NSCoder)](./mkpointofinterestfilter/init%28coder%29.md)
- [init(excludingCategories: [MKPointOfInterestCategory])](./mkpointofinterestfilter/init%28excludingcategories%29.md)
- [init(includingCategories: [MKPointOfInterestCategory])](./mkpointofinterestfilter/init%28includingcategories%29.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Points of interest
- [Identifying unique locations with Place IDs](./identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapFeatureAnnotation](./mkmapfeatureannotation.md)
  A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [struct MKMapFeatureOptions](./mkmapfeatureoptions.md)
  A structure you use to tell the map which kinds of features users can interact with.
- [class MKMapItemRequest](./mkmapitemrequest.md)
  A utility class you use to request additional information about a map feature.
- [class MKIconStyle](./mkiconstyle.md)
  A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [struct MKPointOfInterestCategory](./mkpointofinterestcategory.md)
  A point of interest category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkpointofinterestfilter)*