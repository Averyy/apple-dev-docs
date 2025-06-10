# SRElectrocardiogramData

**Framework**: SensorKit  
**Kind**: class

A representation of the ECG data that the sensor records.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class SRElectrocardiogramData
```

## Topics

### Getting electrocardiogram details
- [var flags: SRElectrocardiogramData.Flags](srelectrocardiogramdata/flags-swift.property.md)
- [SRElectrocardiogramData.Flags](srelectrocardiogramdata/flags-swift.struct.md)
  Sensor context or events that occur during a sample ECG data reading.
- [var value: Measurement<UnitElectricPotentialDifference>](srelectrocardiogramdata/value.md)
  The electrocardiogram data in microvolts.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

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
- [var data: [SRElectrocardiogramData]](srelectrocardiogramsample/data.md)
  The data that the sensor records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramdata)*