# init(placemark:)

**Framework**: MapKit  
**Kind**: init

Creates and returns a map item object using the specified placemark object.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(placemark: MKPlacemark)
```

#### Return Value

An initialized map item object.

#### Discussion

Use this method to create a map item for an existing placemark. Don’t use it to create a map item representing the user’s location. To do that, use the [`forCurrentLocation()`](mkmapitem/forcurrentlocation().md) method instead.

## Parameters

- `placemark`: The placemark object corresponding to the desired map location. This parameter can’t be  .

## See Also

- [class func forCurrentLocation() -> MKMapItem](mkmapitem/forcurrentlocation.md)
  Creates and returns a singleton map item object representing the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/init(placemark:))*