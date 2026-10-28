# Presentation modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Define additional views for the view to present under specified conditions.

## Overview

Use presentation modifiers to show different kinds of modal presentations, like alerts, popovers, sheets, and confirmation dialogs.

Because SwiftUI is a declarative framework, you don’t call a method at the moment you want to present the modal. Rather, you define how the presentation looks and the condition under which SwiftUI should present it. SwiftUI detects when the condition changes and makes the presentation for you. Because you provide a [`Binding`](./binding.md) to the condition that initiates the presentation, SwiftUI can reset the underlying value when the user dismisses the presentation.

For more information about how to use these modifiers, see [Modal presentations](./modal-presentations.md).

## Topics

### Alerts
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
### Alerts with a message
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
### Confirmation dialogs
- [func confirmationDialog(_:isPresented:titleVisibility:actions:)](./view/confirmationdialog%28_,ispresented,titlevisibility,actions%29.md)
  Presents a confirmation dialog when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:)](./view/confirmationdialog%28_,ispresented,titlevisibility,presenting,actions%29.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog(_:item:titleVisibility:actions:)](./view/confirmationdialog%28_,item,titlevisibility,actions%29.md)
  Presents a confirmation dialog using data to produce the dialog’s content and a text view for the title.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:)](./view/dismissalconfirmationdialog%28_,shouldpresent,actions%29.md)
  Presents a confirmation dialog upon an attempt to dismiss the window for this view.
### Confirmation dialogs with a message
- [func confirmationDialog(_:isPresented:titleVisibility:actions:message:)](./view/confirmationdialog%28_,ispresented,titlevisibility,actions,message%29.md)
  Presents a confirmation dialog with a message when a given condition is true, using a localized string resource for the title.
