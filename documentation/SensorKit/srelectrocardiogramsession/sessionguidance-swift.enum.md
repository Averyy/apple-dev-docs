# SRElectrocardiogramSession.SessionGuidance

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

The type of session guidance used to record a ECG sample.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum SessionGuidance
```

```c
enum SRElectrocardiogramSessionGuidance : NSInteger;
```

## Topics

### Types
- [SRElectrocardiogramSession.SessionGuidance.guided](./sessionguidance-swift.enum/guided.md)
  The system coaches the user to guide the ECG readings.
- [SRElectrocardiogramSession.SessionGuidance.unguided](./sessionguidance-swift.enum/unguided.md)
  The system doesn’t coach the user to guide the ECG readings.
### Initializers
- [init?(rawValue: Int)](./sessionguidance-swift.enum/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting session information
- [var identifier: String](./identifier.md)
  A unique identifier for the ECG session.
- [var sessionGuidance: SRElectrocardiogramSession.SessionGuidance](./sessionguidance-swift.property.md)
  The type of session used to record the sample.
- [var state: SRElectrocardiogramSession.State](./state-swift.property.md)
  The state of the session used to record the sample.
- [SRElectrocardiogramSession.State](./state-swift.enum.md)
  The state of a session used to record a ECG sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession/sessionguidance-swift.enum)*