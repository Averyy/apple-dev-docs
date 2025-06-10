# MKMapItemRequest

**Framework**: MapKit  
**Kind**: class

A utility class you use to request additional information about a map feature.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 1.0+
- watchOS 11.0+

## Declaration

```swift
class MKMapItemRequest
```

## Mentions

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)

## Topics

### Creating a request
- [convenience init(feature: MapFeature)](mkmapitemrequest/init(feature:).md)
  Creates a new map item request with the specified map feature.
- [init(mapItemIdentifier: MKMapItem.Identifier)](mkmapitemrequest/init(mapitemidentifier:).md)
  Create a request with a map item identifier.
- [init(mapFeatureAnnotation: MKMapFeatureAnnotation)](mkmapitemrequest/init(mapfeatureannotation:).md)
  Creates a new map item request with the specified feature annotation.
### Configuring the item request
- [var mapFeature: MapFeature?](mkmapitemrequest/mapfeature.md)
  The map feature.
- [var mapFeatureAnnotation: MKMapFeatureAnnotation?](mkmapitemrequest/mapfeatureannotation.md)
  The feature annotation.
- [var mapItemIdentifier: MKMapItem.Identifier?](mkmapitemrequest/mapitemidentifier.md)
  The map item identifer.
- [var feature: MapFeature](mkmapitemrequest/feature.md)
  The map feature.
- [var featureAnnotation: MKMapFeatureAnnotation](mkmapitemrequest/featureannotation.md)
  The feature annotation.
- [var placeDescriptor: PlaceDescriptor?](mkmapitemrequest/placedescriptor.md)
  The place descriptor that contains information that’s helpful in uniquely identifying this place.
### Starting and stopping requests
- [func cancel()](mkmapitemrequest/cancel.md)
  Cancels an in-progress map item request.
- [func getMapItem(completionHandler: (MKMapItem?, (any Error)?) -> Void)](mkmapitemrequest/getmapitem(completionhandler:).md)
  Requests a map item and calls the provided completion handler.
### Checking the status of a request
- [var isCancelled: Bool](mkmapitemrequest/iscancelled.md)
  A Boolean value that indicates if the cancellation of the request was successful.
- [var isLoading: Bool](mkmapitemrequest/isloading.md)
  A Boolean value that indicates if the request is loading.
### Initializers
- [convenience init(placeDescriptor: PlaceDescriptor)](mkmapitemrequest/init(placedescriptor:).md)
  Creates a new map item request with the specified place descriptor

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapFeatureAnnotation](mkmapfeatureannotation.md)
  A class that describes an annotation element on the map’s display such as a point of interest, territorial boundary, or physical feature.
- [struct MKMapFeatureOptions](mkmapfeatureoptions.md)
  A structure you use to tell the map which kinds of features users can interact with.
- [class MKIconStyle](mkiconstyle.md)
  A class you use to customize the annotation view icon of a point of interest (POI) on the map.
- [class MKPointOfInterestFilter](mkpointofinterestfilter.md)
  A filter that includes or excludes point of interest categories from a map view, local search, or local search completer.
- [struct MKPointOfInterestCategory](mkpointofinterestcategory.md)
  A point of interest category.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitemrequest)*