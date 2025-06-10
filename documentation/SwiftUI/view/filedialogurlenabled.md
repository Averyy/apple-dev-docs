# fileDialogURLEnabled(_:)

**Framework**: SwiftUI  
**Kind**: method

On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileDialogURLEnabled(_ predicate: Predicate<URL>) -> some View
```

## Parameters

- `predicate`: The predicate that evaluates the   URLs presented to the user to conditionally disable them.   The implementation is expected to have constant complexity   and should not access the files contents or metadata. A common use case   is inspecting the path or the file name.

## See Also

- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](view/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(_:)](view/filedialogconfirmationlabel(_:).md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](view/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](view/filedialogdefaultdirectory(_:).md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](view/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(_:)](view/filedialogmessage(_:).md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [struct FileDialogBrowserOptions](filedialogbrowseroptions.md)
  The way that file dialogs present the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/filedialogurlenabled(_:))*