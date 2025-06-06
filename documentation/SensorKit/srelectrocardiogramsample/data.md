# data

**Framework**: SensorKit  
**Kind**: property

The data that the sensor records.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var data: [SRElectrocardiogramData] { get }
```

## See Also

- [var date: Date](srelectrocardiogramsample/date.md)
  The start date of the ECG sensor data recording, not the start of the session.
- [var frequency: Measurement<UnitFrequency>](srelectrocardiogramsample/frequency.md)
  The frequency in hertz that the ECG sensor records the data.
- [var lead: SRElectrocardiogramSample.Lead](srelectrocardiogramsample/lead-swift.property.md)
  The lead used to record the ECG data.
- [SRElectrocardiogramSample.Lead](srelectrocardiogramsample/lead-swift.enum.md)
  The location of the lead that a person uses to record the ECG data.
- [var session: SRElectrocardiogramSession](srelectrocardiogramsample/session.md)
  The session where this sample occurs.
- [class SRElectrocardiogramSession](srelectrocardiogramsession.md)
  An object that represents ECG data that a device records during a period of time.
- [class SRElectrocardiogramData](srelectrocardiogramdata.md)
  A representation of the ECG data that the sensor records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/data)*