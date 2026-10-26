# accessoryView

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the accessory view of the Print panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.5

> **Deprecated**: Use [`accessoryControllers`](./accessorycontrollers.md) instead.

## Declaration

```objc
- (NSView *) accessoryView;
```

#### Return Value

The accessory view of the receiver, if any.

## See Also

### Deprecated
- [- setAccessoryView:](./setaccessoryview_.md)
  Sets the accessory view for the Print panel.
- [- updateFromPrintInfo](./updatefromprintinfo.md)
  Updates the Print panel with information from the current print operation object.
- [- finalWritePrintInfo](./finalwriteprintinfo.md)
  Writes the Print panel’s printing attributes to the current print operation object.
- [func beginSheet(with: NSPrintInfo, modalFor: NSWindow, delegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer?)](./beginsheet%28with,modalfor,delegate,didend,contextinfo%29.md)
  Displays a Print panel sheet and runs it modally for the specified window.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsprintpanel/accessoryview)*