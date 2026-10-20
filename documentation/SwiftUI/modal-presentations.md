# Modal presentations

**Framework**: SwiftUI  
**Role**: API Collection

Present content in a separate view that offers focused interaction.

#### Overview

To draw attention to an important, narrowly scoped task, you display a modal presentation, like an alert, popover, sheet, or confirmation dialog.

![](https://developer.apple.com/tutorials/images/com.apple.SwiftUI/modal-presentations-hero@2x.png)

In SwiftUI, you create a modal presentation using a view modifier that defines how the presentation looks and the condition under which SwiftUI presents it. SwiftUI detects when the condition changes and makes the presentation for you. Because you provide a [`Binding`](./binding.md) to the condition that initiates the presentation, SwiftUI can reset the underlying value when the user dismisses the presentation.

For design guidance, see [Modality](https://developer.apple.com/design/human-interface-guidelines/modality) in the Human Interface Guidelines.

## Topics

### Configuring a dialog
- [struct DialogSeverity](./dialogseverity.md)
  The severity of an alert or confirmation dialog.
### Showing a sheet, cover, or popover
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./view/sheet%28ispresented,ondismiss,content%29.md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./view/sheet%28item,ondismiss,content%29.md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./view/fullscreencover%28ispresented,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./view/fullscreencover%28item,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](./view/popover%28item,attachmentanchor,arrowedge,content%29.md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](./view/popover%28ispresented,attachmentanchor,arrowedge,content%29.md)
  Presents a popover when a given condition is true.
- [enum PopoverAttachmentAnchor](./popoverattachmentanchor.md)
  An attachment anchor for a popover.
### Adapting a presentation size
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](./view/presentationcompactadaptation%28horizontal,vertical%29.md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](./view/presentationcompactadaptation%28_%29.md)
  Specifies how to adapt a presentation to compact size classes.
- [struct PresentationAdaptation](./presentationadaptation.md)
  Strategies for adapting a presentation to a different size class.
- [func presentationSizing(some PresentationSizing) -> some View](./view/presentationsizing%28_%29.md)
  Sets the sizing of the containing presentation.
- [protocol PresentationSizing](./presentationsizing.md)
  A type that defines the size of the presentation content and how the presentation size adjusts to its content’s size changing.
- [struct PresentationSizingRoot](./presentationsizingroot.md)
  A proxy to a view provided to the presentation with a defined presentation size.
- [struct PresentationSizingContext](./presentationsizingcontext.md)
  Contextual information about a presentation.
### Configuring a sheet’s height and placement
- [func presentationDetents(Set<PresentationDetent>) -> some View](./view/presentationdetents%28_%29.md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](./view/presentationdetents%28_,selection%29.md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](./view/presentationcontentinteraction%28_%29.md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationDragIndicator(Visibility) -> some View](./view/presentationdragindicator%28_%29.md)
  Sets the visibility of the drag indicator on top of a sheet.
- [struct PresentationDetent](./presentationdetent.md)
  A type that represents a height where a sheet naturally rests.
- [protocol CustomPresentationDetent](./custompresentationdetent.md)
  The definition of a custom detent with a calculated height.
- [struct PresentationContentInteraction](./presentationcontentinteraction.md)
  A behavior that you can use to influence how a presentation responds to swipe gestures.
- [func presentationPlacement(PresentationPlacement) -> some View](./view/presentationplacement%28_%29.md)
  Sets the placement of a presentation within the presenting view.
- [struct PresentationPlacement](./presentationplacement.md)
  The placement of a presentation within the presenting view.
### Styling a sheet and its background
- [func presentationCornerRadius(CGFloat?) -> some View](./view/presentationcornerradius%28_%29.md)
  Requests that the presentation have a specific corner radius.
- [func presentationBackground<S>(S) -> some View](./view/presentationbackground%28_%29.md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](./view/presentationbackground%28alignment,content%29.md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](./view/presentationbackgroundinteraction%28_%29.md)
  Controls whether people can interact with the view behind a presentation.
- [struct PresentationBackgroundInteraction](./presentationbackgroundinteraction.md)
  The kinds of interaction available to views behind a presentation.
