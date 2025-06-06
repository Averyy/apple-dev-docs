# SRElectrocardiogramSample.Lead

**Framework**: SensorKit  
**Kind**: enum

The location of the lead that a person uses to record the ECG data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum Lead
```

## Topics

### Locations
- [SRElectrocardiogramSample.Lead.leftArmMinusRightArm](srelectrocardiogramsample/lead-swift.enum/leftarmminusrightarm.md)
  The lead that records the sample is on the right arm.
- [SRElectrocardiogramSample.Lead.rightArmMinusLeftArm](srelectrocardiogramsample/lead-swift.enum/rightarmminusleftarm.md)
  The lead that records the sample is on the left arm.
### Initializers
- [init?(rawValue: Int)](srelectrocardiogramsample/lead-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var date: Date](srelectrocardiogramsample/date.md)
  The start date of the ECG sensor data recording, not the start of the session.
- [var frequency: Measurement<UnitFrequency>](srelectrocardiogramsample/frequency.md)
  The frequency in hertz that the ECG sensor records the data.
- [var lead: SRElectrocardiogramSample.Lead](srelectrocardiogramsample/lead-swift.property.md)
  The lead used to record the ECG data.
- [var session: SRElectrocardiogramSession](srelectrocardiogramsample/session.md)
  The session where this sample occurs.
- [class SRElectrocardiogramSession](srelectrocardiogramsession.md)
  An object that represents ECG data that a device records during a period of time.
- [var data: [SRElectrocardiogramData]](srelectrocardiogramsample/data.md)
  The data that the sensor records.
- [class SRElectrocardiogramData](srelectrocardiogramdata.md)
  A representation of the ECG data that the sensor records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/lead-swift.enum)*