# HKAudiogramSensitivityPoint

**Framework**: HealthKit  
**Kind**: class

A hearing sensitivity reading associated with a hearing test.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HKAudiogramSensitivityPoint
```

## Topics

### Creating Sensitivity Points
- [convenience init(frequency: HKQuantity, leftEarSensitivity: HKQuantity?, rightEarSensitivity: HKQuantity?) throws](hkaudiogramsensitivitypoint/init(frequency:leftearsensitivity:rightearsensitivity:).md)
  Creates a new sensitivity point.
### Accessing Data
- [var frequency: HKQuantity](hkaudiogramsensitivitypoint/frequency.md)
  The frequency tested in the hearing test.
- [var leftEarSensitivity: HKQuantity?](hkaudiogramsensitivitypoint/leftearsensitivity.md)
  The sensitivity of the left ear.
- [var rightEarSensitivity: HKQuantity?](hkaudiogramsensitivitypoint/rightearsensitivity.md)
  The sensitivity of the right ear.
### Initializers
- [convenience init(frequency: HKQuantity, tests: [HKAudiogramSensitivityTest]) throws](hkaudiogramsensitivitypoint/init(frequency:tests:).md)
### Instance Properties
- [var tests: [HKAudiogramSensitivityTest]](hkaudiogramsensitivitypoint/tests.md)

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
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKAudiogramSample](hkaudiogramsample.md)
  A sample that stores an audiogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint)*