# init(pdfURL:id:)

**Framework**: Assignables  
**Kind**: init

Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
init(pdfURL: URL, id: String? = nil) throws
```

## Parameters

- `pdfURL`: A URL to the PDF document that   is the basis of this assessment document.
- `id`: An optional ID to use for this document.   if one is not provided, a random UUID string will be used.

## See Also

- [init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : MergeablePartData]) async throws](assignabledocument/init(id:partdata:)-8gf6g.md)
  Construct an instance of this object with the parts data passed in.
- [enum MergeablePartData](mergeablepartdata.md)
- [init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : URL]) throws](assignabledocument/init(id:partdata:)-4am19.md)
  Construct an instance of this object with the parts data passed in.
- [init(pdfURL: URL, authors: [some UserIdentity], id: String?) throws](assignabledocument/init(pdfurl:authors:id:).md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/init(pdfurl:id:))*