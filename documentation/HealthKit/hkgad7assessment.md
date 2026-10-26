# HKGAD7Assessment

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
class HKGAD7Assessment
```

```objc
@interface HKGAD7Assessment : HKScoredAssessment
```

## Topics

### Initializers
- [convenience init(date: Date, answers: [HKGAD7Assessment.Answer], metadata: [String : Any]?)](./hkgad7assessment/init%28date,answers,metadata%29.md)
### Instance Properties
- [var answers: [HKGAD7Assessment.Answer]](./hkgad7assessment/answers-1zj1.md)
- [var risk: HKGAD7Assessment.Risk](./hkgad7assessment/risk-swift.property.md)
- [answers](./hkgad7assessment/answers-7k5w8.md)
### Type Methods
- [+ assessmentWithDate:answers:](./hkgad7assessment/assessmentwithdate_answers_.md)
- [+ assessmentWithDate:answers:metadata:](./hkgad7assessment/assessmentwithdate_answers_metadata_.md)

## Relationships

### Inherits From
- [HKScoredAssessment](./hkscoredassessment.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class HKAudiogramSensitivityPointClampingRange](./hkaudiogramsensitivitypointclampingrange.md)
  Defines the range within which an ear’s sensitivity point may have been clamped, if any.
- [class HKAudiogramSensitivityTest](./hkaudiogramsensitivitytest.md)
- [class HKBiologicalSexObject](./hkbiologicalsexobject.md)
  This class acts as a wrapper for the [`HKBiologicalSex`](./hkbiologicalsex.md) enumeration.
- [class HKBloodTypeObject](./hkbloodtypeobject.md)
  This class acts as a wrapper for the [`HKBloodType`](./hkbloodtype.md) enumeration.
- [class HKFitzpatrickSkinTypeObject](./hkfitzpatrickskintypeobject.md)
  This class acts as a wrapper for the [`HKFitzpatrickSkinType`](./hkfitzpatrickskintype.md) enumeration.
- [class HKPHQ9Assessment](./hkphq9assessment.md)
- [class HKScoredAssessment](./hkscoredassessment.md)
- [class HKScoredAssessmentType](./hkscoredassessmenttype.md)
- [class HKStateOfMind](./hkstateofmind.md)
- [class HKStateOfMindType](./hkstateofmindtype.md)
- [class HKWheelchairUseObject](./hkwheelchairuseobject.md)
  This class acts as a wrapper for the wheelchair use enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkgad7assessment)*