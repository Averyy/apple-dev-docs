# arrivalBoatTerminalLocation

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The place where the boat trip ends.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
@NSCopying
var arrivalBoatTerminalLocation: CLPlacemark { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly) CLPlacemark * arrivalBoatTerminalLocation;
```

*macOS*

```objc
@property (atomic, copy, readonly) CLPlacemark * arrivalBoatTerminalLocation;
```

## See Also

### Getting the Boat Trip Information
- [var provider: String?](./provider.md)
  The operator of the boat line.
- [var boatName: String?](./boatname.md)
  The name of the boat.
- [var boatNumber: String?](./boatnumber.md)
  The number associated with the boat.
- [var tripDuration: INDateComponentsRange](./tripduration.md)
  The timespan of the boat trip from departure to arrival.
- [var departureBoatTerminalLocation: CLPlacemark](./departureboatterminallocation.md)
  The place where the boat trip starts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inboattrip/arrivalboatterminallocation)*