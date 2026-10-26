# beginSheetForDirectory:file:modalForWindow:modalDelegate:didEndSelector:contextInfo:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents a Save panel as a sheet with a specified path and, optionally, a specified file in that path.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`beginSheetModal(for:completionHandler:)`](./beginsheetmodal%28for,completionhandler%29.md) instead.

## Declaration

```objc
- (void) beginSheetForDirectory:(NSString *) path file:(NSString *) name modalForWindow:(NSWindow *) docWindow modalDelegate:(id) delegate didEndSelector:(SEL) didEndSelector contextInfo:(void *) contextInfo;
```

## Parameters

- `path`: Directory whose files the panel displays. When `nil`, the directory is the same directory used in the previous invocation of the panel; this is probably the best choice for most situations.
- `name`: Specifies a particular file in `path` that is selected when the Save panel is presented to a user. When `nil`, no file is initially selected.
- `docWindow`: If not `nil`, the Save panel slides down as a sheet running as a document modal window in `docWindow`. If `nil`, the behavior defaults to a standalone modal window.
- `delegate`: This is not the same as a delegate assigned to the panel. This delegate is temporary and the relationship only lasts until the panel is dismissed. The `NSSavePanel` object has a weak reference to the modal delegate.
- `didEndSelector`: Message sent to `modalDelegate` after the modal session has ended, but before dismissing the Save panel. `didEndSelector` may dismiss the Save panel itself; otherwise, it is dismissed on return from the method. The corresponding method should have the following signature:

  ```objc
  - (void)savePanelDidEnd:(NSSavePanel *)sheet returnCode:(int)returnCode contextInfo:(void *)contextInfo;
  ```

  The value passed as `returnCode` is either `NSCancelButton` or `NSOKButton`.
- `contextInfo`: Context information passed to `modalDelegate` in the `didEndSelector` message.

## See Also

### Related Documentation
- [func beginSheetModal(for: NSWindow, completionHandler: (NSApplication.ModalResponse) -> Void)](./beginsheetmodal%28for,completionhandler%29.md)
  Presents the panel as a sheet modal to the specified window.
### Deprecated methods
- [var allowedFileTypes: [String]?](./allowedfiletypes.md)
  An array of filename extensions or UTIs that represent the allowed file types for the panel.
- [- requiredFileType](./requiredfiletype.md)
  Returns the required file type (if any).
- [- setRequiredFileType:](./setrequiredfiletype_.md)
  Specifies the file type (as an extension) or a UTI.
- [- setDirectory:](./setdirectory_.md)
  Sets the current pathname in the panel’s browser.
- [- runModalForDirectory:file:](./runmodalfordirectory_file_.md)
  Initializes the panel to the directory and file specified, if any, then displays it and begins its modal event loop.
- [- panel:compareFilename:with:caseSensitive:](../../ObjectiveC/nsobject-swift.class/panel_comparefilename_with_casesensitive_.md)
  Controls the ordering of files presented by the `NSSavePanel` object specified.
- [- panel:isValidFilename:](../../ObjectiveC/nsobject-swift.class/panel_isvalidfilename_.md)
  Gives the delegate the opportunity to validate selected items.
- [- panel:shouldShowFilename:](../../ObjectiveC/nsobject-swift.class/panel_shouldshowfilename_.md)
  Gives the delegate the opportunity to filter items that it doesn’t want the user to choose.
- [- panel:directoryDidChange:](../../ObjectiveC/nsobject-swift.class/panel_directorydidchange_.md)
  Tells the delegate that the user has changed the selected directory in the `NSSavePanel` object specified.
- [- directory](./directory.md)
  Returns the absolute pathname of the directory currently shown in the panel.
- [- filename](./filename.md)
  Returns the absolute pathname of the file currently shown in the panel.
- [- selectText:](./selecttext_.md)
  This method has been deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/beginsheetfordirectory:file:modalforwindow:modaldelegate:didendselector:contextinfo:)*