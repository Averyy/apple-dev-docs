# export(partIDs:)

**Framework**: Assignables  
**Kind**: method

Given a set of part identifiers, return a dictionary of part ID to data objects for the requested layers.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
func export(partIDs: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : URL]
```

#### Return Value

A dictionary of part ID to URLs of the data stored on disk for the requested parts.

## Parameters

- `partIDs`: An array of part IDs to export. This is treated as a set.

## See Also

- [func exportBaseAsPDF() async -> PDFDocument](assignabledocument/exportbaseaspdf.md)
  Exports the base part of this document to a `PDFDocument`.
- [func exportParts(identifiedBy: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : MergeablePartData]](assignabledocument/exportparts(identifiedby:).md)
  Given a set of part identifiers, return a dictionary of part ID to part data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/export(partids:))*