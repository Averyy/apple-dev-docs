# CMWaterSubmersionMeasurement.DepthState

**Framework**: Core Motion  
**Kind**: enum

A state based on the device’s depth under water.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum DepthState
```

## Topics

### Depth states
- [CMWaterSubmersionMeasurement.DepthState.notSubmerged](cmwatersubmersionmeasurement/depthstate/notsubmerged.md)
  The device is not submerged in water.
- [CMWaterSubmersionMeasurement.DepthState.submergedShallow](cmwatersubmersionmeasurement/depthstate/submergedshallow.md)
  The device is submerged, but less than 1 meter under water.
- [CMWaterSubmersionMeasurement.DepthState.submergedDeep](cmwatersubmersionmeasurement/depthstate/submergeddeep.md)
  The device is submerged at least 1 meter under water.
- [CMWaterSubmersionMeasurement.DepthState.approachingMaxDepth](cmwatersubmersionmeasurement/depthstate/approachingmaxdepth.md)
  The device is approaching the maximum safe diving depth.
- [CMWaterSubmersionMeasurement.DepthState.pastMaxDepth](cmwatersubmersionmeasurement/depthstate/pastmaxdepth.md)
  The device has exceeded the maximum safe diving depth.
- [CMWaterSubmersionMeasurement.DepthState.sensorDepthError](cmwatersubmersionmeasurement/depthstate/sensordeptherror.md)
  An error with the depth sensor occurred.
- [CMWaterSubmersionMeasurement.DepthState.unknown](cmwatersubmersionmeasurement/depthstate/unknown.md)
  The device’s depth state is unknown.
### Initializers
- [init?(rawValue: Int)](cmwatersubmersionmeasurement/depthstate/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var date: Date](cmwatersubmersionmeasurement/date.md)
  The time and date when the system recorded the measurements.
- [var depth: Measurement<UnitLength>?](cmwatersubmersionmeasurement/depth.md)
  The depth under water.
- [var pressure: Measurement<UnitPressure>?](cmwatersubmersionmeasurement/pressure.md)
  The water pressure.
- [var surfacePressure: Measurement<UnitPressure>](cmwatersubmersionmeasurement/surfacepressure.md)
  The surface air pressure.
- [var submersionState: CMWaterSubmersionMeasurement.DepthState](cmwatersubmersionmeasurement/submersionstate.md)
  The depth state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depthstate)*