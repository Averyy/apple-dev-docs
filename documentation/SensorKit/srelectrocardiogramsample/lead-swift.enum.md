# SRElectrocardiogramSample.Lead

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

The location of the lead that a person uses to record the ECG data.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum Lead
```

```c
enum SRElectrocardiogramLead : NSInteger;
```

## Topics

### Locations
- [SRElectrocardiogramSample.Lead.leftArmMinusRightArm](./lead-swift.enum/leftarmminusrightarm.md)
  The lead that records the sample is on the right arm.
- [SRElectrocardiogramSample.Lead.rightArmMinusLeftArm](./lead-swift.enum/rightarmminusleftarm.md)
  The lead that records the sample is on the left arm.
### Initializers
- [init?(rawValue: Int)](./lead-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Accessing ECG data
- [var date: Date](./date.md)
  The start date of the ECG sensor data recording, not the start of the session.
- [var frequency: Measurement<UnitFrequency>](./frequency.md)
  The frequency in hertz that the ECG sensor records the data.
- [var lead: SRElectrocardiogramSample.Lead](./lead-swift.property.md)
  The lead used to record the ECG data.
- [var session: SRElectrocardiogramSession](./session.md)
  The session where this sample occurs.
- [class SRElectrocardiogramSession](../srelectrocardiogramsession.md)
  An object that represents ECG data that a device records during a period of time.
- [var data: [SRElectrocardiogramData]](./data.md)
  The data that the sensor records.
- [class SRElectrocardiogramData](../srelectrocardiogramdata.md)
  A representation of the ECG data that the sensor records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsample/lead-swift.enum)*