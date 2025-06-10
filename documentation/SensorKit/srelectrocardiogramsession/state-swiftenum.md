# SRElectrocardiogramSession.State

**Framework**: SensorKit  
**Kind**: enum

The state of a session used to record a ECG sample.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum State
```

## Topics

### States
- [SRElectrocardiogramSession.State.begin](srelectrocardiogramsession/state-swift.enum/begin.md)
  The session begins.
- [SRElectrocardiogramSession.State.active](srelectrocardiogramsession/state-swift.enum/active.md)
  The session is ongoing.
- [SRElectrocardiogramSession.State.end](srelectrocardiogramsession/state-swift.enum/end.md)
  The session ends.
### Initializers
- [init?(rawValue: Int)](srelectrocardiogramsession/state-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [var identifier: String](srelectrocardiogramsession/identifier.md)
  A unique identifier for the ECG session.
- [var sessionGuidance: SRElectrocardiogramSession.SessionGuidance](srelectrocardiogramsession/sessionguidance-swift.property.md)
  The type of session used to record the sample.
- [SRElectrocardiogramSession.SessionGuidance](srelectrocardiogramsession/sessionguidance-swift.enum.md)
  The type of session guidance used to record a ECG sample.
- [var state: SRElectrocardiogramSession.State](srelectrocardiogramsession/state-swift.property.md)
  The state of the session used to record the sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession/state-swift.enum)*