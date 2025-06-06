# performClick(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Displays the receiver’s menu and track mouse events in it.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func performClick(withFrame frame: NSRect, in controlView: NSView)
```

#### Discussion

You normally do not call this method explicitly. It is called by the Application Kit automatically to handle events in the pop-up button.

## Parameters

- `frame`: The cell’s rectangle, specified in points in the coordinate system of the view in the   parameter.
- `controlView`: The view in which to display the pop-up button’s menu.

## See Also

- [func attachPopUp(withFrame: NSRect, in: NSView)](nspopupbuttoncell/attachpopup(withframe:in:).md)
  Sets up the receiver to display a menu.
- [func dismissPopUp()](nspopupbuttoncell/dismisspopup.md)
  Dismisses the pop-up button’s menu by ordering its window out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/performclick(withframe:in:))*