# frequency

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The frequency in hertz that the ECG sensor records the data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var frequency: Measurement<UnitFrequency> { get }
```

```objc
@property (nonatomic, strong, readonly) NSMeasurement<NSUnitFrequency *> * frequency;
```

## See Also

### Accessing ECG data
- [var date: Date](./date.md)
  The start date of the ECG sensor data recording, not the start of the session.
- [var lead: SRElectrocardiogramSample.Lead](./lead-swift.property.md)
  The lead used to record the ECG data.
- [SRElectrocardiogramSample.Lead](./lead-swift.enum.md)
  The location of the lead that a person uses to record the ECG data.
- [var session: SRElectrocardiogramSession](./session.md)
  The session where this sample occurs.
- [class SRElectrocardiogramSession](../srelectrocardiogramsession.md)
  An object that represents ECG data that a device records during a period of time.
- [var data: [SRElectrocardiogramData]](./data.md)
  The data that the sensor records.
- [class SRElectrocardiogramData](../srelectrocardiogramdata.md)
  A representation of the ECG data that the sensor records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/frequency)*