### Presenting an alert
- [struct AlertScene](./alertscene.md)
  A scene that renders itself as a standalone alert dialog.
- [func alert(_:isPresented:actions:)](./view/alert%28_,ispresented,actions%29.md)
  Presents an alert when a given condition is true, using a localized string resource for the title.
- [func alert(_:isPresented:presenting:actions:)](./view/alert%28_,ispresented,presenting,actions%29.md)
  Presents an alert using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert(_:item:actions:)](./view/alert%28_,item,actions%29.md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert(error:actions:)](./view/alert%28error,actions%29.md)
  Presents an alert when an error is present.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](./view/alert%28ispresented,error,actions%29.md)
  Presents an alert when an error is present.
- [func alert(_:isPresented:actions:message:)](./view/alert%28_,ispresented,actions,message%29.md)
  Presents an alert with a message when a given condition is true, using a localized string resource for a title.
- [func alert(_:isPresented:presenting:actions:message:)](./view/alert%28_,ispresented,presenting,actions,message%29.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string resource for a title.
- [func alert(_:item:actions:message:)](./view/alert%28_,item,actions,message%29.md)
  Presents an alert with a message using the given data to produce the alert’s content and a localized string key for a title.
- [func alert(error:actions:message:)](./view/alert%28error,actions,message%29.md)
  Presents an alert with a message when an error is present.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](./view/alert%28ispresented,error,actions,message%29.md)
  Presents an alert with a message when an error is present.
### Getting confirmation for an action
- [func confirmationDialog(_:isPresented:titleVisibility:actions:)](./view/confirmationdialog%28_,ispresented,titlevisibility,actions%29.md)
  Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](./view/confirmationdialog%28_,ispresented,titlevisibility,presenting,actions%29.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:)](./view/dismissalconfirmationdialog%28_,shouldpresent,actions%29.md)
  Presents a confirmation dialog upon an attempt to dismiss the window for this view.
### Showing a confirmation dialog with a message
- [func confirmationDialog(_:isPresented:titleVisibility:actions:message:)](./view/confirmationdialog%28_,ispresented,titlevisibility,actions,message%29.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](./view/confirmationdialog%28_,ispresented,titlevisibility,presenting,actions,message%29.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:message:)](./view/dismissalconfirmationdialog%28_,shouldpresent,actions,message%29.md)
  Presents a confirmation dialog upon an attempt to dismiss the window for this view.
### Configuring a dialog
- [func dialogIcon(Image?) -> some View](./view/dialogicon%28_%29.md)
  Configures the icon used by dialogs within this view.
- [func dialogIcon(Image?) -> some Scene](./scene/dialogicon%28_%29.md)
  Configures the icon used by alerts.
