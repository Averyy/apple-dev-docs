# filenames

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array containing the absolute paths (as NSString objects) of the selected files and directories.

**Availability**:
- macOS 10.0+ - Deprecated in 10.6

> **Deprecated**: Use [`urls`](./urls.md) instead.

## Declaration

```objc
- (NSArray *) filenames;
```

#### Return Value

The array of filenames.

#### Discussion

If multiple selections aren’t allowed, the array contains a single name. The [`filenames`](./filenames.md) method is preferable over NSSavePanel’s [`filename`](../nssavepanel/filename.md) to get the name or names of files and directories that the user has selected.

## See Also

### Related Documentation
- [var urls: [URL]](./urls.md)
  An array of URLs, each of which contains the fully specified location of a selected file or directory.
### Deprecated methods
- [- beginForDirectory:file:types:modelessDelegate:didEndSelector:contextInfo:](./beginfordirectory_file_types_modelessdelegate_didendselector_contextinfo_.md)
  Presents a modeless Open panel.
- [- beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:](./beginsheetfordirectory_file_types_modalforwindow_modaldelegate_didendselector_contextinfo_.md)
  Presents an Open panel as a sheet with the directory specified by `absoluteDirectoryPath` and optionally the file specified by `filename` selected.
- [- runModalForDirectory:file:types:](./runmodalfordirectory_file_types_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.
- [- runModalForTypes:](./runmodalfortypes_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel/filenames)*