# departureStationLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The station from which the train departs.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@NSCopying
var departureStationLocation: CLPlacemark { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) CLPlacemark * departureStationLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly) CLPlacemark * departureStationLocation;
```

## See Also

### Getting the Train Trip Information
- [var provider: String?](./provider.md)
  The name for the train company.
- [var trainName: String?](./trainname.md)
  The name of the train.
- [var trainNumber: String?](./trainnumber.md)
  The unique identifier for the train.
- [var tripDuration: INDateComponentsRange](./tripduration.md)
  The date and time range for the departure and arrival of the train.
- [var departurePlatform: String?](./departureplatform.md)
  The platform from which the train departs.
- [var arrivalStationLocation: CLPlacemark](./arrivalstationlocation.md)
  The station at which the train arrives.
- [var arrivalPlatform: String?](./arrivalplatform.md)
  The platform at which the train arrives.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/intraintrip/departurestationlocation)*