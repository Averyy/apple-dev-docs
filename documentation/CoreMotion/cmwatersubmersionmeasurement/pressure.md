# pressure

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The water pressure.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var pressure: Measurement<UnitPressure>? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSMeasurement<NSUnitPressure *> * pressure;
```

## See Also

### Accessing the data
- [var date: Date](./date.md)
  The time and date when the system recorded the measurements.
- [var depth: Measurement<UnitLength>?](./depth.md)
  The depth under water.
- [var surfacePressure: Measurement<UnitPressure>](./surfacepressure.md)
  The surface air pressure.
- [var submersionState: CMWaterSubmersionMeasurement.DepthState](./submersionstate.md)
  The depth state.
- [CMWaterSubmersionMeasurement.DepthState](./depthstate.md)
  A state based on the device’s depth under water.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/pressure)*