# CMWaterSubmersionMeasurement.DepthState.submergedShallow

**Framework**: Core Motion  
**Kind**: case  
**Role**: Case

The device is submerged, but less than 1 meter under water.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 4.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
case submergedShallow
```

```c
CMWaterSubmersionDepthStateSubmergedShallow
```

## See Also

### Depth states
- [CMWaterSubmersionMeasurement.DepthState.notSubmerged](./notsubmerged.md)
  The device is not submerged in water.
- [CMWaterSubmersionMeasurement.DepthState.submergedDeep](./submergeddeep.md)
  The device is submerged at least 1 meter under water.
- [CMWaterSubmersionMeasurement.DepthState.approachingMaxDepth](./approachingmaxdepth.md)
  The device is approaching the maximum safe diving depth.
- [CMWaterSubmersionMeasurement.DepthState.pastMaxDepth](./pastmaxdepth.md)
  The device has exceeded the maximum safe diving depth.
- [CMWaterSubmersionMeasurement.DepthState.sensorDepthError](./sensordeptherror.md)
  An error with the depth sensor occurred.
- [CMWaterSubmersionMeasurement.DepthState.unknown](./unknown.md)
  The device’s depth state is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depthstate/submergedshallow)*