# init(recordTypes:sourceTypes:predicate:)

**Framework**: HealthKit  
**Kind**: init

Creates a query descriptor for reading verifiable clinical records.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS ?+

## Declaration

```swift
init(recordTypes: [HKVerifiableClinicalRecordCredentialType], sourceTypes: [HKVerifiableClinicalRecordSourceType], predicate: NSPredicate? = nil)
```

## Parameters

- `recordTypes`: The types of records that this query returns. For a list of valid record types, see  .
- `sourceTypes`: The format of the verifiable clinical records. For a list of valid sources, see  .
- `predicate`: A predicate that limits the results that this query returns. Pass   to receive all records of the specified source and record type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquerydescriptor/init(recordtypes:sourcetypes:predicate:))*