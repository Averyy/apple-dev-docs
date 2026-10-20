# MarkupEditViewController.Delegate

**Framework**: PaperKit  
**Kind**: protocol  
**Role**: Protocol

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- visionOS 26.0+

## Declaration

```swift
protocol Delegate : AnyObject
```

## Topics

### Inserting content
- [func markupEditViewController(MarkupEditViewController, insertNewShape: ShapeConfiguration.Shape)](./delegate-swift.protocol/markupeditviewcontroller%28_,insertnewshape%29.md)
  Add a new shape on top of the paper.
- [func markupEditViewControllerInsertNewTextbox(MarkupEditViewController)](./delegate-swift.protocol/markupeditviewcontrollerinsertnewtextbox%28_%29.md)
  Add a new textbox on top of the paper.
- [func markupEditViewController(MarkupEditViewController, insertNewLineWithStartMarker: Bool, endMarker: Bool)](./delegate-swift.protocol/markupeditviewcontroller%28_,insertnewlinewithstartmarker,endmarker%29.md)
  Add a new line on top of the paper.
- [func markupEditViewController(MarkupEditViewController, insertNewContents: PaperMarkup)](./delegate-swift.protocol/markupeditviewcontroller%28_,insertnewcontents%29.md)
  Add new content on top of the paper.

## Relationships

### Conforming Types
- [PaperMarkupViewController](../papermarkupviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markupeditviewcontroller/delegate-swift.protocol)*