# CMWaterSubmersionMeasurement.DepthState

**Framework**: Core Motion  
**Kind**: enum  
**Role**: Enumeration

A state based on the device’s depth under water.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
enum DepthState
```

```c
enum CMWaterSubmersionDepthState : NSInteger;
```

## Topics

### Depth states
- [CMWaterSubmersionMeasurement.DepthState.notSubmerged](./depthstate/notsubmerged.md)
  The device is not submerged in water.
- [CMWaterSubmersionMeasurement.DepthState.submergedShallow](./depthstate/submergedshallow.md)
  The device is submerged, but less than 1 meter under water.
- [CMWaterSubmersionMeasurement.DepthState.submergedDeep](./depthstate/submergeddeep.md)
  The device is submerged at least 1 meter under water.
- [CMWaterSubmersionMeasurement.DepthState.approachingMaxDepth](./depthstate/approachingmaxdepth.md)
  The device is approaching the maximum safe diving depth.
- [CMWaterSubmersionMeasurement.DepthState.pastMaxDepth](./depthstate/pastmaxdepth.md)
  The device has exceeded the maximum safe diving depth.
- [CMWaterSubmersionMeasurement.DepthState.sensorDepthError](./depthstate/sensordeptherror.md)
  An error with the depth sensor occurred.
- [CMWaterSubmersionMeasurement.DepthState.unknown](./depthstate/unknown.md)
  The device’s depth state is unknown.
### Initializers
- [init?(rawValue: Int)](./depthstate/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing the data
- [var date: Date](./date.md)
  The time and date when the system recorded the measurements.
- [var depth: Measurement<UnitLength>?](./depth.md)
  The depth under water.
- [var pressure: Measurement<UnitPressure>?](./pressure.md)
  The water pressure.
- [var surfacePressure: Measurement<UnitPressure>](./surfacepressure.md)
  The surface air pressure.
- [var submersionState: CMWaterSubmersionMeasurement.DepthState](./submersionstate.md)
  The depth state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depthstate)*