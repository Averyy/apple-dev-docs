# predicateForObjectsAssociated(electrocardiogram:)

**Framework**: HealthKit  
**Kind**: method  
**Role**: Type Method

Returns a predicate that matches symptom samples associated with the specified electrocardiogram.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func predicateForObjectsAssociated(electrocardiogram: HKElectrocardiogram) -> NSPredicate
```

```objc
+ (NSPredicate *) predicateForObjectsAssociatedWithElectrocardiogram:(HKElectrocardiogram *) electrocardiogram;
```

#### Return Value

A predicate that matches symptom samples associated with the specified electrocardiogram.

#### Discussion

If the [`HKElectrocardiogram`](../hkelectrocardiogram.md) sample’s [`symptomsStatus`](../hkelectrocardiogram/symptomsstatus-swift.property.md) property is [`HKElectrocardiogram.SymptomsStatus.present`](../hkelectrocardiogram/symptomsstatus-swift.enum/present.md), you can query for symptom samples associated with the electrocardiogram. See [Symptom Type Identifiers](../symptom-type-identifiers.md) for a complete list of symptom types.

## Parameters

- `electrocardiogram`: The target electrocardiogram.

## See Also

### Creating electrocardiogram predicates
- [class func predicateForElectrocardiograms(classification: HKElectrocardiogram.Classification) -> NSPredicate](./predicateforelectrocardiograms%28classification%29.md)
  Returns a predicate that matches electrocardiogram samples with the specified classification.
- [class func predicateForElectrocardiograms(symptomsStatus: HKElectrocardiogram.SymptomsStatus) -> NSPredicate](./predicateforelectrocardiograms%28symptomsstatus%29.md)
  Returns a predicate that matches electrocardiogram samples with the specified symptom status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforobjectsassociated(electrocardiogram:))*