# responderClockFrequencyOffset

**Framework**: Nearby Interaction  
**Kind**: property

The clock frequency offset of the responder anchor relative to the initiator anchor.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)

## Declaration

```swift
var responderClockFrequencyOffset: Double? { get }
```

#### Discussion

This property represents relative clock frequency information between the responder anchor and initiator anchor. The relative difference is a key part of calculating precise distances. Drift between the clocks of anchors represents a persistent issue in DL-TDOA deployments that the responder clock frequency offset helps mitigate.

The value is dimensionless because it expresses a ratio rather than an absolute frequency. The ratio compares the responder’s clock frequency to the initiator’s clock frequency as a fractional difference. You can use the difference as necessary while implementing your DL-TDOA positioning engine.

## See Also

- [var measurementType: NIDLTDOAMeasurementType](nidltdoameasurement/measurementtype.md)
  The type of anchor message that the measurement derives from.
- [var carrierFrequencyOffset: Double](nidltdoameasurement/carrierfrequencyoffset.md)
  The drift, as a ratio, across the frequencies of the receiver and the anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/responderclockfrequencyoffset-8wu5r)*