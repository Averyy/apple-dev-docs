# requiredFileType

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the required file type (if any).

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`allowedFileTypes`](./allowedfiletypes.md) instead.

## Declaration

```objc
- (NSString *) requiredFileType;
```

## Return Value

The required file type (if any).

## Discussion

A file specified in the Save panel is saved with the designated filename and this file type as an extension. Examples of common file types are “rtf”, “tiff”, and “ps”. File type strings encoding HFS file types are not valid values for this attribute. An `nil` return value indicates that the user can save to any ASCII file.

This method is equivalent to using [`allowedFileTypes`](./allowedfiletypes.md) and returning the first element of the list of allowed types, or `nil` if there are none.

## See Also

### Deprecated methods
- [var allowedFileTypes: [String]?](./allowedfiletypes.md)
  An array of filename extensions or UTIs that represent the allowed file types for the panel.
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
- [- directory](./directory.md)
  Returns the absolute pathname of the directory currently shown in the panel.
- [- filename](./filename.md)
  Returns the absolute pathname of the file currently shown in the panel.
- [- selectText:](./selecttext_.md)
  This method has been deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/requiredfiletype)*