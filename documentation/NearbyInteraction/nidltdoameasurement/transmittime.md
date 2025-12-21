# transmitTime

**Framework**: Nearby Interaction  
**Kind**: property

A timestamp, in seconds, for the elapsed message transmission time.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+

## Declaration

```swift
var transmitTime: Double { get }
```

#### Discussion

The elapsed transmission time correponds to the time it takes for the message that contains the measurement to leave the anchor and arrive at the receiver.

## See Also

- [var receiveTime: Double](nidltdoameasurement/receivetime.md)
  A timestamp, in seconds, for the time that the device receives the measurement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/transmittime)*