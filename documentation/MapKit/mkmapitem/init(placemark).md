# init(placemark:)

**Framework**: MapKit  
**Kind**: init  
**Role**: Initializer

Creates and returns a map item object using the specified placemark object.

**Availability**:
- iOS 6.0+ - Deprecated in 26.0
- iPadOS 6.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.9+ - Deprecated in 26.0
- tvOS 9.2+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use init(location:address:)

## Declaration

```swift
init(placemark: MKPlacemark)
```

```objc
- (instancetype) initWithPlacemark:(MKPlacemark *) placemark;
```

## Return Value

An initialized map item object.

## Discussion

Use this method to create a map item for an existing placemark. Don’t use it to create a map item representing the user’s location. To do that, use the [`forCurrentLocation()`](./forcurrentlocation%28%29.md) method instead.

## Parameters

- `placemark`: The placemark object corresponding to the desired map location. This parameter can’t be `nil`.

## See Also

### Creating map items
- [class func forCurrentLocation() -> MKMapItem](./forcurrentlocation%28%29.md)
  Creates and returns a singleton map item object representing the user’s location.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapitem/init(placemark:))*