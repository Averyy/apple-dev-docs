# identifier

**Framework**: SensorKit  
**Kind**: property  
**Role**: Instance Property

A unique identifier for the ECG session.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+

## Declaration

```swift
var identifier: String { get }
```

```objc
@property (nonatomic, copy, readonly) NSString * identifier;
```

## See Also

### Getting session information
- [var sessionGuidance: SRElectrocardiogramSession.SessionGuidance](./sessionguidance-swift.property.md)
  The type of session used to record the sample.
- [SRElectrocardiogramSession.SessionGuidance](./sessionguidance-swift.enum.md)
  The type of session guidance used to record a ECG sample.
- [var state: SRElectrocardiogramSession.State](./state-swift.property.md)
  The state of the session used to record the sample.
- [SRElectrocardiogramSession.State](./state-swift.enum.md)
  The state of a session used to record a ECG sample.


---

*[View on Apple Developer](https://developer.apple.com/documentation/sensorkit/srelectrocardiogramsession/identifier)*