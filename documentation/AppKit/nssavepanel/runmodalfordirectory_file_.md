# runModalForDirectory:file:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Initializes the panel to the directory and file specified, if any, then displays it and begins its modal event loop.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`runModal()`](./runmodal%28%29.md) instead.

## Declaration

```objc
- (NSInteger) runModalForDirectory:(NSString *) path file:(NSString *) name;
```

#### Return Value

`NSFileHandlingPanelOKButton` (if the user clicks the OK button) or `NSFileHandlingPanelCancelButton` (if the user clicks the Cancel button).

#### Discussion

This method invokes `NSApplication`’s [`runModal(for:)`](../nsapplication/runmodal%28for%29.md) method with `self` as the argument.

## Parameters

- `path`: Directory whose files the panel displays. When `nil`, the directory is the same directory used in the previous invocation of the panel; this is probably the best choice for most situations.
- `name`: Specifies a particular file in `path` that is selected when the Save panel is presented to a user. When `nil`, no file is initially selected.

## See Also

### Related Documentation
- [func runModal(for: NSWindow) -> NSApplication.ModalResponse](../nsapplication/runmodal%28for%29.md)
  Starts a modal event loop for the specified window.
- [func runModal() -> NSApplication.ModalResponse](./runmodal%28%29.md)
  Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.
### Deprecated methods
- [var allowedFileTypes: [String]?](./allowedfiletypes.md)
  An array of filename extensions or UTIs that represent the allowed file types for the panel.
- [- requiredFileType](./requiredfiletype.md)
  Returns the required file type (if any).
- [- setRequiredFileType:](./setrequiredfiletype_.md)
  Specifies the file type (as an extension) or a UTI.
- [- setDirectory:](./setdirectory_.md)
  Sets the current pathname in the panel’s browser.
- [- beginSheetForDirectory:file:modalForWindow:modalDelegate:didEndSelector:contextInfo:](./beginsheetfordirectory_file_modalforwindow_modaldelegate_didendselector_contextinfo_.md)
  Presents a Save panel as a sheet with a specified path and, optionally, a specified file in that path.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/runmodalfordirectory:file:)*