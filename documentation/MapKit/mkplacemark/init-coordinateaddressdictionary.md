# init(coordinate:addressDictionary:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a placemark object using the specified coordinate and Address Book dictionary.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)
```

#### Return Value

An initialized `MKPlacemark` object.

#### Discussion

You can create placemark objects manually for entities for which you already have address information, such as contacts in the Address Book. Creating a placemark object explicitly avoids the need to query the reverse geocoder object for the same information.

## Parameters

- `coordinate`: The geographic coordinate to associate with the placemark.
- `addressDictionary`: A dictionary containing keys and values from an Address Book record. For a list of strings that you can use for the keys of this dictionary, see the “Address Property” constants in  . All of the keys in should be at the top level of the dictionary.

## See Also

- [Location and Maps Programming Guide](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/UserExperience/Conceptual/LocationAwarenessPG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40009497)
- [init(coordinate: CLLocationCoordinate2D)](mkplacemark/init(coordinate:).md)
  Creates and returns a placemark object using the specified coordinate.
- [init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)](mkplacemark/init(coordinate:postaladdress:).md)
  Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:addressdictionary:))*