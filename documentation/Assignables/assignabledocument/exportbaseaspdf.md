# exportBaseAsPDF()

**Framework**: Assignables  
**Kind**: method

Exports the base part of this document to a `PDFDocument`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
func exportBaseAsPDF() async -> PDFDocument
```

#### Return Value

The base part of this document as a `PDFDocument`.

## See Also

- [func exportParts(identifiedBy: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : MergeablePartData]](assignabledocument/exportparts(identifiedby:).md)
  Given a set of part identifiers, return a dictionary of part ID to part data.
- [func export(partIDs: [AssignableDocument.PartID]) async throws -> [AssignableDocument.PartID : URL]](assignabledocument/export(partids:).md)
  Given a set of part identifiers, return a dictionary of part ID to data objects for the requested layers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocument/exportbaseaspdf())*