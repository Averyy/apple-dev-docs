# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func activate(ignoringOtherApps: Bool)](./nsapplication/activate%28ignoringotherapps%29.md)
  Makes the receiver the active app.
- [func endModalSession(NSApplication.ModalSession)](./nsapplication/endmodalsession%28_%29.md)
  Finishes a modal session.
- [func beginSheet(NSWindow, modalFor: NSWindow, modalDelegate: Any?, didEnd: Selector?, contextInfo: UnsafeMutableRawPointer!)](./nsapplication/beginsheet%28_,modalfor,modaldelegate,didend,contextinfo%29.md)
  Starts a document modal session.
- [func endSheet(NSWindow)](./nsapplication/endsheet%28_%29.md)
  Ends a document modal session by specifying the sheet window.
- [func endSheet(NSWindow, returnCode: Int)](./nsapplication/endsheet%28_,returncode%29.md)
  Ends a document modal session by specifying the sheet window.
- [- beginModalSessionForWindow:relativeToWindow:](./nsapplication/beginmodalsessionforwindow_relativetowindow_.md)
- [- runModalForWindow:relativeToWindow:](./nsapplication/runmodalforwindow_relativetowindow_.md)
- [- application:printFiles:](./nsapplication/application_printfiles_.md)
  Use the delegate method [`application:printFiles:withSettings:showPrintPanels:`](./nsapplicationdelegate/application%28_,printfiles,withsettings,showprintpanels%29.md) instead.
- [- application:delegateHandlesKey:](../ObjectiveC/nsobject-swift.class/application_delegatehandleskey_.md)
  Sent by Cocoa’s built-in scripting support during execution of `get` or `set` script commands to find out if the delegate can handle operations on the specified key-value key.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsapplication-deprecated-symbols)*