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

## Relationships

### Inherits From
- [HKSample](hksample.md)
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

- [class HKAudiogramSensitivityPoint](hkaudiogramsensitivitypoint.md)
  A hearing sensitivity reading associated with a hearing test.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsample)*