- [func confirmationDialog(_:isPresented:titleVisibility:presenting:actions:message:)](./view/confirmationdialog%28_,ispresented,titlevisibility,presenting,actions,message%29.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a localized string resource for the title.
- [func confirmationDialog(_:item:titleVisibility:actions:message:)](./view/confirmationdialog%28_,item,titlevisibility,actions,message%29.md)
  Presents a confirmation dialog with a message using data to produce the dialog’s content and a text view for the message.
- [func dismissalConfirmationDialog(_:shouldPresent:actions:message:)](./view/dismissalconfirmationdialog%28_,shouldpresent,actions,message%29.md)
  Presents a confirmation dialog upon an attempt to dismiss the window for this view.
### Dialog configuration
- [func dialogIcon(Image?) -> some View](./view/dialogicon%28_%29.md)
  Configures the icon used by dialogs within this view.
- [func dialogSeverity(DialogSeverity) -> some View](./view/dialogseverity%28_%29.md)
- [func dialogSuppressionToggle(isSuppressed: Binding<Bool>) -> some View](./view/dialogsuppressiontoggle%28issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a default suppression message on macOS. Unused on other platforms.
- [func dialogSuppressionToggle(_:isSuppressed:)](./view/dialogsuppressiontoggle%28_,issuppressed%29.md)
  Enables user suppression of dialogs and alerts presented within `self`, with a custom suppression message on macOS. Unused on other platforms.
- [func dialogPreventsAppTermination(Bool?) -> some View](./view/dialogpreventsapptermination%28_%29.md)
  Whether the alert or confirmation dialog prevents the app from being quit/terminated by the system or app termination menu item.
### Sheets
- [func sheet<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./view/sheet%28ispresented,ondismiss,content%29.md)
  Presents a sheet when a binding to a Boolean value that you provide is true.
- [func sheet<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./view/sheet%28item,ondismiss,content%29.md)
  Presents a sheet using the given item as a data source for the sheet’s content.
- [func fullScreenCover<Content>(isPresented: Binding<Bool>, onDismiss: (() -> Void)?, content: () -> Content) -> some View](./view/fullscreencover%28ispresented,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible when binding to a Boolean value you provide is true.
- [func fullScreenCover<Item, Content>(item: Binding<Item?>, onDismiss: (() -> Void)?, content: (Item) -> Content) -> some View](./view/fullscreencover%28item,ondismiss,content%29.md)
  Presents a modal view that covers as much of the screen as possible using the binding you provide as a data source for the sheet’s content.
### Popovers
- [func popover<Item, Content>(item: Binding<Item?>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: (Item) -> Content) -> some View](./view/popover%28item,attachmentanchor,arrowedge,content%29.md)
  Presents a popover using the given item as a data source for the popover’s content.
- [func popover<Content>(isPresented: Binding<Bool>, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, content: () -> Content) -> some View](./view/popover%28ispresented,attachmentanchor,arrowedge,content%29.md)
  Presents a popover when a given condition is true.
### Sheet and popover configuration
- [func interactiveDismissDisabled(Bool) -> some View](./view/interactivedismissdisabled%28_%29.md)
  Conditionally prevents interactive dismissal of presentations like popovers, sheets, and inspectors.
- [func presentationDetents(Set<PresentationDetent>) -> some View](./view/presentationdetents%28_%29.md)
  Sets the available detents for the enclosing sheet.
- [func presentationDetents(Set<PresentationDetent>, selection: Binding<PresentationDetent>) -> some View](./view/presentationdetents%28_,selection%29.md)
  Sets the available detents for the enclosing sheet, giving you programmatic control of the currently selected detent.
- [func presentationDragIndicator(Visibility) -> some View](./view/presentationdragindicator%28_%29.md)
  Sets the visibility of the drag indicator on top of a sheet.
- [func presentationBackground<S>(S) -> some View](./view/presentationbackground%28_%29.md)
  Sets the presentation background of the enclosing sheet using a shape style.
- [func presentationBackground<V>(alignment: Alignment, content: () -> V) -> some View](./view/presentationbackground%28alignment,content%29.md)
  Sets the presentation background of the enclosing sheet to a custom view.
- [func presentationBackgroundInteraction(PresentationBackgroundInteraction) -> some View](./view/presentationbackgroundinteraction%28_%29.md)
  Controls whether people can interact with the view behind a presentation.
- [func presentationCompactAdaptation(horizontal: PresentationAdaptation, vertical: PresentationAdaptation) -> some View](./view/presentationcompactadaptation%28horizontal,vertical%29.md)
  Specifies how to adapt a presentation to horizontally and vertically compact size classes.
- [func presentationCompactAdaptation(PresentationAdaptation) -> some View](./view/presentationcompactadaptation%28_%29.md)
  Specifies how to adapt a presentation to compact size classes.
- [func presentationContentInteraction(PresentationContentInteraction) -> some View](./view/presentationcontentinteraction%28_%29.md)
  Configures the behavior of swipe gestures on a presentation.
- [func presentationCornerRadius(CGFloat?) -> some View](./view/presentationcornerradius%28_%29.md)
  Requests that the presentation have a specific corner radius.
- [func presentationSizing(some PresentationSizing) -> some View](./view/presentationsizing%28_%29.md)
  Sets the sizing of the containing presentation.
- [func presentationBreakthroughEffect(BreakthroughEffect) -> some View](./view/presentationbreakthrougheffect%28_%29.md)
  Changes the way the enclosing presentation breaks through content occluding it.
- [func presentationPreventsAppTermination(Bool?) -> some View](./view/presentationpreventsapptermination%28_%29.md)
  Whether a presentation prevents the app from being terminated/quit by the system or app termination menu item.
- [func presentationPlacement(PresentationPlacement) -> some View](./view/presentationplacement%28_%29.md)
  Sets the placement of a presentation within the presenting view.
- [struct PresentationPlacement](./presentationplacement.md)
  The placement of a presentation within the presenting view.
### File exporter
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
### File importer
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](./view/fileimporter%28ispresented,allowedcontenttypes,allowsmultipleselection,oncompletion%29.md)
  Presents a system dialog for allowing the user to import multiple files.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], onCompletion: (Result<URL, any Error>) -> Void) -> some View](./view/fileimporter%28ispresented,allowedcontenttypes,oncompletion%29.md)
  Presents a system dialog for allowing the user to import an existing file.
