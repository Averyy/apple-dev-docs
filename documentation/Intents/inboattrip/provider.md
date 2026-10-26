# provider

**Framework**: Intents  
**Kind**: property  
**Role**: Instance Property

The operator of the boat line.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var provider: String? { get }
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS, watchOS*

```objc
@property (nonatomic, copy, readonly, nullable) NSString * provider;
```

*macOS*

```objc
@property (atomic, copy, readonly, nullable) NSString * provider;
```

## See Also

### Getting the Boat Trip Information
- [var boatName: String?](./boatname.md)
  The name of the boat.
- [var boatNumber: String?](./boatnumber.md)
  The number associated with the boat.
- [var tripDuration: INDateComponentsRange](./tripduration.md)
  The timespan of the boat trip from departure to arrival.
- [var departureBoatTerminalLocation: CLPlacemark](./departureboatterminallocation.md)
  The place where the boat trip starts.
- [var arrivalBoatTerminalLocation: CLPlacemark](./arrivalboatterminallocation.md)
  The place where the boat trip ends.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intents/inboattrip/provider)*