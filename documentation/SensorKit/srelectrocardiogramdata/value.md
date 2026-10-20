# value

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The electrocardiogram data in microvolts.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var value: Measurement<UnitElectricPotentialDifference> { get }
```

```objc
@property (nonatomic, strong, readonly) NSMeasurement<NSUnitElectricPotentialDifference *> * value;
```

## See Also

### Getting electrocardiogram details
- [var flags: SRElectrocardiogramData.Flags](./flags-swift.property.md)
- [SRElectrocardiogramData.Flags](./flags-swift.struct.md)
  Sensor context or events that occur during a sample ECG data reading.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata/value)*