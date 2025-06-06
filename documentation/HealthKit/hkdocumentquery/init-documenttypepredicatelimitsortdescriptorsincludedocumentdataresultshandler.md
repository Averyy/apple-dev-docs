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
init(documentType: HKDocumentType, predicate: NSPredicate?, limit: Int, sortDescriptors: [NSSortDescriptor]?, includeDocumentData: Bool, resultsHandler: @escaping (HKDocumentQuery, [HKDocumentSample]?, Bool, (any Error)?) -> Void)
```

#### Return Value

A newly initialized document query object.

#### Discussion

After you instantiate the query, call the [`HKHealthStore`](hkhealthstore.md) class’s [`execute(_:)`](hkhealthstore/execute(_:).md) method to run it. Queries run on an anonymous background queue. As soon as the query is complete, the results handler is executed on the same background queue (but not necessarily on the same thread). You typically dispatch these results to the main queue to update the user interface.

## Parameters

- `documentType`: The type of document to search for. For a list of supported document types, see Document Type Identifier in  .
- `predicate`: A predicate that limits the results returned by the query. Pass   to receive all the documents of the specified type.
- `limit`: The maximum number of samples returned by the query. If you want to return all matching samples, use  .
- `sortDescriptors`: An array of sort descriptors that specify the order of the results returned by this query. Pass   if you don’t need the results in a specific order.
- `includeDocumentData`: Since the full document data can be quite large, only pass   when you need to access the full document’s data.
- `resultsHandler`: This block takes the following parameters:

## See Also

- [let HKObjectQueryNoLimit: Int](hkobjectquerynolimit.md)
  A value indicating that the query returns all the matching samples in the HealthKit store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumentquery/init(documenttype:predicate:limit:sortdescriptors:includedocumentdata:resultshandler:))*