- [func dialogSeverity(DialogSeverity) -> some View](./view/dialogseverity%28_%29.md)
- [func dialogSeverity(DialogSeverity) -> some Scene](./scene/dialogseverity%28_%29.md)
  Sets the severity for alerts.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](./view/dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some Scene](./scene/dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogSuppressionToggle(_:isSuppressed:)](./view/dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](./scene/dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of an alert with a custom suppression message.
- [func dialogPreventsAppTermination(Bool?) -> some View](./view/dialogpreventsapptermination%28_%29.md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
### Exporting to file
- [func fileExporter<D>(isPresented: Binding<Bool>, document: D?, contentType: UTType?, defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: (() -> Void)?) -> some View](./view/fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a `WritableDocument` to a file on disk.
- [func fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](./view/fileexporter%28ispresented,documents,contenttypes,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a collection of objects conforming to `WritableDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/fileexporter%28ispresented,item,contenttypes,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog allowing the user to export a `Transferable` item to a file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/fileexporter%28ispresented,items,contenttypes,oncompletion,oncancellation%29.md)
  Presents a system dialog allowing the user to export a collection of `Transferable` items to files on disk.
- [func fileExporterFilenameLabel(_:)](./view/fileexporterfilenamelabel%28_%29.md)
  On macOS, configures the `fileExporter` with a label for the file name field.
### Importing from file
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](./view/fileimporter%28ispresented,allowedcontenttypes,allowsmultipleselection,oncompletion%29.md)
  Presents a system dialog for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](./view/fileimporter%28ispresented,allowedcontenttypes,oncompletion%29.md)
  Presents a system dialog for allowing the user to import an existing file.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/fileimporter%28ispresented,allowedcontenttypes,allowsmultipleselection,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to import multiple files.
### Moving a file
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](./view/filemover%28ispresented,file,oncompletion%29.md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](./view/filemover%28ispresented,files,oncompletion%29.md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/filemover%28ispresented,file,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/filemover%28ispresented,files,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
### Configuring a file dialog
- [func fileDialogBrowserOptions(FileDialogBrowserOptions) -> some View](./view/filedialogbrowseroptions%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to provide a refined URL search experience: include or exclude hidden files, allow searching by tag, etc.
- [func fileDialogConfirmationLabel(_:)](./view/filedialogconfirmationlabel%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom confirmation button label.
- [func fileDialogCustomizationID(String) -> some View](./view/filedialogcustomizationid%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` to persist and restore the file dialog configuration.
- [func fileDialogDefaultDirectory(URL?) -> some View](./view/filedialogdefaultdirectory%28_%29.md)
  Configures the `fileExporter`, `fileImporter`, or `fileMover` to open with the specified default directory.
- [func fileDialogImportsUnresolvedAliases(Bool) -> some View](./view/filedialogimportsunresolvedaliases%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` behavior when a user chooses an alias.
- [func fileDialogMessage(_:)](./view/filedialogmessage%28_%29.md)
  On macOS, configures the `fileExporter`, `fileImporter`, or `fileMover` with a custom message that is presented to the user, similar to a title.
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](./view/filedialogurlenabled%28_%29.md)
  On macOS, configures the `fileImporter` or `fileMover` to conditionally disable presented URLs.
- [struct FileDialogBrowserOptions](./filedialogbrowseroptions.md)
  The way that file dialogs present the file system.
### Presenting an inspector
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](./view/inspector%28ispresented,content%29.md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](./view/inspectorcolumnwidth%28_%29.md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](./view/inspectorcolumnwidth%28min,ideal,max%29.md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
### Dismissing a presentation
- [var isPresented: Bool](./environmentvalues/ispresented.md)
  A Boolean value that indicates whether the view associated with this environment is currently presented.
- [var dismiss: DismissAction](./environmentvalues/dismiss.md)
  An action that dismisses the current presentation.
- [struct DismissAction](./dismissaction.md)
  An action that dismisses a presentation.
- [func interactiveDismissDisabled(Bool) -> some View](./view/interactivedismissdisabled%28_%29.md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
### Deprecated
- [struct Alert](./alert.md)
  A representation of an alert presentation.
- [struct ActionSheet](./actionsheet.md)
  A representation of an action sheet presentation.
- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](./view/fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion%29.md)
  Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:documents:contentType:onCompletion:)](./view/fileexporter%28ispresented,documents,contenttype,oncompletion%29.md)
  Presents a system dialog for exporting a collection of value type documents to files on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](./view/fileexporter%28ispresented,document,contenttypes,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.

## See Also

### App structure
- [App organization](./app-organization.md)
  Define the entry point and top-level structure of your app.
- [Scenes](./scenes.md)
  Declare the user interface groupings that make up the parts of your app.
- [Windows](./windows.md)
  Display user interface content in a window or a collection of windows.
- [Immersive spaces](./immersive-spaces.md)
  Display unbounded content in a person’s surroundings.
- [Documents](./documents.md)
  Enable people to open and manage documents.
- [Navigation](./navigation.md)
  Enable people to move between different parts of your app’s view hierarchy within a scene.
- [Toolbars](./toolbars.md)
  Provide immediate access to frequently used commands and controls.
- [Search](./search.md)
  Enable people to search for text or other content within your app.
- [App extensions](./app-extensions.md)
  Extend your app’s basic functionality to other parts of the system, like by adding a Widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/modal-presentations)*