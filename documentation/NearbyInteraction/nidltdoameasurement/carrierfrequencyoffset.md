# carrierFrequencyOffset

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

The drift, as a ratio, across the frequencies of the receiver and the anchor.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+

## Declaration

```swift
var carrierFrequencyOffset: Double { get }
```

```objc
@property (nonatomic, assign, readonly) double carrierFrequencyOffset;
```

## See Also

### Evaluating the message
- [var measurementType: NIDLTDOAMeasurementType](./measurementtype.md)
  The type of anchor message that the measurement derives from.
- [var responderClockFrequencyOffset: Double?](./responderclockfrequencyoffset-8wu5r.md)
  The clock frequency offset of the responder anchor relative to the initiator anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/carrierfrequencyoffset)*