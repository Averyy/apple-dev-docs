# exportParts(identifiedBy:)

**Framework**: Assignables  
**Kind**: method

Given a set of part identifiers, return a dictionary of part ID to part data.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS ?+

## Declaration

```swift
func exportParts(identifiedBy partIDs: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : MergeablePartData]
```

#### Return Value

A dictionary of part ID to part data file for the requested parts.

## Parameters

- `partIDs`: An array of part IDs to export. This is treated as a set.

## See Also

- [func exportBaseAsPDF() async -> PDFDocument](assignabledocument/exportbaseaspdf.md)
  Exports the base part of this document to a `PDFDocument`.
- [func export(partIDs: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : URL]](assignabledocument/export(partids:).md)
  Given a set of part identifiers, return a dictionary of part ID to data objects for the requested layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/exportparts(identifiedby:))*