- [func fileImporter(isPresented: Binding<Bool>, allowedContentTypes: [UTType], allowsMultipleSelection: Bool, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/fileimporter%28ispresented,allowedcontenttypes,allowsmultipleselection,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to import multiple files.
### File mover
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void) -> some View](./view/filemover%28ispresented,file,oncompletion%29.md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void) -> some View](./view/filemover%28ispresented,files,oncompletion%29.md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
- [func fileMover(isPresented: Binding<Bool>, file: URL?, onCompletion: (Result<URL, any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/filemover%28ispresented,file,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to move an existing file to a new location.
- [func fileMover<C>(isPresented: Binding<Bool>, files: C, onCompletion: (Result<[URL], any Error>) -> Void, onCancellation: () -> Void) -> some View](./view/filemover%28ispresented,files,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to move a collection of existing files to a new location.
### File dialog configuration
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
### Foveated streaming
- [func foveatedStreamingPauseSheet(session: Binding<FoveatedStreamingSession?>) -> some View](./view/foveatedstreamingpausesheet%28session%29.md)
  Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.
### Screen capture
- [func recordingEditor(Binding<URL?>) -> some View](./view/recordingeditor%28_%29.md)
  Presents the recording editor for the given recording URL.
- [func recordingEditor(Binding<URL?>, mode: SCRecordingEditor.Mode) -> some View](./view/recordingeditor%28_,mode%29.md)
  Presents the recording editor for the given recording URL with a specific mode.
### Document browser
- [func documentLaunchTitle(_:)](./view/documentlaunchtitle%28_%29.md)
  Sets the title displayed on the document launch card.
- [func documentLaunchSubtitle(_:)](./view/documentlaunchsubtitle%28_%29.md)
  Sets the subtitle displayed beneath the title on the document launch card.
- [func documentBrowserContextMenu(([URL]?) -> some View) -> some View](./view/documentbrowsercontextmenu%28_%29.md)
  Adds to a `DocumentLaunchView` actions that accept a list of selected files as their parameter.
### Inspectors
- [func inspector<V>(isPresented: Binding<Bool>, content: () -> V) -> some View](./view/inspector%28ispresented,content%29.md)
  Inserts an inspector at the applied position in the view hierarchy.
- [func inspectorColumnWidth(CGFloat) -> some View](./view/inspectorcolumnwidth%28_%29.md)
  Sets a fixed, preferred width for the inspector containing this view when presented as a trailing column.
- [func inspectorColumnWidth(min: CGFloat?, ideal: CGFloat, max: CGFloat?) -> some View](./view/inspectorcolumnwidth%28min,ideal,max%29.md)
  Sets a flexible, preferred width for the inspector in a trailing-column presentation.
### Quick look previews
- [func quickLookPreview(Binding<URL?>) -> some View](./view/quicklookpreview%28_%29.md)
  Presents a Quick Look preview of the contents of a single URL.
- [func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some View](./view/quicklookpreview%28_,in%29.md)
  Presents a Quick Look preview of the URLs you provide.
### Family Sharing
- [func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](./view/familyactivitypicker%28ispresented,selection%29.md)
  Presents an activity picker view as a sheet.
- [func familyActivityPicker(headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](./view/familyactivitypicker%28headertext,footertext,ispresented,selection%29.md)
  Presents an activity picker view as a sheet.
- [func familyActivityPicker(title: String?, headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](./view/familyactivitypicker%28title,headertext,footertext,ispresented,selection%29.md)
  Present an activity picker sheet for selecting apps and websites to manage.
### Live Activities
- [func activitySystemActionForegroundColor(Color?) -> some View](./view/activitysystemactionforegroundcolor%28_%29.md)
  The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [func activityBackgroundTint(Color?) -> some View](./view/activitybackgroundtint%28_%29.md)
  Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
### Game saving
- [func gameSaveSyncingAlert(directory: Binding<GameSaveSyncedDirectory?>, finishedLoading: () -> Void) -> some View](./view/gamesavesyncingalert%28directory,finishedloading%29.md)
  Presents a modal view while the game synced directory loads.
### Apple Music
- [func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) -> some View](./view/musicsubscriptionoffer%28ispresented,options,onloadcompletion%29.md)
  Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
### Contacts
- [func contactAccessButtonCaption(ContactAccessButton.Caption) -> some View](./view/contactaccessbuttoncaption%28_%29.md)
- [func contactAccessButtonStyle(ContactAccessButton.Style) -> some View](./view/contactaccessbuttonstyle%28_%29.md)
- [func contactAccessPicker(isPresented: Binding<Bool>, completionHandler: ([String]) -> Void) -> some View](./view/contactaccesspicker%28ispresented,completionhandler%29.md)
  Modally present UI which allows the user to select which contacts your app has access to.
### StoreKit
- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](./view/appstoreoverlay%28ispresented,configuration%29.md)
  Presents a StoreKit overlay when a given condition is true.
- [func appStoreMerchandising(isPresented: Binding<Bool>, kind: AppStoreMerchandisingKind, onDismiss: ((Result<AppStoreMerchandisingKind.PresentationResult, any Error>) async -> ())?) -> some View](./view/appstoremerchandising%28ispresented,kind,ondismiss%29.md)
  Display a merchandising view.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](./view/managesubscriptionssheet%28ispresented%29.md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](./view/refundrequestsheet%28for,ispresented,ondismiss%29.md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View](./view/offercoderedemption%28options,ispresented,oncompletion%29.md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
### PhotoKit
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](./view/photospicker%28ispresented,selection,matching,preferreditemencoding%29.md)
  Presents a Photos picker that selects a `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<PhotosPickerItem?>, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](./view/photospicker%28ispresented,selection,matching,preferreditemencoding,photolibrary%29.md)
  Presents a Photos picker that selects a `PhotosPickerItem` from a given photo library.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy) -> some View](./view/photospicker%28ispresented,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding%29.md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem`.
- [func photosPicker(isPresented: Binding<Bool>, selection: Binding<[PhotosPickerItem]>, maxSelectionCount: Int?, selectionBehavior: PhotosPickerSelectionBehavior, matching: PHPickerFilter?, preferredItemEncoding: PhotosPickerItem.EncodingDisambiguationPolicy, photoLibrary: PHPhotoLibrary) -> some View](./view/photospicker%28ispresented,selection,maxselectioncount,selectionbehavior,matching,preferreditemencoding,photolibrary%29.md)
  Presents a Photos picker that selects a collection of `PhotosPickerItem` from a given photo library.
- [func photosPickerAccessoryVisibility(Visibility, edges: Edge.Set) -> some View](./view/photospickeraccessoryvisibility%28_,edges%29.md)
  Sets the accessory visibility of the Photos picker. Accessories include anything between the content and the edge, like the navigation bar or the sidebar.
- [func photosPickerDisabledCapabilities(PHPickerCapabilities) -> some View](./view/photospickerdisabledcapabilities%28_%29.md)
  Disables capabilities of the Photos picker.
- [func photosPickerSearchText(_:)](./view/photospickersearchtext%28_%29.md)
  Sets search text of the Photos picker.
- [func photosPickerStyle(PhotosPickerStyle) -> some View](./view/photospickerstyle%28_%29.md)
  Sets the mode of the Photos picker.
- [func photosSharedAlbumCreationSheet(isPresented: Binding<Bool>, defaultTitle: String?, defaultSharingPolicy: PHSharedAlbumCreationSharingPolicy?, photoLibrary: PHPhotoLibrary, onCompletion: ((PHSharedAlbumCreationResult?) -> Void)?) -> some View](./view/photossharedalbumcreationsheet%28ispresented,defaulttitle,defaultsharingpolicy,photolibrary,oncompletion%29.md)
  Presents a view for allowing the user to create a new shared album.
- [func photosSharedAlbumCustomizationSheet(isPresented: Binding<Bool>, albumIdentifier: String?, photoLibrary: PHPhotoLibrary, onCompletion: (((any Error)?) -> Void)?) -> some View](./view/photossharedalbumcustomizationsheet%28ispresented,albumidentifier,photolibrary,oncompletion%29.md)
  Presents a view for allowing the user to customize a specified shared album.
- [func photosSharedAlbumPostingSheet(isPresented:items:defaultAlbumIdentifier:photoLibrary:completion:)](./view/photossharedalbumpostingsheet%28ispresented,items,defaultalbumidentifier,photolibrary,completion%29.md)
  Presents an “Add to Shared Album” sheet that allows the user to post the given items to a shared album.
- [func photosReferenceImageViewer(asset: Binding<PHAsset?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View](./view/photosreferenceimageviewer%28asset,onprocessingcompletion%29.md)
  Presents an image viewer for an asset in a photo library that contains Apple Reference Image data when `asset` is set.
- [func photosReferenceImageViewer(fileURL: Binding<URL?>, onProcessingCompletion: ((Result<URL, any Error>) -> Void)?) -> some View](./view/photosreferenceimageviewer%28fileurl,onprocessingcompletion%29.md)
  Presents an image viewer for a given image file containing Apple Reference Image data when `fileURL` is set.
- [func photosReferenceImageViewer(pickerItem: Binding<PhotosPickerItem?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View](./view/photosreferenceimageviewer%28pickeritem,onprocessingcompletion%29.md)
  Presents an image viewer for an image containing Apple Reference Image data selected from the Photos picker when `pickerItem` is set.
- [func photosReferenceImageViewer(pickerResult: Binding<PHPickerResult?>, onProcessingCompletion: ((Result<PHAsset, any Error>) -> Void)?) -> some View](./view/photosreferenceimageviewer%28pickerresult,onprocessingcompletion%29.md)
  Presents an image viewer for the resulting image containing Apple Reference Image data from `PHPickerViewController` when `pickerResult` is set.
### Translation
- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](./view/translationpresentation%28ispresented,text,attachmentanchor,arrowedge,replacementaction%29.md)
  Presents a translation popover when a given condition is true.
- [func translationTask(TranslationSession.Configuration?, action: (TranslationSession) async -> Void) -> some View](./view/translationtask%28_,action%29.md)
  Adds a task to perform before this view appears or when the translation configuration changes.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](./view/translationtask%28source,target,action%29.md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy, action: (TranslationSession) async -> Void) -> some View](./view/translationtask%28source,target,preferredstrategy,action%29.md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
### Security
- [func certificateSheet(trust: Binding<SecTrust?>, title: String?, message: String?, help: URL?) -> some View](./view/certificatesheet%28trust,title,message,help%29.md)
  Displays a certificate sheet using the provided certificate trust.
### Deprecated
- [func fileExporter(isPresented:document:contentType:defaultFilename:onCompletion:)](./view/fileexporter%28ispresented,document,contenttype,defaultfilename,oncompletion%29.md)
  Presents a system dialog for exporting a document that’s stored in a value type, like a structure, to a file on disk.
- [func fileExporter(isPresented:documents:contentType:onCompletion:)](./view/fileexporter%28ispresented,documents,contenttype,oncompletion%29.md)
  Presents a system dialog for exporting a collection of value type documents to files on disk.
- [func fileExporter(isPresented:document:contentTypes:defaultFilename:onCompletion:onCancellation:)](./view/fileexporter%28ispresented,document,contenttypes,defaultfilename,oncompletion,oncancellation%29.md)
  Presents a system dialog for allowing the user to export a `FileDocument` to a file on disk.

## See Also

### Providing interactivity
- [Input and event modifiers](./view-input-and-events.md)
  Supply actions for a view to perform in response to user input and system events.
- [Search modifiers](./view-search.md)
  Enable people to search for content in your app.
- [State modifiers](./view-state.md)
  Access storage and provide child views with configuration data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-presentation)*