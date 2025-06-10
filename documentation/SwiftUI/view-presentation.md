# Presentation modifiers

**Framework**: SwiftUI

Define additional views for the view to present under specified conditions.

#### Overview

Use presentation modifiers to show different kinds of modal presentations, like alerts, popovers, sheets, and confirmation dialogs.

Because SwiftUI is a declarative framework, you don’t call a method at the moment you want to present the modal. Rather, you define how the presentation looks and the condition under which SwiftUI should present it. SwiftUI detects when the condition changes and makes the presentation for you. Because you provide a [`Binding`](binding.md) to the condition that initiates the presentation, SwiftUI can reset the underlying value when the user dismisses the presentation.

For more information about how to use these modifiers, see [`Modal presentations`](modal-presentations.md).

## Topics

### Alerts
- [func alert(_:isPresented:actions:)](view/alert(_:ispresented:actions:).md)
  Presents an alert when a given condition is true, using a text view for the title.
- [func alert(_:isPresented:presenting:actions:)](view/alert(_:ispresented:presenting:actions:).md)
  Presents an alert using the given data to produce the alert’s content and a text view as a title.
- [func alert<E, A>(isPresented: Binding<Bool>, error: E?, actions: () -> A) -> some View](view/alert(ispresented:error:actions:).md)
  Presents an alert when an error is present.
### Alerts with a message
- [func alert(_:isPresented:actions:message:)](view/alert(_:ispresented:actions:message:).md)
  Presents an alert with a message when a given condition is true using a text view as a title.
- [func alert(_:isPresented:presenting:actions:message:)](view/alert(_:ispresented:presenting:actions:message:).md)
  Presents an alert with a message using the given data to produce the alert’s content and a text view for a title.
- [func alert<E, A, M>(isPresented: Binding<Bool>, error: E?, actions: (E) -> A, message: (E) -> M) -> some View](view/alert(ispresented:error:actions:message:).md)
  Presents an alert with a message when an error is present.
### Confirmation dialogs
- [func confirmationDialog(_:isPresented:titleVisibility:actions:)](view/confirmationdialog(_:ispresented:titlevisibility:actions:).md)
  Presents a confirmation dialog when a given condition is true, using a text view for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:).md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:)](view/dismissalconfirmationdialog(_:shouldpresent:actions:).md)
  Presents a confirmation dialog when a dismiss action has been triggered.
### Confirmation dialogs with a message
- [func confirmationDialog(_:isPresented:titleVisibility:actions:message:)](view/confirmationdialog(_:ispresented:titlevisibility:actions:message:).md)
  Presents a confirmation dialog with a message when a given condition is true, using a text view for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](view/confirmationdialog(_:ispresented:titlevisibility:presenting:actions:message:).md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:message:)](view/dismissalconfirmationdialog(_:shouldpresent:actions:message:).md)
  Presents a confirmation dialog when a dismiss action has been triggered.
### Dialog configuration
- [func dialogIcon(Image?) -> some View](view/dialogicon(_:).md)
  Configures the icon used by dialogs within this view.
