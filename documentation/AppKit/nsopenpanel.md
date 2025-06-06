# NSOpenPanel

**Framework**: AppKit  
**Kind**: class

A panel that prompts the user to select a file to open.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSOpenPanel
```

#### Overview

Apps use the Open panel as a convenient way to query the user for the name of a file to open. In macOS 10.15 and later, the system always draws Open panels in a separate process, regardless of whether the app is sandboxed. When the user chooses a file to open, macOS adds that file to the app’s sandbox. Prior to macOS 10.15, the system drew the panels in a separate process only for sandboxed apps.

## Topics

### Configuring the Open Panel
- [var canChooseFiles: Bool](nsopenpanel/canchoosefiles.md)
  A Boolean that indicates whether the user can choose files in the panel.
- [var canChooseDirectories: Bool](nsopenpanel/canchoosedirectories.md)
  A Boolean that indicates whether the user can choose directories in the panel.
- [var resolvesAliases: Bool](nsopenpanel/resolvesaliases.md)
  A Boolean that indicates whether the panel resolves aliases.
- [var allowsMultipleSelection: Bool](nsopenpanel/allowsmultipleselection.md)
  A Boolean that indicates whether the user may select multiple files and directories.
- [var isAccessoryViewDisclosed: Bool](nsopenpanel/isaccessoryviewdisclosed.md)
  A Boolean value that indicates whether the panel’s accessory view is visible.
### Accessing User Selection
- [var urls: [URL]](nsopenpanel/urls.md)
  An array of URLs, each of which contains the fully specified location of a selected file or directory.
### Supporting iCloud Documents
- [var canDownloadUbiquitousContents: Bool](nsopenpanel/candownloadubiquitouscontents.md)
  A Boolean value that indicates how the panel responds to iCloud documents that aren’t fully downloaded locally.
- [var canResolveUbiquitousConflicts: Bool](nsopenpanel/canresolveubiquitousconflicts.md)
  A Boolean value that indicates how the panel responds to iCloud documents that have conflicting versions.
### Deprecated
- [Deprecated Symbols](nsopenpanel-deprecated-symbols.md)
  Review symbols that are no longer supported, and find the replacements to use instead.

## Relationships

### Inherits From
- [NSSavePanel](nssavepanel.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](nsappearancecustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSMenuItemValidation](nsmenuitemvalidation.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](nstouchbarprovider.md)
- [NSUserActivityRestoring](nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](nsuserinterfacevalidations.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class NSSavePanel](nssavepanel.md)
  A panel that prompts the user for information about where to save a file.
- [protocol NSOpenSavePanelDelegate](nsopensavepaneldelegate.md)
  A set of methods for managing interactions with an open or save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsopenpanel)*