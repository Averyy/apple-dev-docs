# predicateForElectrocardiograms(classification:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that matches electrocardiogram samples with the specified classification.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func predicateForElectrocardiograms(classification: HKElectrocardiogram.Classification) -> NSPredicate
```

#### Return Value

A predicate that matches electrocardiogram samples with the specified classification.

#### Discussion

Use this convenience method to create a predicate that matches electrocardiogram samples with the specified classification. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

```swift
let forClassification = HKQuery.predicateForElectrocardiograms(classification: .atrialFibrillation)

let classification = HKElectrocardiogram.Classification.atrialFibrillation.rawValue

let explicitForClassification = NSPredicate(format: "%K == %d", HKPredicateKeyPathECGClassification, classification)
```

## Parameters

- `classification`: The target classification.

## See Also

- [let HKPredicateKeyPathECGClassification: String](hkpredicatekeypathecgclassification.md)
  The key path for the sample’s classification.
- [class func predicateForElectrocardiograms(symptomsStatus: HKElectrocardiogram.SymptomsStatus) -> NSPredicate](hkquery/predicateforelectrocardiograms(symptomsstatus:).md)
  Returns a predicate that matches electrocardiogram samples with the specified symptom status.
- [class func predicateForObjectsAssociated(electrocardiogram: HKElectrocardiogram) -> NSPredicate](hkquery/predicateforobjectsassociated(electrocardiogram:).md)
  Returns a predicate that matches symptom samples associated with the specified electrocardiogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforelectrocardiograms(classification:))*