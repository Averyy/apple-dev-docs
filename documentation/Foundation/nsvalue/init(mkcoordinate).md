# init(MKCoordinate:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a new value object containing the specified CoreLocation geographic coordinate structure.

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
init(MKCoordinate coordinate: CLLocationCoordinate2D)
```

```swift
init(mkCoordinate coordinate: CLLocationCoordinate2D)
```

```objc
+ (NSValue *) valueWithMKCoordinate:(CLLocationCoordinate2D) coordinate;
```

#### Return Value

A new value object that contains the geographic coordinate information.

## Parameters

- `coordinate`: The value for the new object.

## See Also

### Related Documentation
- [struct CLLocationCoordinate2D](../../CoreLocation/cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
### Working with Geographic Coordinate Values
- [init(MKCoordinateSpan: MKCoordinateSpan)](./init%28mkcoordinatespan%29.md)
  Creates a new value object containing the specified MapKit coordinate span structure.
- [var mkCoordinateValue: CLLocationCoordinate2D](./mkcoordinatevalue.md)
  The CoreLocation geographic coordinate structure representation of the value.
- [var mkCoordinateSpanValue: MKCoordinateSpan](./mkcoordinatespanvalue.md)
  The MapKit coordinate span structure representation of the value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsvalue/init(mkcoordinate:))*