- [func dialogSeverity(DialogSeverity) -> some View](view/dialogseverity(_:).md)
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](view/dialogsuppressiontoggle(issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](view/dialogsuppressiontoggle(_:issuppressed:).md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
### Sheets
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](view/sheet(ispresented:ondismiss:content:).md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](view/sheet(item:ondismiss:content:).md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](view/fullscreencover(ispresented:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](view/fullscreencover(item:ondismiss:content:).md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
### Popovers
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](view/popover(item:attachmentanchor:arrowedge:content:).md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](view/popover(ispresented:attachmentanchor:arrowedge:content:).md)
  Presents a popover when a given condition is true.
### Sheet and popover configuration
- [func interactiveDismissDisabled(Bool) -> some View](view/interactivedismissdisabled(_:).md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func presentationDetents(Set<PresentationDetent>) -> some View](view/presentationdetents(_:).md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](view/presentationdetents(_:selection:).md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](view/presentationdragindicator(_:).md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationBackground<S>(S) -> some View](view/presentationbackground(_:).md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](view/presentationbackground(alignment:content:).md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](view/presentationbackgroundinteraction(_:).md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](view/presentationcompactadaptation(horizontal:vertical:).md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](view/presentationcompactadaptation(_:).md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](view/presentationcontentinteraction(_:).md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](view/presentationcornerradius(_:).md)
  Requests that the presentation have a specific corner radius.
- [func presentationSizing(some PresentationSizing) -> some View](view/presentationsizing(_:).md)
  Sets the sizing of the containing presentation.
### File exporter
- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](view/fileexporter(ispresented:document:contenttype:defaultfilename:oncompletion:).md)
  Presents a system interface for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:documents:contentType:onCompletion:)](view/fileexporter(ispresented:documents:contenttype:oncompletion:).md)
  Presents a system interface for exporting a collection of value type documents to files on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](view/fileexporter(ispresented:document:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface for allowing the user to export a `FileDocument` to a file on disk.
- [func fileExporter(isPresented:documents:contentTypes:onCompletion:onCancellation:)](view/fileexporter(ispresented:documents:contenttypes:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to export a collection of documents that conform to `FileDocument` to files on disk.
- [func fileExporter<T>(isPresented: Binding<Bool>, item: T?, contentTypes: [UTType], defaultFilename: String?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](view/fileexporter(ispresented:item:contenttypes:defaultfilename:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a `Transferable` item to file on disk.
- [func fileExporter<C, T>(isPresented: Binding<Bool>, items: C, contentTypes: [UTType], onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](view/fileexporter(ispresented:items:contenttypes:oncompletion:oncancellation:).md)
  Presents a system interface allowing the user to export a collection of items to files on disk.
- [func fileExporterFilenameLabel(_:)](view/fileexporterfilenamelabel(_:).md)
  On macOS, configures the `fileExporter` with a label for the file name field.
### File importer
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](view/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:).md)
  Presents a system interface for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](view/fileimporter(ispresented:allowedcontenttypes:oncompletion:).md)
  Presents a system interface for allowing the user to import an existing file.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](view/fileimporter(ispresented:allowedcontenttypes:allowsmultipleselection:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to import multiple files.
### File mover
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](view/filemover(ispresented:file:oncompletion:).md)
  Presents a system interface for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](view/filemover(ispresented:files:oncompletion:).md)
  Presents a system interface for allowing the user to move a collection of existing files to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](view/filemover(ispresented:file:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](view/filemover(ispresented:files:oncompletion:oncancellation:).md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
### File dialog configuration
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
- [func fileDialogURLEnabled(Predicate<URL>) -> some View](view/filedialogurlenabled(_:).md)
  On macOS, configures the the `fileImporter` or `fileMover` to conditionally disable presented URLs.
### Inspectors
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](view/inspector(ispresented:content:).md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](view/inspectorcolumnwidth(_:).md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](view/inspectorcolumnwidth(min:ideal:max:).md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
### Quick look previews
- [func quickLookPreview(Binding<URL?>) -> some View](view/quicklookpreview(_:).md)
  Presents a Quick Look preview of the contents of a single URL.
- [func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some View](view/quicklookpreview(_:in:).md)
  Presents a Quick Look preview of the URLs you provide.
### Family Sharing
- [func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(ispresented:selection:).md)
  Presents an activity picker view as a sheet.
- [func familyActivityPicker(headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(headertext:footertext:ispresented:selection:).md)
  Presents an activity picker view as a sheet.
### Live Activities
- [func activitySystemActionForegroundColor(Color?) -> some View](view/activitysystemactionforegroundcolor(_:).md)
  The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [func activityBackgroundTint(Color?) -> some View](view/activitybackgroundtint(_:).md)
  Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
### Apple Music
- [func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) -> some View](view/musicsubscriptionoffer(ispresented:options:onloadcompletion:).md)
  Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
### StoreKit
- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](view/appstoreoverlay(ispresented:configuration:).md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](view/managesubscriptionssheet(ispresented:).md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](view/refundrequestsheet(for:ispresented:ondismiss:).md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](view/offercoderedemption(ispresented:oncompletion:).md)
  Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.
### PhotoKit
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](view/photospicker(ispresented:selection:matching:preferreditemencoding:).md)
  Presents a Photos picker that selects a `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](view/photospicker(ispresented:selection:matching:preferreditemencoding:photolibrary:).md)
  Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](view/photospicker(ispresented:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:).md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](view/photospicker(ispresented:selection:maxselectioncount:selectionbehavior:matching:preferreditemencoding:photolibrary:).md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some View](view/photospickeraccessoryvisibility(_:edges:).md)
  Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View](view/photospickerdisabledcapabilities(_:).md)
  Disables capabilities of the Photos picker.
- [func photosPickerStyle(PhotosPickerStyle) -> some View](view/photospickerstyle(_:).md)
  Sets the mode of the Photos picker.

## See Also

- [Input and event modifiers](view-input-and-events.md)
  Supply actions for a view to perform in response to user input and system events.
- [Search modifiers](view-search.md)
  Enable people to search for content in your app.
- [State modifiers](view-state.md)
  Access storage and provide child views with configuration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-presentation)*