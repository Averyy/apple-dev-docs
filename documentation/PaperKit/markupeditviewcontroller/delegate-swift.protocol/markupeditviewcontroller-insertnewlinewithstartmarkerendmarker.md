# markupEditViewController(_:insertNewLineWithStartMarker:endMarker:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Add a new line on top of the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
func markupEditViewController(_ markupEditViewController: MarkupEditViewController, insertNewLineWithStartMarker lineStartMarker: Bool, endMarker lineEndMarker: Bool)
```

## Parameters

- `markupEditViewController`: The source of the action.
- `lineStartMarker`: True if the start of the line has a marker / arrow.
- `lineEndMarker`: True if the end of the line has a marker / arrow.

## See Also

- [func markupEditViewController(MarkupEditViewController, insertNewShape: ShapeConfiguration.Shape)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewshape:).md)
  Add a new shape on top of the paper.
- [func markupEditViewControllerInsertNewTextbox(MarkupEditViewController)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontrollerinsertnewtextbox(_:).md)
  Add a new textbox on top of the paper.
- [func markupEditViewController(MarkupEditViewController, insertNewContents: PaperMarkup)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewcontents:).md)
  Add new content on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewlinewithstartmarker:endmarker:))*