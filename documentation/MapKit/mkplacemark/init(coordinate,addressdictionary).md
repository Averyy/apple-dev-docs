# init(coordinate:addressDictionary:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a placemark object using the specified coordinate and Address Book dictionary.

**Availability**:
- iOS 3.0+ - Deprecated in 26.0
- iPadOS 3.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use MKMapItem's location, address and addressRepresentations properties instead. Use MKAddressRepresentations for formatted address strings for MapKit provided MKMapItems

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)
```

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate addressDictionary:(NSDictionary<NSString *,id> *) addressDictionary;
```

#### Return Value

An initialized `MKPlacemark` object.

#### Discussion

You can create placemark objects manually for entities for which you already have address information, such as contacts in the Address Book. Creating a placemark object explicitly avoids the need to query the reverse geocoder object for the same information.

## Parameters

- `coordinate`: The geographic coordinate to associate with the placemark.
- `addressDictionary`: A dictionary containing keys and values from an Address Book record. For a list of strings that you can use for the keys of this dictionary, see the “Address Property” constants in `ABPerson`. All of the keys in should be at the top level of the dictionary.

## See Also

### Related Documentation
- [Location and Maps Programming Guide](https://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
### Creating a placemark object
- [init(coordinate: CLLocationCoordinate2D)](./init%28coordinate%29.md)
  Creates and returns a placemark object using the specified coordinate.
- [init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)](./init%28coordinate,postaladdress%29.md)
  Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:addressdictionary:))*