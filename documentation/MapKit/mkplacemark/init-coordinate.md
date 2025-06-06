# init(coordinate:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a placemark object using the specified coordinate.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D)
```

#### Return Value

An initialized [`MKPlacemark`](mkplacemark.md) object.

#### Discussion

This method doesn’t fill in any of the other inherited properties describing the location.

## Parameters

- `coordinate`: The geographic coordinate to associate with the placemark.

## See Also

- [init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)](mkplacemark/init(coordinate:postaladdress:).md)
  Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.
- [init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)](mkplacemark/init(coordinate:addressdictionary:).md)
  Creates and returns a placemark object using the specified coordinate and Address Book dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:))*