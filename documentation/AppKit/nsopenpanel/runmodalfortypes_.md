# runModalForTypes:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`runModal()`](../nssavepanel/runmodal%28%29.md) instead. You can set `fileTypes` using [`allowedFileTypes`](../nssavepanel/allowedfiletypes.md).

## Declaration

```objc
- (NSInteger) runModalForTypes:(NSArray *) fileTypes;
```

#### Return Value

The button used to dismiss the dialog: `NSOKButton` for the OK button and `NSCancelButton` for the Cancel button.

#### Discussion

This convenience method sends `runModalForDirectory:nil file:nil types:``fileTypes` to the panel. See [`runModalForDirectory:file:types:`](./runmodalfordirectory_file_types_.md) for additional details.

## Parameters

- `fileTypes`: An array of file extensions and/or HFS file types. Specifies the files the panel allows the user to select. `nil` makes all files selectable by the user. An array of types passed in here will override one set using [`allowedFileTypes`](../nssavepanel/allowedfiletypes.md).

## See Also

### Related Documentation
- [func runModal() -> NSApplication.ModalResponse](../nssavepanel/runmodal%28%29.md)
  Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.
### Deprecated methods
- [- filenames](./filenames.md)
  Returns an array containing the absolute paths (as NSString objects) of the selected files and directories.
- [- beginForDirectory:file:types:modelessDelegate:didEndSelector:contextInfo:](./beginfordirectory_file_types_modelessdelegate_didendselector_contextinfo_.md)
  Presents a modeless Open panel.
- [- beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:](./beginsheetfordirectory_file_types_modalforwindow_modaldelegate_didendselector_contextinfo_.md)
  Presents an Open panel as a sheet with the directory specified by `absoluteDirectoryPath` and optionally the file specified by `filename` selected.
- [- runModalForDirectory:file:types:](./runmodalfordirectory_file_types_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/runmodalfortypes:)*