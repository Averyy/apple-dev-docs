# markupEditViewController(_:insertNewShape:)

**Framework**: PaperKit  
**Kind**: method  
**Required**: Yes

Add a new shape on top of the paper.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- visionOS 26.0+

## Declaration

```swift
func markupEditViewController(_ markupEditViewController: MarkupEditViewController, insertNewShape type: ShapeConfiguration.Shape)
```

## Parameters

- `markupEditViewController`: The source of the action.
- `type`: The type of shape.

## See Also

- [func markupEditViewControllerInsertNewTextbox(MarkupEditViewController)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontrollerinsertnewtextbox(_:).md)
  Add a new textbox on top of the paper.
- [func markupEditViewController(MarkupEditViewController, insertNewLineWithStartMarker: Bool, endMarker: Bool)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewlinewithstartmarker:endmarker:).md)
  Add a new line on top of the paper.
- [func markupEditViewController(MarkupEditViewController, insertNewContents: PaperMarkup)](markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewcontents:).md)
  Add new content on top of the paper.


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller/delegate-swift.protocol/markupeditviewcontroller(_:insertnewshape:))*