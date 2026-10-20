# rssi

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The received signal strength of the beacon, measured in decibels.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- macOS 10.15+

## Declaration

```swift
var rssi: Int { get }
```

```objc
@property (nonatomic, readonly) NSInteger rssi;
```

#### Discussion

This value is the average signal strength of the samples received since Core Location last reported the range of the beacon to your app.

Use this value for calibrating beacon transmission power.

## See Also

### Determining the distance to the beacon
- [var proximity: CLProximity](./proximity.md)
  The relative distance to the beacon.
- [enum CLProximity](../clproximity.md)
  Constants that reflect the relative distance to a beacon.
- [var accuracy: CLLocationAccuracy](./accuracy.md)
  The accuracy of the proximity value, measured in meters from the beacon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clbeacon/rssi)*