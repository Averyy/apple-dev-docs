# init(MKCoordinateSpan:)

**Framework**: Foundation  
**Kind**: init

Creates a new value object containing the specified MapKit coordinate span structure.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
init(mkCoordinateSpan span: MKCoordinateSpan)
```

#### Return Value

A new value object that contains the coordinate span information.

## Parameters

- `span`: The value for the new object.

## See Also

- [struct MKCoordinateSpan](../MapKit/MKCoordinateSpan.md)
  The width and height of a map region.
- [init(MKCoordinate: CLLocationCoordinate2D)](nsvalue/init(mkcoordinate:).md)
  Creates a new value object containing the specified CoreLocation geographic coordinate structure.
- [var mkCoordinateValue: CLLocationCoordinate2D](nsvalue/mkcoordinatevalue.md)
  The CoreLocation geographic coordinate structure representation of the value.
- [var mkCoordinateSpanValue: MKCoordinateSpan](nsvalue/mkcoordinatespanvalue.md)
  The MapKit coordinate span structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(mkcoordinatespan:))*