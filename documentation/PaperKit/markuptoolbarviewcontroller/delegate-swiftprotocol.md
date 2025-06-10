# MarkupToolbarViewController.Delegate

**Framework**: PaperKit  
**Kind**: protocol

The delegate for a PaperKit toolbar.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
protocol Delegate : AnyObject
```

## Topics

### Instance Methods
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewContents: PaperMarkup)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewcontents:).md)
  Add new content on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewLineWithStartMarker: Bool, endMarker: Bool)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewlinewithstartmarker:endmarker:).md)
  Add a new line on top of the paper.
- [func markupToolbarViewController(MarkupToolbarViewController, insertNewShape: ShapeConfiguration.Shape)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontroller(_:insertnewshape:).md)
  Add a new shape on top of the paper.
- [func markupToolbarViewControllerInsertNewTextbox(MarkupToolbarViewController)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontrollerinsertnewtextbox(_:).md)
  Add a new textbox on top of the paper.
- [func markupToolbarViewControllerSelectedDrawingToolChanged(MarkupToolbarViewController)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontrollerselecteddrawingtoolchanged(_:).md)
  Called when the `selectedDrawingTool` changes.
- [func markupToolbarViewControllerSelectedIndirectPointerTouchModeChanged(MarkupToolbarViewController)](markuptoolbarviewcontroller/delegate-swift.protocol/markuptoolbarviewcontrollerselectedindirectpointertouchmodechanged(_:).md)
  Called when the `selectedIndirectPointerTouchMode` changes.

## Relationships

### Conforming Types
- [PaperMarkupViewController](papermarkupviewcontroller.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/paperkit/markuptoolbarviewcontroller/delegate-swift.protocol)*