# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

#### Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [- filenames](./nsopenpanel/filenames.md)
  Returns an array containing the absolute paths (as NSString objects) of the selected files and directories.
- [- beginForDirectory:file:types:modelessDelegate:didEndSelector:contextInfo:](./nsopenpanel/beginfordirectory_file_types_modelessdelegate_didendselector_contextinfo_.md)
  Presents a modeless Open panel.
- [- beginSheetForDirectory:file:types:modalForWindow:modalDelegate:didEndSelector:contextInfo:](./nsopenpanel/beginsheetfordirectory_file_types_modalforwindow_modaldelegate_didendselector_contextinfo_.md)
  Presents an Open panel as a sheet with the directory specified by `absoluteDirectoryPath` and optionally the file specified by `filename` selected.
- [- runModalForDirectory:file:types:](./nsopenpanel/runmodalfordirectory_file_types_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.
- [- runModalForTypes:](./nsopenpanel/runmodalfortypes_.md)
  Displays the panel and begins a modal event loop that is terminated when the user clicks either OK or Cancel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel-deprecated-symbols)*