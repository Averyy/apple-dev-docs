# recordTypes

**Framework**: HealthKit  
**Kind**: property

The types of records returned by this query.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
var recordTypes: [HKVerifiableClinicalRecordCredentialType]
```

#### Discussion

For a list of valid record types, see [`HKVerifiableClinicalRecordCredentialType`](hkverifiableclinicalrecordcredentialtype.md).

## See Also

- [var sourceTypes: [HKVerifiableClinicalRecordSourceType]](hkverifiableclinicalrecordquerydescriptor/sourcetypes.md)
  The source for the verifiable clinical records, for example from a SMART Health Card or an EU Digital COVID Certificate.
- [var predicate: NSPredicate?](hkverifiableclinicalrecordquerydescriptor/predicate.md)
  A predicate that limits the results returned by the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquerydescriptor/recordtypes)*