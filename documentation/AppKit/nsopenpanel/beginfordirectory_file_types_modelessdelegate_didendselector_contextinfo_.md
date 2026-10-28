# beginForDirectory:file:types:modelessDelegate:didEndSelector:contextInfo:

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Presents a modeless Open panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`begin(completionHandler:)`](../nssavepanel/begin%28completionhandler%29.md) instead. You can set `absoluteDirectoryPath` using [`directoryURL`](../nssavepanel/directoryurl.md), and you can set `fileTypes` using [`allowedFileTypes`](../nssavepanel/allowedfiletypes.md).

## Declaration

```objc
- (void) beginForDirectory:(NSString *) path file:(NSString *) name types:(NSArray *) fileTypes modelessDelegate:(id) delegate didEndSelector:(SEL) didEndSelector contextInfo:(void *) contextInfo;
```

## Discussion

Similar to [`beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:`](./beginsheetfordirectory_file_types_modalforwindow_modaldelegate_didendselector_contextinfo_.md), but allows for modeless operation of the panel.

## Parameters

- `path`: The directory whose files the panel displays. When `nil`, the directory is the same directory used in the previous invocation of the panel; this is probably the best choice for most situations.
- `name`: Specifies a particular file in `absoluteDirectoryPath` that is selected when the Open panel is presented to the user. When `nil`, no file is initially selected.
- `fileTypes`: An array of file extensions and/or HFS file types. Specifies the files the panel allows the user to select. `nil` makes all files in `absoluteDirectoryPath` selectable by the user. An array of types passed in here will override one set using [`allowedFileTypes`](../nssavepanel/allowedfiletypes.md).
- `delegate`: This is not the same as a delegate assigned to the panel. This delegate is temporary and the relationship only lasts until the panel is dismissed.
- `didEndSelector`: The message sent to `modelessDelegate` after the panel’s session has ended, but before dismissing the Open panel. `didEndSelector` may dismiss the Open panel itself; otherwise, it will be dismissed on return from the method. The corresponding method should have the following signature:

  ```objc
  - (void)openPanelDidEnd:(NSOpenPanel *)panel returnCode:(int)returnCode  contextInfo:(void  *)contextInfo
  ```

  The value passed as `returnCode` will be either `NSCancelButton` or `NSOKButton`.
- `contextInfo`: Any context information passed to `modelessDelegate` in the `didEndSelector` message.

## See Also

### Related Documentation
- [func begin(completionHandler: (NSApplication.ModalResponse) -> Void)](../nssavepanel/begin%28completionhandler%29.md)
  Presents the panel as a modeless window.
### Deprecated methods
- [- filenames](./filenames.md)
  Returns an array containing the absolute paths (as NSString objects) of the selected files and directories.
- [- beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:](./beginsheetfordirectory_file_types_modalforwindow_modaldelegate_didendselector_contextinfo_.md)
  Presents an Open panel as a sheet with the directory specified by `absoluteDirectoryPath` and optionally the file specified by `filename` selected.
- [- runModalForDirectory:file:types:](./runmodalfordirectory_file_types_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.
- [- runModalForTypes:](./runmodalfortypes_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/beginfordirectory:file:types:modelessdelegate:didendselector:contextinfo:)*