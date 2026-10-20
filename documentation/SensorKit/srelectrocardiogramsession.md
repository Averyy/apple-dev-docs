# SRElectrocardiogramSession

**Framework**: SensorKit  
**Kind**: class  
**Role**: Class

An object that represents ECG data that a device records during a period of time.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
class SRElectrocardiogramSession
```

```objc
@interface SRElectrocardiogramSession : NSObject
```

## Topics

### Getting session information
- [var identifier: String](./srelectrocardiogramsession/identifier.md)
  A unique identifier for the ECG session.
- [var sessionGuidance: SRElectrocardiogramSession.SessionGuidance](./srelectrocardiogramsession/sessionguidance-swift.property.md)
  The type of session used to record the sample.
- [SRElectrocardiogramSession.SessionGuidance](./srelectrocardiogramsession/sessionguidance-swift.enum.md)
  The type of session guidance used to record a ECG sample.
- [var state: SRElectrocardiogramSession.State](./srelectrocardiogramsession/state-swift.property.md)
  The state of the session used to record the sample.
- [SRElectrocardiogramSession.State](./srelectrocardiogramsession/state-swift.enum.md)
  The state of a session used to record a ECG sample.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Accessing ECG data
- [var date: Date](./srelectrocardiogramsample/date.md)
  The start date of the ECG sensor data recording, not the start of the session.
- [var frequency: Measurement<UnitFrequency>](./srelectrocardiogramsample/frequency.md)
  The frequency in hertz that the ECG sensor records the data.
- [var lead: SRElectrocardiogramSample.Lead](./srelectrocardiogramsample/lead-swift.property.md)
  The lead used to record the ECG data.
- [SRElectrocardiogramSample.Lead](./srelectrocardiogramsample/lead-swift.enum.md)
  The location of the lead that a person uses to record the ECG data.
- [var session: SRElectrocardiogramSession](./srelectrocardiogramsample/session.md)
  The session where this sample occurs.
- [var data: [SRElectrocardiogramData]](./srelectrocardiogramsample/data.md)
  The data that the sensor records.
- [class SRElectrocardiogramData](./srelectrocardiogramdata.md)
  A representation of the ECG data that the sensor records.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession)*