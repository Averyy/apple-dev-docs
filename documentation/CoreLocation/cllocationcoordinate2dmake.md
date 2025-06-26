# CLLocationCoordinate2DMake(_:_:)

**Framework**: Core Location  
**Kind**: func

Formats a latitude and longitude value into a coordinate data structure format.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CLLocationCoordinate2DMake(_ latitude: CLLocationDegrees, _ longitude: CLLocationDegrees) -> CLLocationCoordinate2D
```

#### Return Value

A coordinate structure encompassing the latitude and longitude values.

## Parameters

- `latitude`: The latitude for the new coordinate.
- `longitude`: The longitude for the new coordinate.

## See Also

- [init()](cllocationcoordinate2d/init.md)
  Creates a location coordinate object.
- [init(latitude: CLLocationDegrees, longitude: CLLocationDegrees)](cllocationcoordinate2d/init(latitude:longitude:).md)
  Creates a location coordination object with the specified latitude and longitude values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/cllocationcoordinate2dmake(_:_:))*