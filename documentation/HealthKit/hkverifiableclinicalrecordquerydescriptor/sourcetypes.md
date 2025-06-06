# sourceTypes

**Framework**: HealthKit  
**Kind**: property

The source for the verifiable clinical records, for example from a SMART Health Card or an EU Digital COVID Certificate.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
var sourceTypes: [HKVerifiableClinicalRecordSourceType]
```

#### Discussion

For a list of valid sources, see [`HKVerifiableClinicalRecordSourceType`](hkverifiableclinicalrecordsourcetype.md).

## See Also

- [var recordTypes: [HKVerifiableClinicalRecordCredentialType]](hkverifiableclinicalrecordquerydescriptor/recordtypes.md)
  The types of records returned by this query.
- [var predicate: NSPredicate?](hkverifiableclinicalrecordquerydescriptor/predicate.md)
  A predicate that limits the results returned by the query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquerydescriptor/sourcetypes)*