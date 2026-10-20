# advisoryNotices

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

An array of advisory notice strings for the route.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
var advisoryNotices: [String] { get }
```

```objc
@property (nonatomic, readonly) NSArray<NSString *> * advisoryNotices;
```

#### Discussion

This property contains an array of [`NSString`](../../Foundation/nsstring.md) objects. The framework localizes each string according to the user’s language preferences. The strings contain additional information that’s important for the user to know about the route. For example, a string might note the closing of a portion of the route during the winter or after big storms.

## See Also

### Getting additional route details
- [var name: String](./name.md)
  The assigned name for the route.
- [var hasHighways: Bool](./hashighways.md)
  A Boolean value that indicates whether the route contains highways.
- [var hasTolls: Bool](./hastolls.md)
  A Boolean value that indicates whether the route has tolls.
- [var distance: CLLocationDistance](./distance.md)
  The route distance, in meters.
- [var expectedTravelTime: TimeInterval](./expectedtraveltime.md)
  The expected travel time, in seconds.
- [var transportType: MKDirectionsTransportType](./transporttype.md)
  The overall route transport type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkroute/advisorynotices)*