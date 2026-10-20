# MKAddress

**Framework**: MapKit  
**Kind**: class  
**Role**: Class

A class that contains a full address, and, optionally, a short address.

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
class MKAddress
```

```objc
@interface MKAddress : NSObject
```

#### Discussion

MapKit capabilities, such as Search and Reverse geocoding, populate the [`MKAddress`](./mkaddress.md) of a [`MKMapItem`](./mkmapitem.md) with a full address, and a short address, if the framework has one.

When presenting a Place Card using an [`MKMapItemDetailViewController`](./mkmapitemdetailviewcontroller.md) or a selection accessory on an annotation you created using an [`MKMapItem`](./mkmapitem.md), MapKit uses the full address provided if you create the `MKMapitem` using [`init(location:address:)`](./mkmapitem/init%28location,address%29.md).

## Topics

### Creating an address
- [init?(fullAddress: String, shortAddress: String?)](./mkaddress/init%28fulladdress,shortaddress%29.md)
  Initializes a new address with a location’s full address using a string and a short address that provides an abbreviated form of the address such as a street address.
### Getting the full and short addresses
- [var fullAddress: String](./mkaddress/fulladdress.md)
  A string that represents a place’s full address
- [var shortAddress: String?](./mkaddress/shortaddress.md)
  A  string that represents the short address of a location, such as it’s street address and city.

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
- [class MKAddressRepresentations](./mkaddressrepresentations.md)
  A class that provides formatted address strings.
- [GeoToolbox](../GeoToolbox/GeoToolbox.md)
  Determine place descriptor information for map coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkaddress)*