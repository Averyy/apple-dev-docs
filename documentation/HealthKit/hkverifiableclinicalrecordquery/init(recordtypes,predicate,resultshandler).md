# init(recordTypes:predicate:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init  
**Role**: Initializer

Creates a query for one-time access to a SMART Health Card.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- visionOS

## Declaration

```swift
init(recordTypes: [String], predicate: NSPredicate?, resultsHandler: @escaping @Sendable (HKVerifiableClinicalRecordQuery, [HKVerifiableClinicalRecord]?, (any Error)?) -> Void)
```

```objc
- (instancetype) initWithRecordTypes:(NSArray<NSString *> *) recordTypes predicate:(NSPredicate *) predicate resultsHandler:(void (^)(HKVerifiableClinicalRecordQuery *query, NSArray<HKVerifiableClinicalRecord *> *records, NSError *error)) resultsHandler;
```

## Parameters

- `recordTypes`: The types of records that the query returns.
- `predicate`: A predicate that limits the results that they query returns. Pass `nil` to receive all records of the specified type.
- `resultsHandler`: A block that the HealthKit store calls after it finishes executing the query.

  This block takes the following parameters:

  - **`query`**: A reference to the query that called this block.
  - **`records`**: An array containing the verifiable health records found by the query, or `nil` if an error occurs.
  - **`error`**: If an error occurs, an object describing the error; otherwise, it’s `nil`.

## See Also

### Creating Queries
- [init(recordTypes: [String], sourceTypes: [HKVerifiableClinicalRecordSourceType], predicate: NSPredicate?, resultsHandler: (HKVerifiableClinicalRecordQuery, [HKVerifiableClinicalRecord]?, (any Error)?) -> Void)](./init%28recordtypes,sourcetypes,predicate,resultshandler%29.md)
  Creates a query for one-time access to a verifiable clinical record.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquery/init(recordtypes:predicate:resultshandler:))*