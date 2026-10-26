# arrivalPlatform

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The platform at which the bus arrives.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var arrivalPlatform: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * arrivalPlatform;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * arrivalPlatform;
```

## See Also

### Getting the Bus Trip Information
- [var arrivalBusStopLocation: CLPlacemark](./arrivalbusstoplocation.md)
  The bus stop where the trip ends.
- [var busName: String?](./busname.md)
  The name of the bus.
- [var busNumber: String?](./busnumber.md)
  The number of the bus or route.
- [var departureBusStopLocation: CLPlacemark](./departurebusstoplocation.md)
  The bus stop where the bus trip starts.
- [var departurePlatform: String?](./departureplatform.md)
  The platform from which the bus departs.
- [var provider: String?](./provider.md)
  The business or other entity operating the bus.
- [var tripDuration: INDateComponentsRange](./tripduration.md)
  The timespan of the bus trip from departure to arrival.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inbustrip/arrivalplatform)*