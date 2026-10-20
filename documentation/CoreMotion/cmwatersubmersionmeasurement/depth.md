# depth

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The depth under water.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var depth: Measurement<UnitLength>? { get }
```

```objc
@property (nonatomic, readonly, nullable) NSMeasurement<NSUnitLength *> * depth;
```

## See Also

### Accessing the data
- [var date: Date](./date.md)
  The time and date when the system recorded the measurements.
- [var pressure: Measurement<UnitPressure>?](./pressure.md)
  The water pressure.
- [var surfacePressure: Measurement<UnitPressure>](./surfacepressure.md)
  The surface air pressure.
- [var submersionState: CMWaterSubmersionMeasurement.DepthState](./submersionstate.md)
  The depth state.
- [CMWaterSubmersionMeasurement.DepthState](./depthstate.md)
  A state based on the device’s depth under water.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/depth)*