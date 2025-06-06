# NSSavePanel

**Framework**: AppKit  
**Kind**: class

A panel that prompts the user for information about where to save a file.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
class NSSavePanel
```

#### Overview

The Save panel provides an interface for specifying the location to save a file and the name of that file. You present this panel when the user attempts to save a new document, or when the user saves a copy of an existing document to a new location. The panel includes UI for browsing the file system, selecting a directory, and specifying the new name for the file. You can also add custom UI for your app using an accessory view.

An [`NSSavePanel`](nssavepanel.md) object reports user interactions to its associated [`delegate`](nssavepanel/delegate.md) object, which must adopt the [`NSOpenSavePanelDelegate`](nsopensavepaneldelegate.md) protocol. Use your delegate object to validate the user’s selection and respond to user interactions with the panel.

In macOS 10.15, the system always displays the Save dialog in a separate process, regardless of whether the app is sandboxed. When the user saves the document, macOS adds the saved file to the app’s sandbox (if necessary) so that the app can write to the file. Prior to macOS 10.15, the system used a separate process only for sandboxed apps.

## Topics

### Responding to User Interactions
- [var delegate: (any NSOpenSavePanelDelegate)?](nssavepanel/delegate.md)
  A custom object you use to manage interactions with an open or save panel.
- [protocol NSOpenSavePanelDelegate](nsopensavepaneldelegate.md)
  A set of methods for managing interactions with an open or save panel.
### Showing the Panel
- [func beginSheetModal(for: NSWindow, completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/beginsheetmodal(for:completionhandler:).md)
  Presents the panel as a sheet modal to the specified window.
- [func begin(completionHandler: (NSApplication.ModalResponse) -> Void)](nssavepanel/begin(completionhandler:).md)
  Presents the panel as a modeless window.
- [func runModal() -> NSApplication.ModalResponse](nssavepanel/runmodal.md)
  Displays the panel and begins its event loop with the current working (or last-selected) directory as the default starting point.
- [func validateVisibleColumns()](nssavepanel/validatevisiblecolumns.md)
  Validates and reloads the browser columns visible in the panel.
### Getting the Selected Item
- [var url: URL?](nssavepanel/url.md)
  A URL that contains the fully specified location of the targeted file.
### Configuring the Panel’s Appearance
- [var title: String!](nssavepanel/title.md)
  The title of the panel.
- [var prompt: String!](nssavepanel/prompt.md)
  The text to display in the default button.
- [var message: String!](nssavepanel/message.md)
  The message text displayed in the panel.
- [var nameFieldLabel: String!](nssavepanel/namefieldlabel.md)
  The label text displayed in front of the filename text field.
- [var nameFieldStringValue: String](nssavepanel/namefieldstringvalue.md)
  The user-editable filename currently shown in the name field.
- [var directoryURL: URL?](nssavepanel/directoryurl.md)
  The current directory shown in the panel.
- [var accessoryView: NSView?](nssavepanel/accessoryview.md)
  The custom accessory view for the current app.
- [var showsTagField: Bool](nssavepanel/showstagfield.md)
  A Boolean value that indicates whether the panel displays the Tags field.
- [var tagNames: [String]?](nssavepanel/tagnames.md)
  The tag names that you want to include on a saved file.
### Configuring the Panel’s Behavior
- [var canCreateDirectories: Bool](nssavepanel/cancreatedirectories.md)
  A Boolean value that indicates whether the panel displays UI for creating directories.
- [var canSelectHiddenExtension: Bool](nssavepanel/canselecthiddenextension.md)
  A Boolean value that indicates whether the panel displays UI for hiding or showing filename extensions.
- [var showsHiddenFiles: Bool](nssavepanel/showshiddenfiles.md)
  A Boolean value that indicates whether the panel displays files that are normally hidden from the user.
- [var isExtensionHidden: Bool](nssavepanel/isextensionhidden.md)
  A Boolean value that indicates whether to display filename extensions.
- [var isExpanded: Bool](nssavepanel/isexpanded.md)
  A Boolean value that indicates whether whether the panel is expanded.
- [Button tags](button-tags.md)
  Button tags that refer to items on the panel.
### Configuring the File Types
- [var allowedContentTypes: [UTType]](nssavepanel/allowedcontenttypes.md)
  An array of types that specify the files types to which you can save.
- [var allowsOtherFileTypes: Bool](nssavepanel/allowsotherfiletypes.md)
  A Boolean value that indicates whether the panel allows the user to save files with a filename extension that’s not in the list of allowed types.
- [var treatsFilePackagesAsDirectories: Bool](nssavepanel/treatsfilepackagesasdirectories.md)
  A Boolean value that indicates whether the panel displays file packages as directories.
### Handling Actions
- [func ok(Any?)](nssavepanel/ok(_:).md)
  The action method that the panel calls when the user clicks the OK button.
- [func cancel(Any?)](nssavepanel/cancel(_:).md)
  The action method that the panel calls when the user clicks the Cancel button.
### Deprecated
- [Deprecated Symbols](nssavepanel-deprecated-symbols.md)
  Review unsupported symbols and their replacements.
### Instance Properties
- [var identifier: NSUserInterfaceItemIdentifier?](nssavepanel/identifier.md)
- [var currentContentType: UTType?](nssavepanel/currentcontenttype.md)
  `NSSavePanel`:The current type. If set to `nil`, resets to the first allowed content type. Returns `nil` if `allowedContentTypes` is empty. `NSOpenPanel`: Not used.
- [var showsContentTypes: Bool](nssavepanel/showscontenttypes.md)
  `NSSavePanel`: Whether or not to show a control for selecting the type of the saved file. The control shows the types in `allowedContentTypes`. Default is `NO`.

## Relationships

### Inherits From
- [NSPanel](nspanel.md)
### Inherited By
- [NSOpenPanel](nsopenpanel.md)
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

- [class NSOpenPanel](nsopenpanel.md)
  A panel that prompts the user to select a file to open.
- [protocol NSOpenSavePanelDelegate](nsopensavepaneldelegate.md)
  A set of methods for managing interactions with an open or save panel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nssavepanel)*