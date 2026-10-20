# fileDialogBrowserOptions(_:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileDialogBrowserOptions(_ options: FileDialogBrowserOptions) -> some View
```

## Parameters

- `options`: The search options to apply to a given file dialog.

## See Also

### Configuring a file dialog
- [func fileDialogConfirmationLabel(_:)](./filedialogconfirmationlabel%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](./filedialogcustomizationid%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](./filedialogdefaultdirectory%28_%29.md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](./filedialogimportsunresolvedaliases%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(_:)](./filedialogmessage%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](./filedialogurlenabled%28_%29.md)
  On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [struct FileDialogBrowserOptions](../filedialogbrowseroptions.md)
  The way that file dialogs present the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/filedialogbrowseroptions(_:))*