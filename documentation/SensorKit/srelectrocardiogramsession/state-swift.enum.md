# SRElectrocardiogramSession.State

**Framework**: SensorKit  
**Kind**: enum  
**Role**: Enumeration

The state of a session used to record a ECG sample.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum State
```

```c
enum SRElectrocardiogramSessionState : NSInteger;
```

## Topics

### States
- [SRElectrocardiogramSession.State.begin](./state-swift.enum/begin.md)
  The session begins.
- [SRElectrocardiogramSession.State.active](./state-swift.enum/active.md)
  The session is ongoing.
- [SRElectrocardiogramSession.State.end](./state-swift.enum/end.md)
  The session ends.
### Initializers
- [init?(rawValue: Int)](./state-swift.enum/init%28rawvalue%29.md)

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
- [SRElectrocardiogramSession.SessionGuidance](./sessionguidance-swift.enum.md)
  The type of session guidance used to record a ECG sample.
- [var state: SRElectrocardiogramSession.State](./state-swift.property.md)
  The state of the session used to record the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession/state-swift.enum)*