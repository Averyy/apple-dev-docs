# includeDocumentData

**Framework**: HealthKit  
**Kind**: property

A Boolean value that indicates whether the sample includes the full document’s data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var includeDocumentData: Bool { get }
```

#### Discussion

This property contains the value passed to the [`init(documentType:predicate:limit:sortDescriptors:includeDocumentData:resultsHandler:)`](hkdocumentquery/init(documenttype:predicate:limit:sortdescriptors:includedocumentdata:resultshandler:).md) method’s `includeDocumentData` parameter.

## See Also

- [var limit: Int](hkdocumentquery/limit.md)
  The maximum number of documents the receiver will return upon completion.
- [var sortDescriptors: [NSSortDescriptor]?](hkdocumentquery/sortdescriptors.md)
  An array of sort descriptors that specify the order of the results returned by this query.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkdocumentquery/includedocumentdata)*