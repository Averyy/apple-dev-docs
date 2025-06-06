# init(document:activePartID:hiddenPartIDs:selectedPageID:selectedQuestionID:showsPageThumbnails:isStructureEditingEnabled:onMarkupActivation:)

**Framework**: Assignables  
**Kind**: init

Displays an `AssignedWorkDocument`.

**Availability**:
- iOS 18.1+
- iPadOS 18.1+
- Mac Catalyst 18.1+

## Declaration

```swift
@MainActor
@preconcurrency init(document: Binding<AssignedWorkDocumentView.Document>, activePartID: MergeablePartsContainerPartID? = nil, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignedWorkDocumentView.Document.Page.ID?>? = nil, selectedQuestionID: Binding<AssignableDocument.Question.ID?>? = nil, showsPageThumbnails: Bool = true, isStructureEditingEnabled: Bool = false, onMarkupActivation: @escaping (Bool) -> Void)
```

## Parameters

- `document`: A binding to the   to present in the view.
- `activePartID`: The   to enable user interaction on.
- `hiddenPartIDs`: A set of  s to hide on this view. Treated as a set.
- `selectedPageID`: A binding to the selected page.
- `selectedQuestionID`: A binding to the selected question.
- `showsPageThumbnails`: Controls showing or hiding the document pages thumbnail previews.
- `isStructureEditingEnabled`: Controls access to actions that allow changing the structure   of the document on the page thumbnail view contextual menu (i.e. add/duplicate/move/remove pages).
- `onMarkupActivation`: An action performed when the user started or ended a drawing sequence with an Apple Pencil.


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:onmarkupactivation:))*