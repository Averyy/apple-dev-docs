# markupToolbarViewController(_:insertNewContents:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Add new content on top of the paper.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func markupToolbarViewController(_ markupToolbarViewController: MarkupToolbarViewController, insertNewContents toInsert: PaperMarkup)
```

## Discussion

This is used for inserting any custom content, and non-shape elements like signatures or loupes.

## Parameters

- `markupToolbarViewController`: The source of the action.
- `toInsert`: The markup whose contents is added on top of this paper.

## See Also

### Inserting content
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewShape: ShapeConfiguration.Shape)](./markuptoolbarviewcontroller%28_,insertnewshape%29.md)
  Add a new shape on top of the paper.
- [func markupToolbarViewControllerInsertNewTextbox(MarkupToolbarViewController)](./markuptoolbarviewcontrollerinsertnewtextbox%28_%29.md)
  Add a new textbox on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewLineWithStartMarker: Bool, endMarker: Bool)](./markuptoolbarviewcontroller%28_,insertnewlinewithstartmarker,endmarker%29.md)
  Add a new line on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewcontents:))*