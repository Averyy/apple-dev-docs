# init(document:activePartID:hiddenPartIDs:selectedPageID:selectedQuestionID:showsPageThumbnails:isStructureEditingEnabled:)

**Framework**: Assignables  
**Kind**: init

Displays an `AssignableDocument`.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- Mac Catalyst 17.4+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency init(document: Binding<AssignableDocumentView.Document>, activePartID: MergeablePartsContainerPartID? = nil, hiddenPartIDs: [MergeablePartsContainerPartID] = [], selectedPageID: Binding<AssignableDocumentView.Document.Page.ID?>? = nil, selectedQuestionID: Binding<AssignableDocumentView.Document.Question.ID?>? = nil, showsPageThumbnails: Bool = true, isStructureEditingEnabled: Bool = true)
```

#### Discussion

- Example:

```None
    AssignableDocumentView(
        document: $document,
        activePartID: activeLayerID,
        hiddenPartIDs: hiddenPartIDs,
        selectedPageID: $selectedPageID,
        showsPageThumbnails: isMultiPageDocument,
        isStructureEditingEnabled: false,
        onMarkupActivation: { isMarkupActivated in
            if isMarkupActivated {
                activeLayerID = AssignableDocument.PartIDs.instructionMarkup
                isMarkupSelected = true
            }
        }
    )
```

## Parameters

- `document`: A binding to the   to present in the view.
- `activePartID`: The   to enable user interaction on.
- `hiddenPartIDs`: A set of  s to hide on this view. Treated as a set.
- `selectedPageID`: A binding to the selected page id.
- `selectedQuestionID`: A binding to the selected question id.
- `showsPageThumbnails`: Controls showing or hiding the document pages thumbnail previews.
- `isStructureEditingEnabled`: Controls access to actions that allow changing the structure   of the document on the page thumbnail view contextual menu (i.e. add/duplicate/move/remove pages).


---

*[View on Apple Developer](https://developer.apple.com/documentation/assignables/assignabledocumentview/init(document:activepartid:hiddenpartids:selectedpageid:selectedquestionid:showspagethumbnails:isstructureeditingenabled:))*