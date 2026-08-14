# HKAudiogramSample

**Framework**: HealthKit  
**Kind**: class

A sample that stores an audiogram.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
class HKAudiogramSample
```

#### Overview

This sample stores the results from a hearing test. The sample stores the audiogram data as an array of sensitivity points.

## Topics

### Creating Audiogram Samples
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], start: Date, end: Date, metadata: [String : Any]?)](hkaudiogramsample/init(sensitivitypoints:start:end:metadata:).md)
  Creates a new audiogram sample.
### Accessing Sensitivity Point Data
- [var sensitivityPoints: [HKAudiogramSensitivityPoint]](hkaudiogramsample/sensitivitypoints.md)
  An array of sensitivity point objects.
### Initializers
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], start: Date, end: Date, device: HKDevice?, metadata: [String : Any]?)](hkaudiogramsample/init(sensitivitypoints:start:end:device:metadata:).md)
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], startDate: Date, endDate: Date, device: HKDevice?, metadata: [String : Any]?)](hkaudiogramsample/init(sensitivitypoints:startdate:enddate:device:metadata:).md)
- [convenience init(sensitivityPoints: [HKAudiogramSensitivityPoint], startDate: Date, endDate: Date, metadata: [String : Any]?)](hkaudiogramsample/init(sensitivitypoints:startdate:enddate:metadata:).md)

## Relationships

### Inherits From
- [HKSample](hksample.md)
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

- [class HKAudiogramSensitivityPoint](hkaudiogramsensitivitypoint.md)
  A hearing sensitivity reading associated with a hearing test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsample)*