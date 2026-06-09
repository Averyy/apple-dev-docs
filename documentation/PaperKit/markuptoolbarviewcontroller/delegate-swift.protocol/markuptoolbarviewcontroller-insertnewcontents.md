# markupToolbarViewController(_:insertNewContents:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Add new content on top of the paper.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func markupToolbarViewController(_ markupToolbarViewController: MarkupToolbarViewController, insertNewContents toInsert: PaperMarkup)
```

#### Discussion

This is used for inserting any custom content, and non-shape elements like signatures or loupes.

## Parameters

- `markupToolbarViewController`: The source of the action.
- `toInsert`: The markup whose contents is added on top of this paper.

## See Also

- [func markupToolbarViewController(MarkupToolbarViewController, insertNewShape: ShapeConfiguration.Shape)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewshape:).md)
  Add a new shape on top of the paper.
- [func markupToolbarViewControllerInsertNewTextbox(MarkupToolbarViewController)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontrollerinsertnewtextbox(_:).md)
  Add a new textbox on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewLineWithStartMarker: Bool, endMarker: Bool)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewlinewithstartmarker:endmarker:).md)
  Add a new line on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewcontents:))*