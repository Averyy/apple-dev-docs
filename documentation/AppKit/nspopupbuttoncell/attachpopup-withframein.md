# attachPopUp(withFrame:in:)

**Framework**: AppKit  
**Kind**: method

Sets up the receiver to display a menu.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func attachPopUp(withFrame cellFrame: NSRect, in controlView: NSView)
```

#### Discussion

This call sets up the popup button cell to display a menu, which occurs in [`performClick(withFrame:in:)`](nspopupbuttoncell/performclick(withframe:in:).md). This method sets the cell’s control view and then highlights and redraws the cell. It does not show the menu.

This method also posts an [`willPopUpNotification`](nspopupbuttoncell/willpopupnotification.md). (The `NSPopUpButton` object sends a corresponding [`willPopUpNotification`](nspopupbutton/willpopupnotification.md).)

You normally do not call this method explicitly. It is called by the Application Kit automatically when the menu for the pop-up button is to be displayed.

## Parameters

- `cellFrame`: The cell’s rectangle, specified in points in the coordinate system of the view in the   parameter. The menu is attached to this rectangle.
- `controlView`: The view in which to display the pop-up button’s menu.

## See Also

- [func dismissPopUp()](nspopupbuttoncell/dismisspopup.md)
  Dismisses the pop-up button’s menu by ordering its window out.
- [func performClick(withFrame: NSRect, in: NSView)](nspopupbuttoncell/performclick(withframe:in:).md)
  Displays the receiver’s menu and track mouse events in it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/attachpopup(withframe:in:))*