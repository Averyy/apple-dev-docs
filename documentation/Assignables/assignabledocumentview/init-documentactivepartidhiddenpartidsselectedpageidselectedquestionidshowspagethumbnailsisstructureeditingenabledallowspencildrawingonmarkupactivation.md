# init(document:activePartID:hiddenPartIDs:selectedPageID:selectedQuestionID:showsPageThumbnails:isStructureEditingEnabled:allowsPencilDrawing:onMarkupActivation:)

**Framework**: Assignables  
**Kind**: init

Displays an `AssignableDocument`.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+

## Declaration

```swift
@MainActor
@preconcurrency init(document: Binding<AssignableDocumentView.Document>, activePartID: MergeablePartsContainerPartID? = nil, hiddenPartIDs: [MergeablePartsContainerPartID] = [], selectedPageID: Binding<AssignableDocumentView.Document.Page.ID?>? = nil, selectedQuestionID: Binding<AssignableDocumentView.Document.Question.ID?>? = nil, showsPageThumbnails: Bool = true, isStructureEditingEnabled: Bool = true, allowsPencilDrawing: Bool = true, onMarkupActivation: @escaping (Bool) -> Void)
```

## Parameters

- `document`: A binding to the   to present in the view.
- `activePartID`: The   to enable user interaction on.
- `hiddenPartIDs`: A set of  s to hide on this view. Treated as a set.
- `selectedPageID`: A binding to the selected page id.
- `selectedQuestionID`: A binding to the selected question id.
- `showsPageThumbnails`: Controls showing or hiding the document pages thumbnail previews.
- `isStructureEditingEnabled`: Controls access to actions that allow changing the structure   of the document on the page thumbnail view contextual menu (i.e. add/duplicate/move/remove pages).
- `onMarkupActivation`: An action performed when the user started or ended a drawing sequence with an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:allowspencildrawing:onmarkupactivation:))*