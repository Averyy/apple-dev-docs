# documentData

**Framework**: HealthKit  
**Kind**: property

The CDA document stored as XML data.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var documentData: Data? { get }
```

#### Discussion

The CDA document’s XML format is specified by the [`Clinical Document Architecture, R2`](https://developer.apple.comhttp://www.hl7.org/implement/standards/product_brief.cfm?product_id=7) standard. .

When using an [`HKDocumentQuery`](hkdocumentquery.md) object to retrieve documents from the HealthKit store, if the query’s [`includeDocumentData`](hkdocumentquery/includedocumentdata.md) property is set to [`false`](https://developer.apple.com/documentation/swift/false), the retrieved documents will have `nil`-valued `documentData` properties.

## See Also

- [var authorName: String](hkcdadocument/authorname.md)
  The document’s author.
- [var custodianName: String](hkcdadocument/custodianname.md)
  The name of the organization responsible for the document.
- [var patientName: String](hkcdadocument/patientname.md)
  The patient’s name.
- [var title: String](hkcdadocument/title.md)
  The document’s title.


---

*[View on Apple Developer](https://developer.apple.com/documentation/healthkit/hkcdadocument/documentdata)*