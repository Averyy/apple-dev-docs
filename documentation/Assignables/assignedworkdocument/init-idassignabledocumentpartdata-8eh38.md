# init(id:assignableDocument:partData:)

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
init(id: AssignedWorkDocument.ID, assignableDocument: AssignableDocument, partData: [AssignedWorkDocument.PartID : MergeablePartData]) async throws
```

## Parameters

- `id`: The ID of this document.
- `partData`: A dictionary of part IDs to   objects   that contain the parts data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/init(id:assignabledocument:partdata:)-8eh38)*