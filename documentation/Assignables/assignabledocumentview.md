# AssignableDocumentView

**Framework**: Assignables  
**Kind**: struct  
**Role**: Structure

SwiftUI View to display an `AssignableDocument`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency struct AssignableDocumentView
```

## Topics

### Creating a document view
- [init(document: Binding<AssignableDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignableDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocumentView.Document.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool)](./assignabledocumentview/init%28document,activepartid,hiddenpartids,selectedpageid,selectedquestionid,showspagethumbnails,isstructureeditingenabled%29.md)
  Displays an `AssignableDocument`.
### Customizing the view
- [AssignableDocumentView.Document](./assignabledocumentview/document.md)
  The document type that this view presents.
### Initializers
- [init(document: Binding<AssignableDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignableDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocumentView.Document.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool, allowsPencilDrawing: Bool, onMarkupActivation: (Bool) -> Void)](./assignabledocumentview/init%28document,activepartid,hiddenpartids,selectedpageid,selectedquestionid,showspagethumbnails,isstructureeditingenabled,allowspencildrawing,onmarkupactivation%29.md)
  Displays an `AssignableDocument`.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Presentation
- [struct AssignedWorkDocumentView](./assignedworkdocumentview.md)
  SwiftUI View to display an `AssignedWorkDocument`


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview)*