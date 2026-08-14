# HKAudiogramSensitivityTest

**Framework**: HealthKit  
**Kind**: class

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+
- macOS 15.1+
- visionOS 2.1+
- watchOS 11.1+

## Declaration

```swift
class HKAudiogramSensitivityTest
```

## Topics

### Initializers
- [init?(coder: NSCoder)](hkaudiogramsensitivitytest/init(coder:).md)
- [init(sensitivity: HKQuantity, type: HKAudiogramConductionType, masked: Bool, side: HKAudiogramSensitivityTestSide, clampingRange: HKAudiogramSensitivityPointClampingRange?) throws](hkaudiogramsensitivitytest/init(sensitivity:type:masked:side:clampingrange:).md)
### Instance Properties
- [var clampingRange: HKAudiogramSensitivityPointClampingRange?](hkaudiogramsensitivitytest/clampingrange.md)
- [var masked: Bool](hkaudiogramsensitivitytest/masked.md)
- [var sensitivity: HKQuantity](hkaudiogramsensitivitytest/sensitivity.md)
- [var side: HKAudiogramSensitivityTestSide](hkaudiogramsensitivitytest/side.md)
- [var type: HKAudiogramConductionType](hkaudiogramsensitivitytest/type.md)

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
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [class HKAudiogramSensitivityPointClampingRange](hkaudiogramsensitivitypointclampingrange.md)
  Defines the range within which an ear’s sensitivity point may have been clamped, if any.
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

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitytest)*