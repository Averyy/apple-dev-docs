# date

**Framework**: Core Motion  
**Kind**: property  
**Role**: Instance Property

The time and date when the system recorded the measurements.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
var date: Date { get }
```

```objc
@property (nonatomic, readonly) NSDate * date;
```

## See Also

### Accessing the data
- [var depth: Measurement<UnitLength>?](./depth.md)
  The depth under water.
- [var pressure: Measurement<UnitPressure>?](./pressure.md)
  The water pressure.
- [var surfacePressure: Measurement<UnitPressure>](./surfacepressure.md)
  The surface air pressure.
- [var submersionState: CMWaterSubmersionMeasurement.DepthState](./submersionstate.md)
  The depth state.
- [CMWaterSubmersionMeasurement.DepthState](./depthstate.md)
  A state based on the device’s depth under water.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmwatersubmersionmeasurement/date)*