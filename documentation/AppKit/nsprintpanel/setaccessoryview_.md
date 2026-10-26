# setAccessoryView:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the accessory view for the Print panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`addAccessoryController(_:)`](./addaccessorycontroller%28_%29.md) instead.

## Declaration

```objc
- (void) setAccessoryView:(NSView *) accessoryView;
```

#### Discussion

You can use an accessory view to add printing controls and information to the standard print panel. You set your accessory view prior to displaying the print panel. Upon display, the print panel adds your application’s name as an item to its pane-selection pull-down menu. When the user selects this item, the print panel displays your accessory view.

## Parameters

- `accessoryView`: The view containing the controls and information you want to add to the print panel. Specify `nil` to remove the receiver’s current accessory view.

## See Also

### Deprecated
- [- accessoryView](./accessoryview.md)
  Returns the accessory view of the Print panel.
- [- updateFromPrintInfo](./updatefromprintinfo.md)
  Updates the Print panel with information from the current print operation object.
- [- finalWritePrintInfo](./finalwriteprintinfo.md)
  Writes the Print panel’s printing attributes to the current print operation object.
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md)
  Displays a Print panel sheet and runs it modally for the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/setaccessoryview:)*