# HKVerifiableClinicalRecordQuery

**Framework**: HealthKit  
**Kind**: class

A query for one-time access to a SMART Health Card or EU Digital COVID Certificate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- visionOS ?+

## Declaration

```swift
class HKVerifiableClinicalRecordQuery
```

#### Overview

> **Note**:  To use Swift concurrency when reading verifiable clinical records, see [`HKVerifiableClinicalRecordQueryDescriptor`](hkverifiableclinicalrecordquerydescriptor.md).

 To use Swift concurrency when reading verifiable clinical records, see [`HKVerifiableClinicalRecordQueryDescriptor`](hkverifiableclinicalrecordquerydescriptor.md).

Use an [`HKVerifiableClinicalRecordQuery`](hkverifiableclinicalrecordquery.md) object to request one-time access to a SMART Health Card or EU Digital COVID Certificate. For example, the following code requests cards that represent immunizations within the last six months.

```swift
// Calculate the start and end dates.
var sixMonthsAgo = DateComponents()
sixMonthsAgo.month = -6

let end = Date()
guard let start = Calendar.current.date(byAdding: sixMonthsAgo, to: end) else {
    fatalError("*** Unable to calculate a date using \(end) and \(sixMonthsAgo) ***")
}

// Create the predicate.
let lastSixMonthsPredicate =
HKQuery.predicateForVerifiableClinicalRecords(withRelevantDateWithin: DateInterval(start: start, end: end))

// Create the query for immunization cards.
let query = HKVerifiableClinicalRecordQuery(
    recordTypes: [HKVerifiableClinicalRecordCredentialType.covid19.rawValue,
                  HKVerifiableClinicalRecordCredentialType.immunization.rawValue],
    sourceTypes: [.smartHealthCard, .euDigitalCOVIDCertificate],
    predicate: lastSixMonthsPredicate) { query, records, error in
        
        if let error = error {
            // Handle errors here.
            fatalError("*** An error occurred: \(error.localizedDescription)***")
        }
        
        if let records = records {
            
            // Use the records here.
            for record in records {
                print(record.recordTypes)
                print(record.itemNames)
                print(record.issuedDate)
                print(record.expirationDate ?? "No expiration date.")
            }
        }
    }

// Run the query.
store.execute(query)
```

Unlike other HealthKit queries, you don’t need to request permission to read verifiable health records before running this query. HealthKit prompts the user for permission to read the records each time you run the query.

> **Note**:  Running an [`HKVerifiableClinicalRecordQuery`](hkverifiableclinicalrecordquery.md) requires a special entitlement from Apple, or the query fails with an [`HKError.Code.errorAuthorizationDenied`](hkerror/code/errorauthorizationdenied.md) error. To request the entitlement, see [`Request Access to the Verifiable Health Records Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/verifiable-health-records/).

 Running an [`HKVerifiableClinicalRecordQuery`](hkverifiableclinicalrecordquery.md) requires a special entitlement from Apple, or the query fails with an [`HKError.Code.errorAuthorizationDenied`](hkerror/code/errorauthorizationdenied.md) error. To request the entitlement, see [`Request Access to the Verifiable Health Records Entitlement`](https://developer.apple.comhttps://developer.apple.com/contact/request/verifiable-health-records/).

## Topics

### Creating Queries
- [init(recordTypes: [String], sourceTypes: [HKVerifiableClinicalRecordSourceType], predicate: NSPredicate?, resultsHandler: (HKVerifiableClinicalRecordQuery, [HKVerifiableClinicalRecord]?, (any Error)?) -> Void)](hkverifiableclinicalrecordquery/init(recordtypes:sourcetypes:predicate:resultshandler:).md)
  Creates a query for one-time access to a verifiable clinical record.
- [init(recordTypes: [String], predicate: NSPredicate?, resultsHandler: (HKVerifiableClinicalRecordQuery, [HKVerifiableClinicalRecord]?, (any Error)?) -> Void)](hkverifiableclinicalrecordquery/init(recordtypes:predicate:resultshandler:).md)
  Creates a query for one-time access to a SMART Health Card.
### Accessing the Metadata
- [var recordTypes: [String]](hkverifiableclinicalrecordquery/recordtypes.md)
  The type of records that this query returns.
- [var sourceTypes: [HKVerifiableClinicalRecordSourceType]](hkverifiableclinicalrecordquery/sourcetypes.md)
  The format of the verifiable clinical record.

## Relationships

### Inherits From
- [HKQuery](hkquery.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct HKVerifiableClinicalRecordQueryDescriptor](hkverifiableclinicalrecordquerydescriptor.md)
  A query interface that provides one-time access to a SMART Health Card or EU Digital COVID Certificate using Swift concurrency.
- [struct HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [struct HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype.md)
  The type of record returned by a verifiable clinical record query.
- [class HKDocumentQuery](hkdocumentquery.md)
  A query that returns a snapshot of all matching documents currently saved in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkverifiableclinicalrecordquery)*