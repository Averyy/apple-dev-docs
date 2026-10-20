# transmitTime

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

A transmission timestamp, in seconds, for the received message.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var transmitTime: Double { get }
```

```objc
@property (nonatomic, assign, readonly) double transmitTime;
```

#### Discussion

The elapsed transmission time correponds to the time it takes for the message that contains the measurement to leave the anchor and arrive at the receiver.

## See Also

### Assessing time difference
- [var receiveTime: Double](./receivetime.md)
  A timestamp, in seconds, for the time that the device receives the measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/transmittime)*