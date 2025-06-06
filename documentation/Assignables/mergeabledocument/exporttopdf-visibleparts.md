# exportToPDF(visibleParts:)

**Framework**: Assignables  
**Kind**: method  
**Required**: Yes

Exports the indicated layers of this document into a single `PDFDocument`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
func exportToPDF(visibleParts: [Self.PartID]) async -> PDFDocument
```

## Parameters

- `visibleParts`: The lDs of layers that should be included in the thumbnail.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/mergeabledocument/exporttopdf(visibleparts:))*