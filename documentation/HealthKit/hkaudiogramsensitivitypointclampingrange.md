# HKAudiogramSensitivityPointClampingRange

**Framework**: HealthKit  
**Kind**: class

Defines the range within which an ear’s sensitivity point may have been clamped, if any.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
class HKAudiogramSensitivityPointClampingRange
```

#### Overview

At times, it may be required to indicate that a sensitivity point has been clamped to a range. These reasons include but are not limited to user safety, hardware limitations, or algorithm features.

## Topics

### Initializers
- [convenience init(lowerBound: NSNumber?, upperBound: NSNumber?) throws](hkaudiogramsensitivitypointclampingrange/init(lowerbound:upperbound:).md)
### Instance Properties
- [var lowerBound: HKQuantity?](hkaudiogramsensitivitypointclampingrange/lowerbound.md)
- [var upperBound: HKQuantity?](hkaudiogramsensitivitypointclampingrange/upperbound.md)

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
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class HKAudiogramSensitivityTest](hkaudiogramsensitivitytest.md)
- [class HKBiologicalSexObject](hkbiologicalsexobject.md)
  This class acts as a wrapper for the [`HKBiologicalSex`](hkbiologicalsex.md) enumeration.
- [class HKBloodTypeObject](hkbloodtypeobject.md)
  This class acts as a wrapper for the [`HKBloodType`](hkbloodtype.md) enumeration.
- [class HKFitzpatrickSkinTypeObject](hkfitzpatrickskintypeobject.md)
  This class acts as a wrapper for the [`HKFitzpatrickSkinType`](hkfitzpatrickskintype.md) enumeration.
- [class HKGAD7Assessment](hkgad7assessment.md)
- [class HKPHQ9Assessment](hkphq9assessment.md)
- [class HKScoredAssessment](hkscoredassessment.md)
- [class HKScoredAssessmentType](hkscoredassessmenttype.md)
- [class HKStateOfMind](hkstateofmind.md)
- [class HKStateOfMindType](hkstateofmindtype.md)
- [class HKWheelchairUseObject](hkwheelchairuseobject.md)
  This class acts as a wrapper for the wheelchair use enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitypointclampingrange)*