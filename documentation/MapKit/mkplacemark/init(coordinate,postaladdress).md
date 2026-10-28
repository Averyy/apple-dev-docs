# init(coordinate:postalAddress:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.

**Availability**:
- iOS 10.0+ - Deprecated in 26.0
- iPadOS 10.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.12+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)
```

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate postalAddress:(CNPostalAddress *) postalAddress;
```

## Return Value

An initialized [`MKPlacemark`](../mkplacemark.md) object.

## Parameters

- `coordinate`: The geographic coordinate to associate with the placemark.
- `postalAddress`: An object containing the address information from the Contacts framework.

## See Also

### Creating a placemark object
- [init(coordinate: CLLocationCoordinate2D)](./init%28coordinate%29.md)
  Creates and returns a placemark object using the specified coordinate.
- [init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)](./init%28coordinate,addressdictionary%29.md)
  Creates and returns a placemark object using the specified coordinate and Address Book dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:postaladdress:))*