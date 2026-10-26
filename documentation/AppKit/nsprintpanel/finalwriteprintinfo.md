# finalWritePrintInfo

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Writes the Print panel’s printing attributes to the current print operation object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

## Declaration

```objc
- (void) finalWritePrintInfo;
```

#### Discussion

Do not invoke this method directly—it is invoked automatically when the Print panel is dismissed by the user clicking the OK button.

## See Also

### Related Documentation
- [class var current: NSPrintOperation?](../nsprintoperation/current.md)
  The current print operation for this thread.
### Deprecated
- [- accessoryView](./accessoryview.md)
  Returns the accessory view of the Print panel.
- [- setAccessoryView:](./setaccessoryview_.md)
  Sets the accessory view for the Print panel.
- [- updateFromPrintInfo](./updatefromprintinfo.md)
  Updates the Print panel with information from the current print operation object.
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md)
  Displays a Print panel sheet and runs it modally for the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/finalwriteprintinfo)*