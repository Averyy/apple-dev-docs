# submersionState

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The depth state.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var submersionState: CMWaterSubmersionMeasurement.DepthState { get }
```

```objc
@property (nonatomic, readonly) CMWaterSubmersionDepthState submersionState;
```

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
- [CMWaterSubmersionMeasurement.DepthState](./depthstate.md)
  A state based on the device’s depth under water.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/submersionstate)*