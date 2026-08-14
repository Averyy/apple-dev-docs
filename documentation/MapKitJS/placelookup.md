# PlaceLookup

**Framework**: MapKit JS  
**Kind**: class

An object that provides the ability to look up place information for a specified Place ID.

**Availability**:
- MapKit JS 5.78.1+

## Declaration

```swift
class PlaceLookup extends Service
```

#### Overview

For more information on places, see [`Identifying unique locations with Place IDs`](https://developer.apple.com/documentation/mapkit/identifying-unique-locations-with-place-ids).

## Topics

### Creating a place lookup
- [new PlaceLookup(options)](placelookup/placelookupconstructor.md)
  Creates a place lookup with a set of options.
### Getting a place
- [getPlace(id, options)](placelookup/getplace.md)
  Obtains a place using its identifier.
- [getPlace(annotation, options)](placelookup/getplace1.md)
  Obtains the place associated with a map feature annotation.
- [interface PlaceLookupOptions](placelookupoptions.md)
  Options for place lookup requests.
### Deprecated
- [getPlace(id, callback, options)](placelookup/getplace2.md)
  Obtains a place using its identifier.

## Relationships

### Inherits From
- [Service](service.md)

## See Also

- [class Place](place.md)
  A place object that returns from a geocoder lookup, a reverse lookup, or a fetch request for points of interest.
- [placeDetails](mapkit/placedetails.md)
  A list of all place detail objects that are currently active on a page.
- [interface PlaceSelectionAccessoryOptions](placeselectionaccessoryoptions.md)
  The options for selection accessories.
- [class PlaceAnnotation](placeannotation.md)
  An annotation for a place.
- [class PlaceDetail](placedetail.md)
  An interactive view that displays information about a place.
- [class PlaceSelectionAccessory](placeselectionaccessory.md)
  The accessory that conveys information about a place associated with an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkitjs/placelookup)*