# HKAudiogramSensitivityPoint

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKAudiogramSensitivityPoint : NSObject
```

## Topics

### Creating Sensitivity Points
- [convenience init(frequency: HKQuantity, leftEarSensitivity: HKQuantity?, rightEarSensitivity: HKQuantity?) throws](./hkaudiogramsensitivitypoint/init%28frequency,leftearsensitivity,rightearsensitivity%29.md)
  Creates a new sensitivity point.
### Accessing Data
- [var frequency: HKQuantity](./hkaudiogramsensitivitypoint/frequency.md)
  The frequency tested in the hearing test.
- [var leftEarSensitivity: HKQuantity?](./hkaudiogramsensitivitypoint/leftearsensitivity.md)
  The sensitivity of the left ear.
- [var rightEarSensitivity: HKQuantity?](./hkaudiogramsensitivitypoint/rightearsensitivity.md)
  The sensitivity of the right ear.
### Initializers
- [init?(coder: NSCoder)](./hkaudiogramsensitivitypoint/init%28coder%29.md)
- [convenience init(frequency: HKQuantity, tests: [HKAudiogramSensitivityTest]) throws](./hkaudiogramsensitivitypoint/init%28frequency,tests%29.md)
### Instance Properties
- [var tests: [HKAudiogramSensitivityTest]](./hkaudiogramsensitivitypoint/tests.md)

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
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Audiograms
- [class HKAudiogramSample](./hkaudiogramsample.md)
  A sample that stores an audiogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypoint)*