# HKPHQ9Assessment

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
class HKPHQ9Assessment
```

```objc
@interface HKPHQ9Assessment : HKScoredAssessment
```

#### Discussion

Represents the result of a PHQ-9 assessment. Learn more about Pfizer’s PHQ-9 at https://support.apple.com/en-us/105070

## Topics

### Initializers
- [convenience init(date: Date, answers: [HKPHQ9Assessment.Answer], metadata: [String : Any]?)](./hkphq9assessment/init%28date,answers,metadata%29.md)
### Instance Properties
- [var answers: [HKPHQ9Assessment.Answer]](./hkphq9assessment/answers-4y95e.md)
- [var risk: HKPHQ9Assessment.Risk](./hkphq9assessment/risk-swift.property.md)
- [answers](./hkphq9assessment/answers-439dt.md)
### Type Methods
- [+ assessmentWithDate:answers:](./hkphq9assessment/assessmentwithdate_answers_.md)
- [+ assessmentWithDate:answers:metadata:](./hkphq9assessment/assessmentwithdate_answers_metadata_.md)

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
- [class HKGAD7Assessment](./hkgad7assessment.md)
- [class HKScoredAssessment](./hkscoredassessment.md)
- [class HKScoredAssessmentType](./hkscoredassessmenttype.md)
- [class HKStateOfMind](./hkstateofmind.md)
- [class HKStateOfMindType](./hkstateofmindtype.md)
- [class HKWheelchairUseObject](./hkwheelchairuseobject.md)
  This class acts as a wrapper for the wheelchair use enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkphq9assessment)*