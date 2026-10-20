# AssignedWorkDocumentView

**Framework**: Assignables  
**Kind**: struct  
**Role**: Structure

SwiftUI View to display an `AssignedWorkDocument`

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency struct AssignedWorkDocumentView
```

## Topics

### Creating a document view
- [init(document: Binding<AssignedWorkDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignedWorkDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocument.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool)](./assignedworkdocumentview/init%28document,activepartid,hiddenpartids,selectedpageid,selectedquestionid,showspagethumbnails,isstructureeditingenabled%29.md)
  Displays an `AssignedWorkDocument`.
### Implementing a view
- [AssignedWorkDocumentView.Document](./assignedworkdocumentview/document.md)
  The document type that this view presents.
### Initializers
- [init(document: Binding<AssignedWorkDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignedWorkDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocument.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool, onMarkupActivation: (Bool) -> Void)](./assignedworkdocumentview/init%28document,activepartid,hiddenpartids,selectedpageid,selectedquestionid,showspagethumbnails,isstructureeditingenabled,onmarkupactivation%29.md)
  Displays an `AssignedWorkDocument`.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [View](../SwiftUI/view.md)

## See Also

### Presentation
- [struct AssignableDocumentView](./assignabledocumentview.md)
  SwiftUI View to display an `AssignableDocument`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview)*