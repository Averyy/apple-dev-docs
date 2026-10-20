# mkCoordinateValue

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

The CoreLocation geographic coordinate structure representation of the value.

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
var mkCoordinateValue: CLLocationCoordinate2D { get }
```

```objc
@property (atomic, readonly) CLLocationCoordinate2D MKCoordinateValue;
```

## See Also

### Related Documentation
- [struct CLLocationCoordinate2D](../../CoreLocation/cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
### Working with Geographic Coordinate Values
- [init(MKCoordinate: CLLocationCoordinate2D)](./init%28mkcoordinate%29.md)
  Creates a new value object containing the specified CoreLocation geographic coordinate structure.
- [init(MKCoordinateSpan: MKCoordinateSpan)](./init%28mkcoordinatespan%29.md)
  Creates a new value object containing the specified MapKit coordinate span structure.
- [var mkCoordinateSpanValue: MKCoordinateSpan](./mkcoordinatespanvalue.md)
  The MapKit coordinate span structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/mkcoordinatevalue)*