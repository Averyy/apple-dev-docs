# dismissPopUp()

**Framework**: AppKit  
**Kind**: method

Dismisses the pop-up button’s menu by ordering its window out.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
func dismissPopUp()
```

#### Discussion

If the pop-up button was not displaying its menu, this method does nothing.

You normally do not call this method explicitly. It is called by the Application Kit automatically to dismiss the menu for the pop-up button.

## See Also

- [func orderOut(Any?)](nswindow/orderout(_:).md)
  Removes the window from the screen list, which hides the window.
- [func attachPopUp(withFrame: NSRect, in: NSView)](nspopupbuttoncell/attachpopup(withframe:in:).md)
  Sets up the receiver to display a menu.
- [func performClick(withFrame: NSRect, in: NSView)](nspopupbuttoncell/performclick(withframe:in:).md)
  Displays the receiver’s menu and track mouse events in it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/dismisspopup())*