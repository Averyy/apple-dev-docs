# AssignedWorkDocumentView

**Framework**: Assignables  
**Kind**: struct

SwiftUI View to display an `AssignedWorkDocument`

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct AssignedWorkDocumentView
```

## Topics

### Creating a document view
- [init(document: Binding<AssignedWorkDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignedWorkDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocument.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool)](assignedworkdocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:).md)
  Displays an `AssignedWorkDocument`.
### Implementing a view
- [var body: some View](assignedworkdocumentview/body-swift.property.md)
  The content and behavior of the view.
- [AssignedWorkDocumentView.Document](assignedworkdocumentview/document.md)
  The document type that this view presents.
### Initializers
- [init(document: Binding<AssignedWorkDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignedWorkDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocument.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool, onMarkupActivation: (Bool) -> Void)](assignedworkdocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:onmarkupactivation:).md)
  Displays an `AssignedWorkDocument`.
### Type Aliases
- [AssignedWorkDocumentView.Body](assignedworkdocumentview/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](assignedworkdocumentview/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct AssignableDocumentView](assignabledocumentview.md)
  SwiftUI View to display an `AssignableDocument`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview)*