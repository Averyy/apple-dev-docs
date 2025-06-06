# init(document:activePartID:hiddenPartIDs:selectedPageID:selectedQuestionID:showsPageThumbnails:isStructureEditingEnabled:)

**Framework**: Assignables  
**Kind**: init

Displays an `AssignedWorkDocument`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(document: Binding<AssignedWorkDocumentView.Document>, activePartID: MergeablePartsContainerPartID? = nil, hiddenPartIDs: [MergeablePartsContainerPartID], selectedPageID: Binding<AssignedWorkDocumentView.Document.Page.ID?>? = nil, selectedQuestionID: Binding<AssignableDocument.Question.ID?>? = nil, showsPageThumbnails: Bool = true, isStructureEditingEnabled: Bool = false)
```

#### Discussion

- Example:

```None
    AssignedWorkDocumentView(
        document: $document,
        activePartID: activeLayerID,
        hiddenPartIDs: hiddenPartIDs,
        selectedPageID: $selectedPageID,
        showsPageThumbnails: isMultiPageDocument,
        isStructureEditingEnabled: false,
        onMarkupActivation: { isMarkupActivated in
            if isMarkupActivated {
                activeLayerID = AssignedWorkDocument.PartIDs.scorerMarkup
                isMarkupSelected = true
            }
        }
    )
```

## Parameters

- `document`: A binding to the   to present in the view.
- `activePartID`: The   to enable user interaction on.
- `hiddenPartIDs`: A set of  s to hide on this view. Treated as a set.
- `selectedPageID`: A binding to the selected page.
- `selectedQuestionID`: A binding to the selected question.
- `showsPageThumbnails`: Controls showing or hiding the document pages thumbnail previews.
- `isStructureEditingEnabled`: Controls access to actions that allow changing the structure   of the document on the page thumbnail view contextual menu (i.e. add/duplicate/move/remove pages).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignedworkdocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:))*