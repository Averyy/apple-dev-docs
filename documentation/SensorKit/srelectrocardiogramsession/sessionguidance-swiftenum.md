# SRElectrocardiogramSession.SessionGuidance

**Framework**: SensorKit  
**Kind**: enum

The type of session guidance used to record a ECG sample.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
enum SessionGuidance
```

## Topics

### Types
- [SRElectrocardiogramSession.SessionGuidance.guided](srelectrocardiogramsession/sessionguidance-swift.enum/guided.md)
  The system coaches the user to guide the ECG readings.
- [SRElectrocardiogramSession.SessionGuidance.unguided](srelectrocardiogramsession/sessionguidance-swift.enum/unguided.md)
  The system doesn’t coach the user to guide the ECG readings.
### Initializers
- [init?(rawValue: Int)](srelectrocardiogramsession/sessionguidance-swift.enum/init(rawvalue:).md)

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
- [var state: SRElectrocardiogramSession.State](srelectrocardiogramsession/state-swift.property.md)
  The state of the session used to record the sample.
- [SRElectrocardiogramSession.State](srelectrocardiogramsession/state-swift.enum.md)
  The state of a session used to record a ECG sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession/sessionguidance-swift.enum)*