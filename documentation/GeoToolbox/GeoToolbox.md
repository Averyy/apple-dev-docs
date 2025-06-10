# GeoToolbox

**Framework**: GeoToolbox  
**Kind**: module

Determine place descriptor information for map coordinates.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

#### Overview

Use `GeoToolbox` to create `PlaceDescriptor` structures for use across Maps technologies and third-party mapping systems.

## Topics

### Getting rich information about a place
- [struct PlaceDescriptor](placedescriptor.md)
  A structure that contains identifying information about a place that a mapping service may use to attempt to find rich place information such as phone numbers, websites, and so on.
### Creating a place descriptor
- [init?(item: MKMapItem)](placedescriptor/init(item:).md)
  Creates a place descriptor from a map item.
- [init(representations: [PlaceDescriptor.PlaceRepresentation], commonName: String?, supportingRepresentations: [PlaceDescriptor.SupportingPlaceRepresentation])](placedescriptor/init(representations:commonname:supportingrepresentations:).md)
  Creates a place descriptor, suitable for use when searching or retrieving rich data about a place.
### Values that describe places and mapping service providers
- [PlaceDescriptor.PlaceRepresentation](placedescriptor/placerepresentation.md)
  Values that represent a physical place, suitable for use when searching or retrieving rich data.
- [PlaceDescriptor.SupportingPlaceRepresentation](placedescriptor/supportingplacerepresentation.md)
  Values that describe the representation of a physical place using proprietary attributes, such as an alphanumeric location identifier from a mapping service provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/GeoToolbox)*