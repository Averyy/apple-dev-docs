# getCoordinates(_:range:)

**Framework**: MapKit  
**Kind**: method

Retrieves one or more points associated with the shape and converts them to coordinate values.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func getCoordinates(_ coords: UnsafeMutablePointer<CLLocationCoordinate2D>, range: NSRange)
```

#### Discussion

This method converts the map points into coordinates before returning them to you. If you want to specify the value of each point as a map point, you can access the values directly using the [`points()`](mkmultipoint/points().md) method.

## Parameters

- `coords`: On input, provide a C array of structures large enough to hold the desired number of coordinates. On output, this structure contains the requested coordinate data.
- `range`: The range of points you want. The   field indicates the first point you’re requesting, with   being the first point,   being the second point, and so on. The   field indicates the number of points you want. The array in   needs to be large enough to accommodate the number of requested coordinates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmultipoint/getcoordinates(_:range:))*