# dismissPopUp()

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Dismisses the pop-up button’s menu by ordering its window out.

**Availability**:
- macOS

## Declaration

```swift
func dismissPopUp()
```

```objc
- (void) dismissPopUp;
```

#### Discussion

If the pop-up button was not displaying its menu, this method does nothing.

You normally do not call this method explicitly. It is called by the Application Kit automatically to dismiss the menu for the pop-up button.

## See Also

### Related Documentation
- [func orderOut(Any?)](../nswindow/orderout%28_%29.md)
  Removes the window from the screen list, which hides the window.
### Handling events and action messages
- [func attachPopUp(withFrame: NSRect, in: NSView)](./attachpopup%28withframe,in%29.md)
  Sets up the receiver to display a menu.
- [func performClick(withFrame: NSRect, in: NSView)](./performclick%28withframe,in%29.md)
  Displays the receiver’s menu and track mouse events in it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/dismisspopup())*