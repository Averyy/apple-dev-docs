# FileDialogBrowserOptions

**Framework**: SwiftUI  
**Kind**: struct

The way that file dialogs present the file system.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
struct FileDialogBrowserOptions
```

#### Overview

Apply the options using the [`fileDialogBrowserOptions(_:)`](view/filedialogbrowseroptions(_:).md) modifier.

## Topics

### Getting browser options
- [static let displayFileExtensions: FileDialogBrowserOptions](filedialogbrowseroptions/displayfileextensions.md)
  On iOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to show or hide file extensions. Default behavior is to hide them. On macOS, this option has no effect.
- [static let enumeratePackages: FileDialogBrowserOptions](filedialogbrowseroptions/enumeratepackages.md)
  Allows enumerating packages contents in contrast to the default behavior when packages are represented flatly, similar to files.
- [static let includeHiddenFiles: FileDialogBrowserOptions](filedialogbrowseroptions/includehiddenfiles.md)
  Displays the files that are hidden by default.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](view/filedialogbrowseroptions(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(_:)](view/filedialogconfirmationlabel(_:).md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with custom text as a confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](view/filedialogcustomizationid(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](view/filedialogdefaultdirectory(_:).md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](view/filedialogimportsunresolvedaliases(_:).md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(_:)](view/filedialogmessage(_:).md)
  On macOS, configures the the `fileExporter`, `fileImporter`, or `fileMover` with a custom text that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](view/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/filedialogbrowseroptions)*