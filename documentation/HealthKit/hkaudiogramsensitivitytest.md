# HKAudiogramSensitivityTest

**Framework**: HealthKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface HKAudiogramSensitivityTest : NSObject
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./hkaudiogramsensitivitytest/init%28coder%29.md)
- [init(sensitivity: HKQuantity, type: HKAudiogramConductionType, masked: Bool, side: HKAudiogramSensitivityTestSide, clampingRange: HKAudiogramSensitivityPointClampingRange?) throws](./hkaudiogramsensitivitytest/init%28sensitivity,type,masked,side,clampingrange%29.md)
### Instance Properties
- [var clampingRange: HKAudiogramSensitivityPointClampingRange?](./hkaudiogramsensitivitytest/clampingrange.md)
- [var masked: Bool](./hkaudiogramsensitivitytest/masked.md)
- [var sensitivity: HKQuantity](./hkaudiogramsensitivitytest/sensitivity.md)
- [var side: HKAudiogramSensitivityTestSide](./hkaudiogramsensitivitytest/side.md)
- [var type: HKAudiogramConductionType](./hkaudiogramsensitivitytest/type.md)

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
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Classes
- [class HKAudiogramSensitivityPointClampingRange](./hkaudiogramsensitivitypointclampingrange.md)
  Defines the range within which an ear’s sensitivity point may have been clamped, if any.
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
- [class HKStateOfMind](./hkstateofmind.md)
- [class HKStateOfMindType](./hkstateofmindtype.md)
- [class HKWheelchairUseObject](./hkwheelchairuseobject.md)
  This class acts as a wrapper for the wheelchair use enumeration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkaudiogramsensitivitytest)*