# AssignableDocumentView

**Framework**: Assignables  
**Kind**: struct

SwiftUI View to display an `AssignableDocument`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct AssignableDocumentView
```

## Topics

### Creating a document view
- [init(document: Binding<AssignableDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignableDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocumentView.Document.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool)](assignabledocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:).md)
  Displays an `AssignableDocument`.
### Customizing the view
- [var body: some View](assignabledocumentview/body-swift.property.md)
  The content and behavior of the view.
- [AssignableDocumentView.Document](assignabledocumentview/document.md)
  The document type that this view presents.
### Initializers
- [init(document: Binding<AssignableDocumentView.Document>, activePartID: MergeablePartsContainerPartID?, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignableDocumentView.Document.Page.ID?>?, selectedQuestionID: Binding<AssignableDocumentView.Document.Question.ID?>?, showsPageThumbnails: Bool, isStructureEditingEnabled: Bool, allowsPencilDrawing: Bool, onMarkupActivation: (Bool) -> Void)](assignabledocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:allowspencildrawing:onmarkupactivation:).md)
  Displays an `AssignableDocument`.
### Type Aliases
- [AssignableDocumentView.Body](assignabledocumentview/body-swift.typealias.md)
  The type of view representing the body of this view.
### Default Implementations
- [View Implementations](assignabledocumentview/view-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [struct AssignedWorkDocumentView](assignedworkdocumentview.md)
  SwiftUI View to display an `AssignedWorkDocument`


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview)*