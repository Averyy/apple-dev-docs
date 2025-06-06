# predicate

**Framework**: HealthKit  
**Kind**: property

A predicate that limits the results returned by the query.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
var predicate: NSPredicate?
```

#### Discussion

If this property is `nil`, the query returns all records of the specified type.

## See Also

- [var recordTypes: [HKVerifiableClinicalRecordCredentialType]](hkverifiableclinicalrecordquerydescriptor/recordtypes.md)
  The types of records returned by this query.
- [var sourceTypes: [HKVerifiableClinicalRecordSourceType]](hkverifiableclinicalrecordquerydescriptor/sourcetypes.md)
  The source for the verifiable clinical records, for example from a SMART Health Card or an EU Digital COVID Certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquerydescriptor/predicate)*