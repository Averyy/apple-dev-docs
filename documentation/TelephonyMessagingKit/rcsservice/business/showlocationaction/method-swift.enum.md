# RCSService.Business.ShowLocationAction.Method

**Framework**: TelephonyMessagingKit  
**Kind**: enum  
**Role**: Enumeration

Enumeration indicating method to use when searching for location.

**Availability**:
- iOS 26.0+

## Declaration

```swift
enum Method
```

## Topics

### Determining location method
- [RCSService.Business.ShowLocationAction.Method.coordinates(_:)](./method-swift.enum/coordinates%28_%29.md)
  Search for location using coordinates.
- [struct CLLocationCoordinate2D](../../../../CoreLocation/cllocationcoordinate2d.md)
  The latitude and longitude associated with a location, specified using the WGS 84 reference frame.
- [RCSService.Business.ShowLocationAction.Method.query(_:)](./method-swift.enum/query%28_%29.md)
  Search for location(s) by query.

## Relationships

### Conforms To
- [Copyable](../../../../Swift/copyable.md)
- [Decodable](../../../../Swift/decodable.md)
- [Encodable](../../../../Swift/encodable.md)
- [Equatable](../../../../Swift/equatable.md)
- [Escapable](../../../../Swift/escapable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Accessing action properties
- [let method: RCSService.Business.ShowLocationAction.Method](./method-swift.property.md)
  The method to use.
- [let label: String?](./label.md)
  Label to use for location.
- [let fallbackURL: URL?](./fallbackurl.md)
  Fallback URL to use when unable to perform operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/telephonymessagingkit/rcsservice/business/showlocationaction/method-swift.enum)*