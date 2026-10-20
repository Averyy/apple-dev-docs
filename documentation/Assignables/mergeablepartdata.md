# MergeablePartData

**Framework**: Assignables  
**Kind**: enum  
**Role**: Enumeration

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS

## Declaration

```swift
enum MergeablePartData
```

## Topics

### Enumeration Cases
- [MergeablePartData.data(_:)](./mergeablepartdata/data%28_%29.md)
  Part data exported as a `Data` object.
- [MergeablePartData.fileURL(_:)](./mergeablepartdata/fileurl%28_%29.md)
  Part data exported as a file URL to a part data archive.

## See Also

### Creating an assignable document
- [init(pdfURL: URL, id: String?) throws](./assignabledocument/init%28pdfurl,id%29.md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.
- [init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : MergeablePartData]) async throws](./assignabledocument/init%28id,partdata%29-8gf6g.md)
  Construct an instance of this object with the parts data passed in.
- [init(id: AssignableDocument.ID, partData: [AssignableDocument.PartID : URL]) throws](./assignabledocument/init%28id,partdata%29-4am19.md)
  Construct an instance of this object with the parts data passed in.
- [init(pdfURL: URL, authors: [some UserIdentity], id: String?) throws](./assignabledocument/init%28pdfurl,authors,id%29.md)
  Initializes a new assessment document that is based on the PDF located at the provided URL. If the file located at the URL provided cannot be accessed, this initializer throws.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeablepartdata)*