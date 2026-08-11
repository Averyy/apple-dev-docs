# markupEditViewController(_:insertNewContents:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Add new content on top of the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
func markupEditViewController(_ markupEditViewController: MarkupEditViewController, insertNewContents toInsert: PaperMarkup)
```

#### Discussion

This is used for inserting any custom content, and non-shape elements like signatures or loupes.

## Parameters

- `markupEditViewController`: The source of the action.
- `toInsert`: The markup whose contents is added on top of this paper.

## See Also

- [func markupEditViewController(MarkupEditViewController, insertNewShape: ShapeConfiguration.Shape)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewshape:).md)
  Add a new shape on top of the paper.
- [func markupEditViewControllerInsertNewTextbox(MarkupEditViewController)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontrollerinsertnewtextbox(_:).md)
  Add a new textbox on top of the paper.
- [func markupEditViewController(MarkupEditViewController, insertNewLineWithStartMarker: Bool, endMarker: Bool)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewlinewithstartmarker:endmarker:).md)
  Add a new line on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewcontents:))*