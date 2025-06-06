# init(coordinate:postalAddress:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)
```

#### Return Value

An initialized [`MKPlacemark`](mkplacemark.md) object.

## Parameters

- `coordinate`: The geographic coordinate to associate with the placemark.
- `postalAddress`: An object containing the address information from the Contacts framework.

## See Also

- [init(coordinate: CLLocationCoordinate2D)](mkplacemark/init(coordinate:).md)
  Creates and returns a placemark object using the specified coordinate.
- [init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)](mkplacemark/init(coordinate:addressdictionary:).md)
  Creates and returns a placemark object using the specified coordinate and Address Book dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:postaladdress:))*