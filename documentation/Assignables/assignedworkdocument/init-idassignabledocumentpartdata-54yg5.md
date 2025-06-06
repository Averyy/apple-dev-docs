# init(id:assignableDocument:partData:)

**Framework**: Assignables  
**Kind**: init

Construct an instance of this object with the parts data passed in.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
init(id: AssignedWorkDocument.ID, assignableDocument: AssignableDocument, partData: [AssignedWorkDocument.PartID : URL]) throws
```

## Parameters

- `id`: The ID of the document.
- `assignableDocument`: The assignable document that this work document is based on.
- `partData`: A dictionary of part ID to URLs of the data stored on disk for the requested parts.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/init(id:assignabledocument:partdata:)-54yg5)*