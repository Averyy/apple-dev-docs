# markupToolbarViewController(_:insertNewLineWithStartMarker:endMarker:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Add a new line on top of the paper.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
func markupToolbarViewController(_ markupToolbarViewController: MarkupToolbarViewController, insertNewLineWithStartMarker lineStartMarker: Bool, endMarker lineEndMarker: Bool)
```

## Parameters

- `markupToolbarViewController`: The source of the action.
- `lineStartMarker`: True if the start of the line has a marker / arrow.
- `lineEndMarker`: True if the end of the line has a marker / arrow.

## See Also

- [func markupToolbarViewController(MarkupToolbarViewController, insertNewShape: ShapeConfiguration.Shape)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewshape:).md)
  Add a new shape on top of the paper.
- [func markupToolbarViewControllerInsertNewTextbox(MarkupToolbarViewController)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontrollerinsertnewtextbox(_:).md)
  Add a new textbox on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewContents: PaperMarkup)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewcontents:).md)
  Add new content on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewlinewithstartmarker:endmarker:))*