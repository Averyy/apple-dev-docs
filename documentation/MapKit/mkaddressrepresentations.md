# MKAddressRepresentations

**Framework**: MapKit  
**Kind**: class

A class that provides formatted address strings.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
class MKAddressRepresentations
```

#### Discussion

Use this class to obtain formatted address strings for a place’s full address, city, or region.

## Topics

### Getting parts of an address
- [var cityName: String?](mkaddressrepresentations/cityname.md)
  The name of the city.
- [var cityWithContext: String?](mkaddressrepresentations/citywithcontext.md)
  The city name along with the country name, to provide additional disambiguating context.
- [var regionName: String?](mkaddressrepresentations/regionname.md)
  The region name, such as “United States”.
- [var region: Locale.Region?](mkaddressrepresentations/region.md)
### Getting a full address and city name
- [func fullAddress(includingRegion: Bool, singleLine: Bool) -> String?](mkaddressrepresentations/fulladdress(includingregion:singleline:).md)
  Returns the the location’s full address, optionally including the country or on a single link without line breaks.
- [func cityWithContext(MKAddressRepresentations.ContextStyle) -> String?](mkaddressrepresentations/citywithcontext(_:).md)
  The city name and, optionally and if applicable, state and region to provide additional disambiguating context.
### Controlling the degree of disambiguation to include in an address representation
- [MKAddressRepresentations.ContextStyle](mkaddressrepresentations/contextstyle.md)
  Values that describe the degree of disambiguation context to include in an address representation.

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

- [class MKMapItem](mkmapitem.md)
  A point of interest on the map.
- [class MKAddress](mkaddress.md)
  A class that contains a full address, and, optionally, a short address.
- [GeoToolbox](../GeoToolbox/GeoToolbox.md)
  Determine place descriptor information for map coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations)*