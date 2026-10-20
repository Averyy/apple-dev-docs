# questionThumbnails(visibleParts:)

**Framework**: Assignables  
**Kind**: method

Produces thumbnails of question regions within the document.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
func questionThumbnails(visibleParts: [AssignedWorkDocument.PartID]) async -> [AssignableDocument.Question.ID : [AssignableDocument.Question.Thumbnail]]
```

#### Return Value

A dictionary of [`AssignableDocument.Question.ID`](assignabledocument/question/id-swift.typealias.md): array of [`AssignableDocument.Question.Thumbnail`](assignabledocument/question/thumbnail.md).

## Parameters

- `visibleParts`: The parts to display in the thumbnails.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocument/questionthumbnails(visibleparts:))*