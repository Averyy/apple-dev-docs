# init(documentType:predicate:limit:sortDescriptors:includeDocumentData:resultsHandler:)

**Framework**: HealthKit  
**Kind**: init

Instantiates and returns a document query.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
init(documentType: HKDocumentType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, includeDocumentData: Bool, resultsHandler: @escaping @Sendable (HKDocumentQuery, [HKDocumentSample]?, Bool, (any Error)?) -> Void)
```

#### Return Value

A newly initialized document query object.

#### Discussion

After you instantiate the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run it. Queries run on an anonymous background queue. As soon as the query is complete, the results handler is executed on the same background queue (but not necessarily on the same thread). You typically dispatch these results to the main queue to update the user interface.

## Parameters

- `documentType`: The type of document to search for. For a list of supported document types, see Document Type Identifier in [`HealthKit Constants`](healthkit-constants.md).
- `predicate`: A predicate that limits the results returned by the query. Pass `nil` to receive all the documents of the specified type.
- `limit`: The maximum number of samples returned by the query. If you want to return all matching samples, use [`HKObjectQueryNoLimit`](hkobjectquerynolimit.md).
- `sortDescriptors`: An array of sort descriptors that specify the order of the results returned by this query. Pass `nil` if you don’t need the results in a specific order. > **Note**:  HealthKit defines a number of sort identifiers (for example, [`HKSampleSortIdentifierStartDate`](hksamplesortidentifierstartdate.md)). Use the sort descriptors you create with these identifiers only in queries. You cannot use them to perform an in-memory sort of an array of samples.
- `includeDocumentData`: Pass [`true`](https://developer.apple.com/documentation/swift/true) to include the full document data. Pass [`false`](https://developer.apple.com/documentation/swift/false) to just receive a summary of the document. For CDA documents, the summary includes the title, the patient’s name, the author’s name, and the custodian’s name. Since the full document data can be quite large, only pass [`true`](https://developer.apple.com/documentation/swift/true) when you need to access the full document’s data.
- `resultsHandler`: A block that is called each time a new batch of documents is available. The document query returns its results incrementally in batches. The results handler may be called multiple times each time the query is executed. This block takes the following parameters: - **query**: A reference to the query calling this block.
- **results**: An array containing the samples returned by this query, or `nil` if an error occurred.
- **done**: A Boolean value that indicates whether the query is done. If [`true`](https://developer.apple.com/documentation/swift/true), the query is complete, and it will not call the results handler again. Otherwise, the query will call the results handler at least one more time, as soon as the next batch of documents is available.
- **error**: If an error occurs, this parameter contains an object describing the error; otherwise, it is `nil`.

## See Also

- [var HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumentquery/init(documenttype:predicate:limit:sortdescriptors:includedocumentdata:resultshandler:))*