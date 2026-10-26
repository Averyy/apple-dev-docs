# responderClockFrequencyOffset

**Framework**: Nearby Interaction  
**Kind**: property  
**Role**: Instance Property

Indicates the clock frequency offset (CFO) fraction of the responder anchor relative to the initiator anchor (dimensionless). For example, a positive value means for every 1 clock cycle, the responder runs fewer cycles than initiator. Returns nil when measurementType is not NIDLTDOAMeasurementTypeResponse, or when the value is not available.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+

## Declaration

```objc
@property (nonatomic, strong, readonly, nullable) NSNumber * responderClockFrequencyOffset;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/nearbyinteraction/nidltdoameasurement/responderclockfrequencyoffset-899dj)*