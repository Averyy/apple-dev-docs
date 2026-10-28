# directory

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the absolute pathname of the directory currently shown in the panel.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`directoryURL`](./directoryurl.md) instead.

## Declaration

```objc
- (NSString *) directory;
```

## Return Value

The absolute pathname of the directory currently shown in the panel.

## See Also

### Related Documentation
- [var directoryURL: URL?](./directoryurl.md)
  The current directory shown in the panel.
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
- [- filename](./filename.md)
  Returns the absolute pathname of the file currently shown in the panel.
- [- selectText:](./selecttext_.md)
  This method has been deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/directory)*