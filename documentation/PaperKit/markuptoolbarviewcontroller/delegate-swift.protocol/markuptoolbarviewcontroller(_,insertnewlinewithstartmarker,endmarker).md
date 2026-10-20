# markupToolbarViewController(_:insertNewLineWithStartMarker:endMarker:)

**Framework**: PaperKit  
**Kind**: method  
**Role**: Instance Method  
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

### Inserting content
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewShape: ShapeConfiguration.Shape)](./markuptoolbarviewcontroller%28_,insertnewshape%29.md)
  Add a new shape on top of the paper.
- [func markupToolbarViewControllerInsertNewTextbox(MarkupToolbarViewController)](./markuptoolbarviewcontrollerinsertnewtextbox%28_%29.md)
  Add a new textbox on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewContents: PaperMarkup)](./markuptoolbarviewcontroller%28_,insertnewcontents%29.md)
  Add new content on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewlinewithstartmarker:endmarker:))*