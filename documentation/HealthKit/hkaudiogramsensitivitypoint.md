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
- [init?(coder: NSCoder)](hkaudiogramsensitivitypoint/init(coder:).md)
- [convenience init(frequency: HKQuantity, tests: [HKAudiogramSensitivityTest]) throws](hkaudiogramsensitivitypoint/init(frequency:tests:).md)
### Instance Properties
- [var tests: [HKAudiogramSensitivityTest]](hkaudiogramsensitivitypoint/tests.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class HKAudiogramSample](hkaudiogramsample.md)
  A sample that stores an audiogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint)*