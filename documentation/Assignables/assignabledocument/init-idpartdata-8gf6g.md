# init(id:partData:)

**Framework**: Assignables  
**Kind**: init

Construct an instance of this object with the parts data passed in.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS ?+

## Declaration

```swift
init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : MergeablePartData]) async throws
```

## Parameters

- `id`: The ID of this document.
- `partData`: A dictionary of part IDs to   objects   that contain the parts data.

## See Also

- [init(pdfURL: URL, id: String?) throws](assignabledocument/init(pdfurl:id:).md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.
- [enum MergeablePartData](mergeablepartdata.md)
- [init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : URL]) throws](assignabledocument/init(id:partdata:)-4am19.md)
  Construct an instance of this object with the parts data passed in.
- [init(pdfURL: URL, authors: [some UserIdentity], id: String?) throws](assignabledocument/init(pdfurl:authors:id:).md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/init(id:partdata:)-8gf6g)*