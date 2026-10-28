# application:printFiles:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Use the delegate method [`application(_:printFiles:withSettings:showPrintPanels:)`](../nsapplicationdelegate/application%28_,printfiles,withsettings,showprintpanels%29.md) instead.

**Availability**:
- macOS 10.3+ - Deprecated in 10.4

## Declaration

```objc
- (void) application:(NSApplication *) sender printFiles:(NSArray<NSString *> *) filenames;
```

## Discussion

Identical to [`application(_:printFile:)`](../nsapplicationdelegate/application%28_,printfile%29.md) except that the receiver prints multiple files corresponding to the file names in the `filenames` array.

Delegates should invoke the [`reply(toOpenOrPrint:)`](./reply%28toopenorprint%29.md) method upon success or failure, or when the user cancels the operation.

## Parameters

- `sender`: Requests application to print file.
- `filenames`: The name of the file to print.

## See Also

### Deprecated methods
- [func activate(ignoringOtherApps: Bool)](./activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
- [- beginModalSessionForWindow:relativeToWindow:](./beginmodalsessionforwindow_relativetowindow_.md)
- [- runModalForWindow:relativeToWindow:](./runmodalforwindow_relativetowindow_.md)
- [func endModalSession(NSApplication.ModalSession)](./endmodalsession%28_%29.md)
  Finishes a modal session.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](./beginsheet%28_,modalfor,modaldelegate,didend,contextinfo%29.md)
  Starts a document modal session.
- [func endSheet(NSWindow)](./endsheet%28_%29.md)
  Ends a document modal session by specifying the sheet window.
- [func endSheet(NSWindow, returnCode: Int)](./endsheet%28_,returncode%29.md)
  Ends a document modal session by specifying the sheet window.
- [- application:delegateHandlesKey:](../../ObjectiveC/nsobject-swift.class/application_delegatehandleskey_.md)
  Sent by Cocoa’s built-in scripting support during execution of `get` or `set` script commands to find out if the delegate can handle operations on the specified key-value key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication/application:printfiles:)*