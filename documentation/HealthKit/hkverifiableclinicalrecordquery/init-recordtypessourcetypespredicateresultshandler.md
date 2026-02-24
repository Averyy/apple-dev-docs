# init(recordTypes:sourceTypes:predicate:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

Creates a query for one-time access to a verifiable clinical record.

**Availability**:
- iOS 15.4+
- iPadOS 15.4+
- Mac Catalyst 15.4+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(recordTypes: [String], sourceTypes: [HKVerifiableClinicalRecordSourceType], predicate: NSPredicate?, resultsHandler: @escaping @Sendable (HKVerifiableClinicalRecordQuery, [HKVerifiableClinicalRecord]?, (any Error)?) -> Void)
```

## Parameters

- `recordTypes`: The types of records that this query returns. For a list of valid record types, see [`HKVerifiableClinicalRecordCredentialType`](hkverifiableclinicalrecordcredentialtype.md).
- `sourceTypes`: The format of the verifiable clinical records. For a list of valid sources, see [`HKVerifiableClinicalRecordSourceType`](hkverifiableclinicalrecordsourcetype.md).
- `predicate`: A predicate that limits the results that this query returns. Pass `nil` to receive all records of the specified source and record type.
- `resultsHandler`: A block that the HealthKit store calls after it finishes executing the query. This block takes the following parameters: - **`query`**: A reference to the query that called this block.
- **`records`**: An array containing the verifiable health records found by the query, or `nil` if an error occurs.
- **`error`**: If an error occurs, an object describing the error; otherwise, it’s `nil`.

## See Also

- [init(recordTypes: [String], predicate: NSPredicate?, resultsHandler: (HKVerifiableClinicalRecordQuery, [HKVerifiableClinicalRecord]?, (any Error)?) -> Void)](hkverifiableclinicalrecordquery/init(recordtypes:predicate:resultshandler:).md)
  Creates a query for one-time access to a SMART Health Card.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquery/init(recordtypes:sourcetypes:predicate:resultshandler:))*