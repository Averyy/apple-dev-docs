# init(coordinate:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a placemark object using the specified coordinate.

**Availability**:
- iOS 10.0+ - Deprecated in 26.0
- iPadOS 10.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.12+ - Deprecated in 26.0
- tvOS 10.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
init(coordinate: CLLocationCoordinate2D)
```

```objc
- (instancetype) initWithCoordinate:(CLLocationCoordinate2D) coordinate;
```

## Return Value

An initialized [`MKPlacemark`](../mkplacemark.md) object.

## Discussion

This method doesn’t fill in any of the other inherited properties describing the location.

## Parameters

- `coordinate`: The geographic coordinate to associate with the placemark.

## See Also

### Creating a placemark object
- [init(coordinate: CLLocationCoordinate2D, postalAddress: CNPostalAddress)](./init%28coordinate,postaladdress%29.md)
  Creates and returns a placemark object with the specified coordinate and postal address from the user’s Contacts database.
- [init(coordinate: CLLocationCoordinate2D, addressDictionary: [String : Any]?)](./init%28coordinate,addressdictionary%29.md)
  Creates and returns a placemark object using the specified coordinate and Address Book dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkplacemark/init(coordinate:))*