# predicateForElectrocardiograms(symptomsStatus:)

**Framework**: HealthKit  
**Kind**: method

Returns a predicate that matches electrocardiogram samples with the specified symptom status.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
class func predicateForElectrocardiograms(symptomsStatus: HKElectrocardiogram.SymptomsStatus) -> NSPredicate
```

#### Return Value

A predicate that matches electrocardiogram samples with the specified symptom status.

#### Discussion

Use this convenience method to create a predicate that matches electrocardiogram samples with the specified symptom status. The following sample uses both the convenience method and a predicate format string to create equivalent predicates.

```swift
let forSymptomStatus = HKQuery.predicateForElectrocardiograms(symptomsStatus: .present)

let status = HKElectrocardiogram.SymptomsStatus.present.rawValue


let explicitForSymptomStatus = NSPredicate(format: "%K == %d", HKPredicateKeyPathECGSymptomsStatus, status)
```

## Parameters

- `symptomsStatus`: The target symptom status.

## See Also

- [let HKPredicateKeyPathECGSymptomsStatus: String](hkpredicatekeypathecgsymptomsstatus.md)
  The key path for the sample’s symptom status.
- [class func predicateForElectrocardiograms(classification: HKElectrocardiogram.Classification) -> NSPredicate](hkquery/predicateforelectrocardiograms(classification:).md)
  Returns a predicate that matches electrocardiogram samples with the specified classification.
- [class func predicateForObjectsAssociated(electrocardiogram: HKElectrocardiogram) -> NSPredicate](hkquery/predicateforobjectsassociated(electrocardiogram:).md)
  Returns a predicate that matches symptom samples associated with the specified electrocardiogram.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkquery/predicateforelectrocardiograms(symptomsstatus:))*