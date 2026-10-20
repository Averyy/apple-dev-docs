# state

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

The state of the session used to record the sample.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var state: SRElectrocardiogramSession.State { get }
```

```objc
@property (nonatomic, assign, readonly) SRElectrocardiogramSessionState state;
```

## See Also

### Getting session information
- [var identifier: String](./identifier.md)
  A unique identifier for the ECG session.
- [var sessionGuidance: SRElectrocardiogramSession.SessionGuidance](./sessionguidance-swift.property.md)
  The type of session used to record the sample.
- [SRElectrocardiogramSession.SessionGuidance](./sessionguidance-swift.enum.md)
  The type of session guidance used to record a ECG sample.
- [SRElectrocardiogramSession.State](./state-swift.enum.md)
  The state of a session used to record a ECG sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession/state-swift.property)*