# CLPlacemark

**Framework**: Core Location  
**Kind**: class

A user-friendly description of a geographic coordinate, often containing the name of the place, its address, and other relevant information.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class CLPlacemark
```

## Mentions

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md)
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)

#### Overview

A `CLPlacemark` object stores placemark data for a given latitude and longitude. Placemark data includes information such as the country or region, state, city, and street address associated with the specified coordinate. It can also include points of interest and geographically related data.

When you reverse geocode a geographic coordinate using a [`CLGeocoder`](clgeocoder.md) object, you receive a [`CLPlacemark`](clplacemark.md) object containing the descriptive information for that location. You can also create [`CLPlacemark`](clplacemark.md) object and fill it with address information yourself, which you might do when you want to determine the geographic coordinate associated with the location.

## Topics

### Creating a placemark object
- [init(placemark: CLPlacemark)](clplacemark/init(placemark:).md)
  Initializes and returns a placemark object from another placemark object.
### Getting the placemark’s location
- [var location: CLLocation?](clplacemark/location.md)
  The location object containing latitude and longitude information.
- [var region: CLRegion?](clplacemark/region.md)
  The geographic region associated with the placemark.
### Getting the placemark name
- [var name: String?](clplacemark/name.md)
  The name of the placemark.
### Getting the placemark details
- [var thoroughfare: String?](clplacemark/thoroughfare.md)
  The street address associated with the placemark.
- [var subThoroughfare: String?](clplacemark/subthoroughfare.md)
  Additional street-level information for the placemark.
- [var locality: String?](clplacemark/locality.md)
  The city associated with the placemark.
- [var subLocality: String?](clplacemark/sublocality.md)
  Additional city-level information for the placemark.
- [var administrativeArea: String?](clplacemark/administrativearea.md)
  The state or province associated with the placemark.
- [var subAdministrativeArea: String?](clplacemark/subadministrativearea.md)
  Additional administrative area information for the placemark.
- [var postalCode: String?](clplacemark/postalcode.md)
  The postal code associated with the placemark.
### Getting the placemark’s country
- [var isoCountryCode: String?](clplacemark/isocountrycode.md)
  The abbreviated country or region name.
- [var country: String?](clplacemark/country.md)
  The name of the country or region associated with the placemark.
### Getting the associated contact details
- [var postalAddress: CNPostalAddress?](clplacemark/postaladdress.md)
  The postal address associated with the location, formatted for use with the Contacts framework.
- [var addressDictionary: [AnyHashable : Any]?](clplacemark/addressdictionary.md)
  A dictionary containing the Address Book keys and values for the placemark.
### Getting landscape information
- [var inlandWater: String?](clplacemark/inlandwater.md)
  The name of the inland water body associated with the placemark.
- [var ocean: String?](clplacemark/ocean.md)
  The name of the ocean associated with the placemark.
### Getting points of interest
- [var areasOfInterest: [String]?](clplacemark/areasofinterest.md)
  The relevant areas of interest associated with the placemark.
### Getting the placemark’s time zone
- [var timeZone: TimeZone?](clplacemark/timezone.md)
  The time zone associated with the placemark.
### Type Aliases
- [CLPlacemark.Specification](clplacemark/specification.md)
- [CLPlacemark.UnwrappedType](clplacemark/unwrappedtype.md)
- [CLPlacemark.ValueType](clplacemark/valuetype.md)
### Type Properties
- [static var defaultResolverSpecification: EmptyResolverSpecification<CLPlacemark>](clplacemark/defaultresolverspecification.md)
### Initializers
- [convenience init(location: CLLocation, name: String?, postalAddress: CNPostalAddress?)](clplacemark/init(location:name:postaladdress:).md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomLocalizedStringResourceConvertible](../Foundation/CustomLocalizedStringResourceConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [DisplayRepresentable](../AppIntents/DisplayRepresentable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [InstanceDisplayRepresentable](../AppIntents/InstanceDisplayRepresentable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [TypeDisplayRepresentable](../AppIntents/TypeDisplayRepresentable.md)

## See Also

- [Converting between coordinates and user-friendly place names](converting-between-coordinates-and-user-friendly-place-names.md)
  Convert between a latitude and longitude pair and a more user-friendly description of that location.
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [class CLGeocoder](clgeocoder.md)
  An interface for converting between geographic coordinates and place names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clplacemark)*