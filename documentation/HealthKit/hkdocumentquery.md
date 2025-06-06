# HKDocumentQuery

**Framework**: HealthKit  
**Kind**: class

A query that returns a snapshot of all matching documents currently saved in the HealthKit store.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class HKDocumentQuery
```

## Mentions

- [Reading data from HealthKit](reading-data-from-healthkit.md)

#### Overview

Use an `HKDocumentQuery` object to search for documents in the HealthKit store. You can provide a predicate to filter the search results, a sort order for the returned samples, or even a limit to the number of samples returned.

Document queries are immutable: The query’s properties are set when the query is first created. They cannot change.

##### Executing Queries

To create and execute a query, perform the following steps:

1. Create the document type by calling the [`HKObjectType`](hkobjecttype.md) class’s [`documentType(forIdentifier:)`](hkobjecttype/documenttype(foridentifier:).md) method.
2. (optionally) Create an [`NSPredicate`](https://developer.apple.com/documentation/Foundation/NSPredicate) object to filter the search results.
3. (optionally) Create an array of [`NSSortDescriptor`](https://developer.apple.com/documentation/Foundation/NSSortDescriptor) objects to provide the sort order for the results.
4. Instantiate a new query by calling the [`init(documentType:predicate:limit:sortDescriptors:includeDocumentData:resultsHandler:)`](hkdocumentquery/init(documenttype:predicate:limit:sortdescriptors:includedocumentdata:resultshandler:).md) method.
5. In the results handler, handle any errors and process the results.

Note, the query returns the results in batches and may call the results handler more than once. If the `done` parameter is set to [`false`](https://developer.apple.com/documentation/swift/false), the query is still active and will call the results handler with additional results. If the `done` parameter is set to [`true`](https://developer.apple.com/documentation/swift/true), the query is complete.

```swift
guard let cdaType = HKObjectType.documentType(forIdentifier: .CDA) else {
    fatalError("Unable to create a CDA document type.")
}
 
var allDocuments = [HKDocumentSample]()
let cdaQuery = HKDocumentQuery(documentType: cdaType,
                               predicate: nil,
                               limit: HKObjectQueryNoLimit,
                               sortDescriptors: nil,
                               includeDocumentData: false) {
                                
                                (query, resultsOrNil, done, errorOrNil) in
                                
                                guard let results = resultsOrNil else {
                                    if let queryError = errorOrNil {
                                        // Handle the query error here...
                                    }
                                    
                                    return
                                }
                                
                                allDocuments += results
                                
                                if done {
                                    // the allDocuments array now contains all the samples returned by the query.
                                    // Handle the documents here...
                                }
}
```

##### Subclassing Document Queries

Like many HealthKit classes, the `HKDocumentQuery` class should not be subclassed.

## Topics

### Creating Document Queries
- [init(documentType: HKDocumentType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, includeDocumentData: Bool, resultsHandler: (HKDocumentQuery, [HKDocumentSample]?, Bool, (any Error)?) -> Void)](hkdocumentquery/init(documenttype:predicate:limit:sortdescriptors:includedocumentdata:resultshandler:).md)
  Instantiates and returns a document query.
- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.
### Accessing the Document Query’s Properties
- [var includeDocumentData: Bool](hkdocumentquery/includedocumentdata.md)
  A Boolean value that indicates whether the sample includes the full document’s data.
- [var limit: Int](hkdocumentquery/limit.md)
  The maximum number of documents the receiver will return upon completion.
- [var sortDescriptors: [NSSortDescriptor]?](hkdocumentquery/sortdescriptors.md)
  An array of sort descriptors that specify the order of the results returned by this query.

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
- [class HKVerifiableClinicalRecordQuery](hkverifiableclinicalrecordquery.md)
  A query for one-time access to a SMART Health Card or EU Digital COVID Certificate.
- [struct HKVerifiableClinicalRecordSourceType](hkverifiableclinicalrecordsourcetype.md)
  The source type for the verifiable clinical record.
- [struct HKVerifiableClinicalRecordCredentialType](hkverifiableclinicalrecordcredentialtype.md)
  The type of record returned by a verifiable clinical record query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumentquery)*