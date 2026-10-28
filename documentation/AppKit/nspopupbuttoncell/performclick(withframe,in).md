# performClick(withFrame:in:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the receiver’s menu and track mouse events in it.

**Availability**:
- macOS

## Declaration

```swift
func performClick(withFrame frame: NSRect, in controlView: NSView)
```

```objc
- (void) performClickWithFrame:(NSRect) frame inView:(NSView *) controlView;
```

## Discussion

You normally do not call this method explicitly. It is called by the Application Kit automatically to handle events in the pop-up button.

## Parameters

- `frame`: The cell’s rectangle, specified in points in the coordinate system of the view in the `controlView` parameter.
- `controlView`: The view in which to display the pop-up button’s menu.

## See Also

### Handling events and action messages
- [func attachPopUp(withFrame: NSRect, in: NSView)](./attachpopup%28withframe,in%29.md)
  Sets up the receiver to display a menu.
- [func dismissPopUp()](./dismisspopup%28%29.md)
  Dismisses the pop-up button’s menu by ordering its window out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nspopupbuttoncell/performclick(withframe:in:))*