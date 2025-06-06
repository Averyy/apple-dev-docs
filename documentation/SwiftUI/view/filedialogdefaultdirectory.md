# fileDialogDefaultDirectory(_:)

**Framework**: SwiftUI  
**Kind**: method

Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func fileDialogDefaultDirectory(_ defaultDirectory: URL?) -> some View
```

## Parameters

- `defaultDirectory`: The directory to show when   the system file dialog launches. If the given file dialog has   a   if stores the user-chosen directory and subsequently   opens with it, ignoring the default value provided in this modifier.

## See Also

- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](view/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(_:)](view/filedialogconfirmationlabel(_:).md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with custom text as a confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](view/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](view/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(_:)](view/filedialogmessage(_:).md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](view/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [struct FileDialogBrowserOptions](filedialogbrowseroptions.md)
  The way that file dialogs present the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/filedialogdefaultdirectory(_:))*