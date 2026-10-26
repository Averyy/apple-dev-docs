# HKStateOfMind

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
class HKStateOfMind
```

```objc
@interface HKStateOfMind : HKSample
```

## Topics

### Initializers
- [convenience init(date: Date, kind: HKStateOfMind.Kind, valence: Double, labels: [HKStateOfMind.Label], associations: [HKStateOfMind.Association], metadata: [String : Any]?)](./hkstateofmind/init%28date,kind,valence,labels,associations,metadata%29.md)
### Instance Properties
- [var associations: [HKStateOfMind.Association]](./hkstateofmind/associations-7gwps.md)
- [var kind: HKStateOfMind.Kind](./hkstateofmind/kind-swift.property.md)
- [var labels: [HKStateOfMind.Label]](./hkstateofmind/labels-994n4.md)
- [var valence: Double](./hkstateofmind/valence.md)
- [var valenceClassification: HKStateOfMind.ValenceClassification](./hkstateofmind/valenceclassification-swift.property.md)
- [associations](./hkstateofmind/associations-5vfw8.md)
- [labels](./hkstateofmind/labels-11jl3.md)
### Type Methods
- [+ stateOfMindWithDate:kind:valence:labels:associations:](./hkstateofmind/stateofmindwithdate_kind_valence_labels_associations_.md)
- [+ stateOfMindWithDate:kind:valence:labels:associations:metadata:](./hkstateofmind/stateofmindwithdate_kind_valence_labels_associations_metadata_.md)

## Relationships

### Inherits From
- [HKSample](./hksample.md)
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
- [class HKPHQ9Assessment](./hkphq9assessment.md)
- [class HKScoredAssessment](./hkscoredassessment.md)
- [class HKScoredAssessmentType](./hkscoredassessmenttype.md)
- [class HKStateOfMindType](./hkstateofmindtype.md)
- [class HKWheelchairUseObject](./hkwheelchairuseobject.md)
  This class acts as a wrapper for the wheelchair use enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkstateofmind)*