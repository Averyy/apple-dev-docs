# MarkupToolbarViewController.Delegate

**Framework**: PaperKit  
**Kind**: protocol  
**Role**: Protocol

The delegate for a PaperKit toolbar.

**Availability**:
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
protocol Delegate : AnyObject
```

## Topics

### Inserting content
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewShape: ShapeConfiguration.Shape)](./delegate-swift.protocol/markuptoolbarviewcontroller%28_,insertnewshape%29.md)
  Add a new shape on top of the paper.
- [func markupToolbarViewControllerInsertNewTextbox(MarkupToolbarViewController)](./delegate-swift.protocol/markuptoolbarviewcontrollerinsertnewtextbox%28_%29.md)
  Add a new textbox on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewLineWithStartMarker: Bool, endMarker: Bool)](./delegate-swift.protocol/markuptoolbarviewcontroller%28_,insertnewlinewithstartmarker,endmarker%29.md)
  Add a new line on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewContents: PaperMarkup)](./delegate-swift.protocol/markuptoolbarviewcontroller%28_,insertnewcontents%29.md)
  Add new content on top of the paper.
### Responding to changes
- [func markupToolbarViewControllerSelectedIndirectPointerTouchModeChanged(MarkupToolbarViewController)](./delegate-swift.protocol/markuptoolbarviewcontrollerselectedindirectpointertouchmodechanged%28_%29.md)
  Called when the `selectedIndirectPointerTouchMode` changes.
- [func markupToolbarViewControllerSelectedDrawingToolChanged(MarkupToolbarViewController)](./delegate-swift.protocol/markuptoolbarviewcontrollerselecteddrawingtoolchanged%28_%29.md)
  Called when the `selectedDrawingTool` changes.

## Relationships

### Conforming Types
- [PaperMarkupViewController](../papermarkupviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.protocol)*