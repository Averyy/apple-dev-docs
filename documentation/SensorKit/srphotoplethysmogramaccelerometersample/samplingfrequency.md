# samplingFrequency

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The frequency of the accelerometer data recording in hertz.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var samplingFrequency: Measurement<UnitFrequency> { get }
```

```objc
@property (nonatomic, strong, readonly) NSMeasurement<NSUnitFrequency *> * samplingFrequency;
```

## See Also

### Accessing accelerometer data
- [var nanosecondsSinceStart: Int64](./nanosecondssincestart.md)
  The time in nanoseconds since the start of the accelerometer data recording.
- [var x: Measurement<UnitAcceleration>](./x.md)
  The x-axis acceleration in G’s (gravitational force).
- [var y: Measurement<UnitAcceleration>](./y.md)
  The y-axis acceleration in G’s (gravitational force).
- [var z: Measurement<UnitAcceleration>](./z.md)
  The z-axis acceleration in G’s (gravitational force).


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srphotoplethysmogramaccelerometersample/samplingfrequency)*