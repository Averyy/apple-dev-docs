# allowedFileTypes

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An array of filename extensions or UTIs that represent the allowed file types for the panel.

**Availability**:
- macOS 10.3+ - Deprecated in 12.0

> **Deprecated**: Use -allowedContentTypes instead

## Declaration

```swift
var allowedFileTypes: [String]? { get set }
```

```objc
@property (copy, nullable) NSArray<NSString *> * allowedFileTypes;
```

## Discussion

Use this property to specify the file types for the user to select from. A file type can be a common filename extension, or a UTI. The default value of this property is `nil`, which indicates that any file type can be used. If you specify an empty array for this parameter, the Save panel raises an exception.

If the user doesn’t select a type, the panel uses the first item in the `allowedFileTypes` array. If [`allowsOtherFileTypes`](./allowsotherfiletypes.md) is [`true`](../../Swift/true.md), and the user enters a filename extension that doesn’t match one of the types in the array, AppKit prompts the user to confirm the choice.

[`NSOpenPanel`](../nsopenpanel.md): In versions of macOS earlier than v10.6, this property is ignored. For applications that link against v10.6 and higher, this property determines which files the open panel enables. Don’t use the deprecated methods to show the open panel (that is, the methods that take a `types:` parameter) because they will overwrite this value. The allowed file types can be changed while the panel is running (for example, from an accessory view). This is also known as the “enabled file types.” A `nil` value indicates that all files should be enabled.

## See Also

### Deprecated methods
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
- [- directory](./directory.md)
  Returns the absolute pathname of the directory currently shown in the panel.
- [- filename](./filename.md)
  Returns the absolute pathname of the file currently shown in the panel.
- [- selectText:](./selecttext_.md)
  This method has been deprecated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel/allowedfiletypes)*