# MKAddressRepresentations

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A class that provides formatted address strings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
class MKAddressRepresentations
```

```objc
@interface MKAddressRepresentations : NSObject
```

## Discussion

Use this class to obtain formatted address strings for a place’s full address, city, or region.

## Topics

### Getting parts of an address
- [var cityName: String?](./mkaddressrepresentations/cityname.md)
  The name of the city.
- [var cityWithContext: String?](./mkaddressrepresentations/citywithcontext.md)
  The city name along with the country name, to provide additional disambiguating context.
- [var regionName: String?](./mkaddressrepresentations/regionname.md)
  The region name, such as “United States”.
- [var region: Locale.Region?](./mkaddressrepresentations/region.md)
- [regionCode](./mkaddressrepresentations/regioncode.md)
  The region’s ISO 3166-2 region code, such as “US”.
### Getting a full address and city name
- [func fullAddress(includingRegion: Bool, singleLine: Bool) -> String?](./mkaddressrepresentations/fulladdress%28includingregion,singleline%29.md)
  Returns the the location’s full address, optionally including the country or on a single link without line breaks.
- [func cityWithContext(MKAddressRepresentations.ContextStyle) -> String?](./mkaddressrepresentations/citywithcontext%28_%29.md)
  The city name and, optionally and if applicable, state and region to provide additional disambiguating context.
### Controlling the degree of disambiguation to include in an address representation
- [MKAddressRepresentations.ContextStyle](./mkaddressrepresentations/contextstyle.md)
  Values that describe the degree of disambiguation context to include in an address representation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Representing places and addresses
- [class MKMapItem](./mkmapitem.md)
  A point of interest on the map.
- [class MKAddress](./mkaddress.md)
  A class that contains a full address, and, optionally, a short address.
- [GeoToolbox](../GeoToolbox/GeoToolbox.md)
  Determine place descriptor information for map coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddressrepresentations)*