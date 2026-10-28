# Technology-specific modifiers

**Framework**: SwiftUI  
**Role**: API Collection

Add modifiers to customize SwiftUI views that other Apple frameworks provide.

## Overview

Configure and customize SwiftUI views that you integrate from other Apple frameworks, such as web views from [WebKit](../WebKit/WebKit.md) or maps from [MapKit](../MapKit/MapKit.md), with these modifiers.

For more information, see [Technology-specific views](./technology-specific-views.md).

## Topics

### Displaying web content
- [struct WebView](../WebKit/webview-swift.struct.md)
  A view that displays some web content.
- [class WebPage](../WebKit/webpage.md)
  An object that controls and manages the behavior of interactive web content.
- [func onWebViewImmersiveEnvironmentRequest(shouldAllow: (WebPage.FrameInfo) async -> Bool, present: (WebPage.ImmersiveEnvironment) async throws -> Void, dismiss: (WebPage.ImmersiveEnvironment) async -> Void) -> some View](./view/onwebviewimmersiveenvironmentrequest%28shouldallow,present,dismiss%29.md)
  Manages the lifecycle of immersive environments requested by websites.
- [func webViewBackForwardNavigationGestures(WebView.BackForwardNavigationGesturesBehavior) -> some View](./view/webviewbackforwardnavigationgestures%28_%29.md)
  Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [func webViewContentBackground(Visibility) -> some View](./view/webviewcontentbackground%28_%29.md)
  Specifies the visibility of the webpage’s natural background color within this view.
- [func webViewContextMenu(menu: (WebView.ActivatedElementInfo) -> some View) -> some View](./view/webviewcontextmenu%28menu%29.md)
  Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [func webViewElementFullscreenBehavior(WebView.ElementFullscreenBehavior) -> some View](./view/webviewelementfullscreenbehavior%28_%29.md)
  Determines whether a web view can display content full screen.
- [func webViewLinkPreviews(WebView.LinkPreviewBehavior) -> some View](./view/webviewlinkpreviews%28_%29.md)
  Determines whether pressing a link displays a preview of the destination for the link.
- [func webViewMagnificationGestures(WebView.MagnificationGesturesBehavior) -> some View](./view/webviewmagnificationgestures%28_%29.md)
  Determines whether magnify gestures change the view’s magnification.
- [func webViewOnScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](./view/webviewonscrollgeometrychange%28for,of,action%29.md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func webViewScrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](./view/webviewscrollinputbehavior%28_,for%29.md)
  Enables or disables scrolling in web views when using particular inputs.
- [func webViewScrollPosition(Binding<ScrollPosition>) -> some View](./view/webviewscrollposition%28_%29.md)
  Associates a binding to a scroll position with the web view.
- [func webViewTextSelection<S>(S) -> some View](./view/webviewtextselection%28_%29.md)
  Determines whether to allow people to select or otherwise interact with text.
### Accessing Apple Pay and Wallet
- [struct PayWithApplePayButton](../PassKit/paywithapplepaybutton.md)
  A type that provides a button to pay with Apple pay.
- [struct AddPassToWalletButton](../PassKit/addpasstowalletbutton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct VerifyIdentityWithWalletButton](../PassKit/verifyidentitywithwalletbutton.md)
  A type that displays a button to present the identity verification flow.
- [func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View](./view/addordertowalletbuttonstyle%28_%29.md)
  Sets the button’s style.
- [func addPassToWalletButtonStyle(AddPassToWalletButtonStyle) -> some View](./view/addpasstowalletbuttonstyle%28_%29.md)
  Sets the style to be used by the button. (see `PKAddPassButtonStyle`).
- [func onApplePayCouponCodeChange(perform: (String) async -> PKPaymentRequestCouponCodeUpdate) -> some View](./view/onapplepaycouponcodechange%28perform%29.md)
  Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [func onApplePayPaymentMethodChange(perform: (PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate) -> some View](./view/onapplepaypaymentmethodchange%28perform%29.md)
  Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [func onApplePayShippingContactChange(perform: (PKContact) async -> PKPaymentRequestShippingContactUpdate) -> some View](./view/onapplepayshippingcontactchange%28perform%29.md)
  Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.
- [func onApplePayShippingMethodChange(perform: (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View](./view/onapplepayshippingmethodchange%28perform%29.md)
  Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [func payLaterViewAction(PayLaterViewAction) -> some View](./view/paylaterviewaction%28_%29.md)
  Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [func payLaterViewDisplayStyle(PayLaterViewDisplayStyle) -> some View](./view/paylaterviewdisplaystyle%28_%29.md)
  Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [func payWithApplePayButtonDisableCardArt() -> some View](./view/paywithapplepaybuttondisablecardart%28%29.md)
  Sets the features that should be allowed to show on the payment buttons.
- [func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View](./view/paywithapplepaybuttonstyle%28_%29.md)
  Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle) -> some View](./view/verifyidentitywithwalletbuttonstyle%28_%29.md)
  Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [struct AsyncShareablePassConfiguration](../PassKit/asyncshareablepassconfiguration.md)
- [func transactionTask(CredentialTransaction.Configuration?, action: (CredentialTransaction) async -> Void) -> some View](./view/transactiontask%28_,action%29.md)
  Provides a task to perform before this view appears
### Authorizing and authenticating
- [struct LocalAuthenticationView](../LocalAuthentication/localauthenticationview.md)
  A SwiftUI view that displays an authentication interface.
- [struct SignInWithAppleButton](../AuthenticationServices/signinwithapplebutton.md)
  A SwiftUI view that creates the Sign in with Apple button for display.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](./view/signinwithapplebuttonstyle%28_%29.md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [var authorizationController: AuthorizationController](./environmentvalues/authorizationcontroller.md)
  A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [var webAuthenticationSession: WebAuthenticationSession](./environmentvalues/webauthenticationsession.md)
  A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.
### Configuring Family Sharing
- [struct FamilyActivityPicker](../FamilyControls/familyactivitypicker.md)
  A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](./view/familyactivitypicker%28ispresented,selection%29.md)
  Presents an activity picker view as a sheet.
- [func familyActivityPicker(headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](./view/familyactivitypicker%28headertext,footertext,ispresented,selection%29.md)
  Presents an activity picker view as a sheet.
- [func familyActivityPicker(title: String?, headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](./view/familyactivitypicker%28title,headertext,footertext,ispresented,selection%29.md)
  Present an activity picker sheet for selecting apps and websites to manage.
### Reporting on device activity
- [struct DeviceActivityReport](../DeviceActivity/deviceactivityreport.md)
  A view that reports the user’s application, category, and web domain activity in a privacy-preserving way.
### Working with managed devices
- [func managedContentStyle(ManagedContentStyle) -> some View](./view/managedcontentstyle%28_%29.md)
  Applies a managed content style to the view.
- [func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some View](./view/automateddeviceenrollmentaddition%28ispresented%29.md)
  Presents a modal view that enables users to add devices to their organization.
### Creating graphics
- [struct Chart](../Charts/chart.md)
  A SwiftUI view that displays a chart.
- [struct SceneView](../SceneKit/sceneview.md)
  A SwiftUI view for displaying 3D SceneKit content.
- [struct SpriteView](../SpriteKit/spriteview.md)
  A SwiftUI view that renders a SpriteKit scene.
### Getting location information
- [struct LocationButton](../CoreLocationUI/locationbutton.md)
  A SwiftUI button that grants one-time location authorization.
- [struct Map](../MapKit/map.md)
  A view that displays an embedded map interface.
- [func mapStyle(MapStyle) -> some View](./view/mapstyle%28_%29.md)
  Specifies the map style to be used.
- [func mapScope(Namespace.ID) -> some View](./view/mapscope%28_%29.md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View](./view/mapfeatureselectiondisabled%28_%29.md)
  Specifies which map features should have selection disabled.
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View](./view/mapfeatureselectionaccessory%28_%29.md)
  Specifies the selection accessory to display for a `MapFeature`
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View](./view/mapfeatureselectioncontent%28content%29.md)
  Specifies a custom presentation for the currently selected feature.
- [func mapControls(() -> some View) -> some View](./view/mapcontrols%28_%29.md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func mapControlVisibility(Visibility) -> some View](./view/mapcontrolvisibility%28_%29.md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View](./view/mapcamerakeyframeanimator%28trigger,keyframes%29.md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](./view/lookaroundviewer%28ispresented,scene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](./view/lookaroundviewer%28ispresented,initialscene,allowsnavigation,showsroadlabels,pointsofinterest,ondismiss%29.md)
- [func onMapCameraChange(frequency:_:)](./view/onmapcamerachange%28frequency,_%29.md)
  Performs an action when Map camera framing changes
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](./view/mapitemdetailpopover%28ispresented,item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](./view/mapitemdetailpopover%28ispresented,item,displaysmap,attachmentanchor,arrowedge%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](./view/mapitemdetailpopover%28item,displaysmap,attachmentanchor%29.md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](./view/mapitemdetailpopover%28item,displaysmap,attachmentanchor,arrowedge%29.md)
  Presents a map item detail popover.
- [func mapItemDetailSheet(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool) -> some View](./view/mapitemdetailsheet%28ispresented,item,displaysmap%29.md)
  Presents a map item detail sheet.
- [func mapItemDetailSheet(item: Binding<MKMapItem?>, displaysMap: Bool) -> some View](./view/mapitemdetailsheet%28item,displaysmap%29.md)
  Presents a map item detail sheet.
### Displaying media
- [struct CameraView](../HomeKit/cameraview.md)
  A SwiftUI view into which a video stream or an image snapshot is rendered.
- [struct NowPlayingView](../WatchKit/nowplayingview.md)
  A view that displays the system’s Now Playing interface so that the user can control audio.
- [struct VideoPlayer](../AVKit/videoplayer.md)
  A view that displays content from a player and a native user interface to control playback.
- [func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect: ((AVContinuityDevice?) -> Void)?) -> some View](./view/continuitydevicepicker%28ispresented,ondidconnect%29.md)
  A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.
- [func cameraAnchor(isActive: Bool) -> some View](./view/cameraanchor%28isactive%29.md)
  Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.
- [func foveatedStreamingPauseSheet(session: Binding<FoveatedStreamingSession?>) -> some View](./view/foveatedstreamingpausesheet%28session%29.md)
  Tells the system to present a sheet with controls for resuming or ending the foveated streaming session when it pauses.
### Supporting Group Activities
- [func groupActivityAssociation(GroupActivityAssociationKind?) -> some View](./view/groupactivityassociation%28_%29.md)
  Specifies how a view should be associated with the current SharePlay group activity.
### Selecting photos
- [struct PhotosPicker](../PhotosUI/photospicker.md)
  A view that displays a Photos picker for choosing assets from the photo library.
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
- [func photosPickerMetadataOptions(PHPickerMetadataOptions) -> some View](./view/photospickermetadataoptions%28_%29.md)
  Sets metadata options for the Photos picker.
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
### Generating images
- [func imagePlaygroundGenerationStyle(ImagePlaygroundStyle, in: [ImagePlaygroundStyle]) -> some View](./view/imageplaygroundgenerationstyle%28_,in%29.md)
  Sets the selected and allowed styles to use when displaying the image generation sheet.
- [func imagePlaygroundOptions(ImagePlaygroundOptions) -> some View](./view/imageplaygroundoptions%28_%29.md)
  Sets the options to use when generating an image.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImage: Image?, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concept,sourceimage,oncompletion,oncancellation%29.md)
  Presents the system sheet to create an image using the specified string and optional starting image.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImage: Image?, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concept,sourceimage,oncompletion,onadaptiveimageglyphcreation,oncancellation%29.md)
  Presents the system sheet to create images from the specified input.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImageURL: URL, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concept,sourceimageurl,oncompletion,oncancellation%29.md)
  Presents the system sheet to create an image using the specified string and image URL.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concept: String, sourceImageURL: URL, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concept,sourceimageurl,oncompletion,onadaptiveimageglyphcreation,oncancellation%29.md)
  Presents the system sheet to create an image or Genmoji using the specified string and image URL.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImage: Image?, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concepts,sourceimage,oncompletion,oncancellation%29.md)
  Presents the system sheet to create an image using one or more concepts and an optional starting image.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImage: Image?, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concepts,sourceimage,oncompletion,onadaptiveimageglyphcreation,oncancellation%29.md)
  Presents the system sheet to create an image or Genmoji using one or more concepts and an optional starting image.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImageURL: URL, onCompletion: (URL) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concepts,sourceimageurl,oncompletion,oncancellation%29.md)
  Presents the system sheet to create an image using one or more concepts and an image URL.
- [func imagePlaygroundSheet(isPresented: Binding<Bool>, concepts: [ImagePlaygroundConcept], sourceImageURL: URL, onCompletion: (URL) -> Void, onAdaptiveImageGlyphCreation: (NSAdaptiveImageGlyph) -> Void, onCancellation: (() -> Void)?) -> some View](./view/imageplaygroundsheet%28ispresented,concepts,sourceimageurl,oncompletion,onadaptiveimageglyphcreation,oncancellation%29.md)
  Presents the system sheet to create an image or Genmoji using one or more concepts and an image URL.
### Previewing content
- [func quickLookPreview(Binding<URL?>) -> some View](./view/quicklookpreview%28_%29.md)
  Presents a Quick Look preview of the contents of a single URL.
- [func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some View](./view/quicklookpreview%28_,in%29.md)
  Presents a Quick Look preview of the URLs you provide.
### Interacting with networked devices
- [struct DevicePicker](../DeviceDiscoveryUI/devicepicker.md)
  A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [var devicePickerSupports: DevicePickerSupportedAction](./environmentvalues/devicepickersupports.md)
  Checks for support to present a DevicePicker.
### Configuring a Live Activity
- [func activitySystemActionForegroundColor(Color?) -> some View](./view/activitysystemactionforegroundcolor%28_%29.md)
  The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [func activityBackgroundTint(Color?) -> some View](./view/activitybackgroundtint%28_%29.md)
  Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [var isActivityFullscreen: Bool](./environmentvalues/isactivityfullscreen.md)
  A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [var activityFamily: ActivityFamily](./environmentvalues/activityfamily.md)
  The size family of the current Live Activity.
### Interacting with the App Store and Apple Music
- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](./view/appstoreoverlay%28ispresented,configuration%29.md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](./view/managesubscriptionssheet%28ispresented%29.md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](./view/refundrequestsheet%28for,ispresented,ondismiss%29.md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View](./view/offercoderedemption%28options,ispresented,oncompletion%29.md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
- [func musicPicker(isPresented:title:selection:)](./view/musicpicker%28ispresented,title,selection%29.md)
  Presents a music picker to select items from the Apple Music catalog and the user’s music library.
- [func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) -> some View](./view/musicsubscriptionoffer%28ispresented,options,onloadcompletion%29.md)
  Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [func currentEntitlementTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View](./view/currententitlementtask%28for,priority,action%29.md)
  Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?) -> some View](./view/inapppurchaseoptions%28_%29.md)
  Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>, subscriptionGroupID: String) -> some View](./view/managesubscriptionssheet%28ispresented,subscriptiongroupid%29.md)
- [func onInAppPurchaseCompletion(perform: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View](./view/oninapppurchasecompletion%28perform%29.md)
  Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View](./view/oninapppurchasestart%28perform%29.md)
  Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [func productIconBorder() -> some View](./view/producticonborder%28%29.md)
  Adds a standard border to an in-app purchase product’s icon .
- [func productViewStyle(some ProductViewStyle) -> some View](./view/productviewstyle%28_%29.md)
  Sets the style for In-App Purchase product views within a view.
- [func productDescription(Visibility) -> some View](./view/productdescription%28_%29.md)
  Configure the visibility of labels displaying an in-app purchase product description within the view.
- [func storeButton(Visibility, for: StoreButtonKind...) -> some View](./view/storebutton%28_,for%29.md)
  Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View](./view/storeproducttask%28for,priority,action%29.md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [func storeProductsTask(for: some Collection<String> & Equatable & Sendable, priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) -> some View](./view/storeproductstask%28for,priority,action%29.md)
  Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [func subscriptionStatusTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some View](./view/subscriptionstatustask%28for,priority,action%29.md)
  Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View](./view/subscriptionstorebuttonlabel%28_%29.md)
  Configures subscription store view instances within a view to use the provided button label.
- [func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo) -> some View) -> some View](./view/subscriptionstorecontrolicon%28icon%29.md)
  Sets a view to use to decorate individual subscription options within a subscription store view.
- [func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) -> some View](./view/subscriptionstorecontrolstyle%28_%29.md)
  Sets the control style for subscription store views within a view.
- [func subscriptionStoreControlStyle<S>(S, placement: S.Placement) -> some View](./view/subscriptionstorecontrolstyle%28_,placement%29.md)
  Sets the control style and control placement for subscription store views within a view.
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some View](./view/subscriptionstoreoptiongroupstyle%28_%29.md)
  Sets the style subscription store views within this view use to display groups of subscription options.
- [func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View](./view/subscriptionstorepickeritembackground%28_%29.md)
  Sets the background style for picker items of the subscription store view instances within a view.
- [func subscriptionStorePickerItemBackground(some ShapeStyle, in: some Shape) -> some View](./view/subscriptionstorepickeritembackground%28_,in%29.md)
  Sets the background shape and style for subscription store view picker items within a view.
- [func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind, destination: () -> some View) -> some View](./view/subscriptionstorepolicydestination%28for,destination%29.md)
  Configures a view as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyDestination(url: URL, for: SubscriptionStorePolicyKind) -> some View](./view/subscriptionstorepolicydestination%28url,for%29.md)
  Configures a URL as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View](./view/subscriptionstorepolicyforegroundstyle%28_%29.md)
  Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle) -> some View](./view/subscriptionstorepolicyforegroundstyle%28_,_%29.md)
  Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStoreSignInAction((() -> ())?) -> some View](./view/subscriptionstoresigninaction%28_%29.md)
  Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [func subscriptionStoreControlBackground(_:)](./view/subscriptionstorecontrolbackground%28_%29.md)
  Set a standard effect to use for the background of subscription store view controls within the view.
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, compactJWS: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> String) -> some View](./view/subscriptionpromotionaloffer%28offer,compactjws%29.md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [func subscriptionIntroductoryOffer(applyOffer: (Product, Product.SubscriptionInfo) -> Bool, compactJWS: (Product, Product.SubscriptionInfo) async throws -> String) -> some View](./view/subscriptionintroductoryoffer%28applyoffer,compactjws%29.md)
  Selects the introductory offer eligibility preference to apply to a purchase a customer makes from a subscription store view.
- [func subscriptionOfferViewButtonVisibility(Visibility, for: SubscriptionOfferViewButtonKind...) -> some View](./view/subscriptionofferviewbuttonvisibility%28_,for%29.md)
- [func subscriptionOfferViewDetailAction((() -> ())?) -> some View](./view/subscriptionofferviewdetailaction%28_%29.md)
- [func subscriptionOfferViewStyle(some SubscriptionOfferViewStyle) -> some View](./view/subscriptionofferviewstyle%28_%29.md)
- [func preferredSubscriptionOffer((Product, Product.SubscriptionInfo, [Product.SubscriptionOffer]) -> Product.SubscriptionOffer?) -> some View](./view/preferredsubscriptionoffer%28_%29.md)
  Selects a subscription offer to apply to a purchase that a customer makes from a subscription store view, a store view, or a product view.
- [func preferredSubscriptionPricingTerms((Product, SubscriptionInfo) -> SubscriptionInfo.PricingTerms?) -> some View](./view/preferredsubscriptionpricingterms%28_%29.md)
### Accessing health data
- [func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType, predicate: NSPredicate?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](./view/healthdataaccessrequest%28store,objecttype,predicate,trigger,completion%29.md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func healthDataAccessRequest(store: HKHealthStore, readTypes: Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](./view/healthdataaccessrequest%28store,readtypes,trigger,completion%29.md)
  Requests permission to read the specified HealthKit data types.
- [func healthDataAccessRequest(store: HKHealthStore, shareTypes: Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](./view/healthdataaccessrequest%28store,sharetypes,readtypes,trigger,completion%29.md)
  Requests permission to save and read the specified HealthKit data types.
- [func workoutPreview(WorkoutPlan, isPresented: Binding<Bool>) -> some View](./view/workoutpreview%28_,ispresented%29.md)
  Presents a preview of the workout contents as a modal sheet
### Providing tips
- [func popoverTip((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](./view/popovertip%28_,arrowedge,action%29.md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](./view/popovertip%28_,ispresented,attachmentanchor,arrowedge,action%29.md)
  Presents a popover tip on the modified view.
- [func popoverTip((any Tip)?, isPresented: Binding<Bool>?, attachmentAnchor: PopoverAttachmentAnchor, arrowEdges: Edge.Set, action: (Tips.Action) -> Void) -> some View](./view/popovertip%28_,ispresented,attachmentanchor,arrowedges,action%29.md)
  Presents a popover tip on the modified view.
- [func tipAnchor<AnchorID>(AnchorID) -> some View](./view/tipanchor%28_%29.md)
  Sets a value for the specified tip anchor to be used to anchor a tip view to the `.bounds` of the view.
- [func tipBackground<S>(S) -> some View](./view/tipbackground%28_%29.md)
  Sets the tip’s view background to a style.
- [func tipBackgroundInteraction(PresentationBackgroundInteraction) -> some View](./view/tipbackgroundinteraction%28_%29.md)
  Controls whether people can interact with the view behind a presented tip.
- [func tipCornerRadius(CGFloat, antialiased: Bool) -> some View](./view/tipcornerradius%28_,antialiased%29.md)
  Sets the corner radius for an inline tip view.
- [func tipImageSize(CGSize) -> some View](./view/tipimagesize%28_%29.md)
  Sets the size for a tip’s image.
- [func tipViewStyle(some TipViewStyle) -> some View](./view/tipviewstyle%28_%29.md)
  Sets the given style for TipView within the view hierarchy.
- [func tipImageStyle<S>(S) -> some View](./view/tipimagestyle%28_%29.md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2>(S1, S2) -> some View](./view/tipimagestyle%28_,_%29.md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2, S3>(S1, S2, S3) -> some View](./view/tipimagestyle%28_,_,_%29.md)
  Sets the style for a tip’s image.
### Showing a translation
- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](./view/translationpresentation%28ispresented,text,attachmentanchor,arrowedge,replacementaction%29.md)
  Presents a translation popover when a given condition is true.
- [func translationTask(TranslationSession.Configuration?, action: (TranslationSession) async -> Void) -> some View](./view/translationtask%28_,action%29.md)
  Adds a task to perform before this view appears or when the translation configuration changes.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](./view/translationtask%28source,target,action%29.md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, preferredStrategy: TranslationSession.Strategy, action: (TranslationSession) async -> Void) -> some View](./view/translationtask%28source,target,preferredstrategy,action%29.md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
### Presenting journaling suggestions
- [func journalingSuggestionsPicker(isPresented: Binding<Bool>, onCompletion: (JournalingSuggestion) async -> Void) -> some View](./view/journalingsuggestionspicker%28ispresented,oncompletion%29.md)
  Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
- [func journalingSuggestionsPicker(isPresented: Binding<Bool>, journalingSuggestionToken: JournalingSuggestionPresentationToken?, onCompletion: (JournalingSuggestion) async -> Void) -> some View](./view/journalingsuggestionspicker%28ispresented,journalingsuggestiontoken,oncompletion%29.md)
  Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
### Managing contact access
- [func contactAccessButtonCaption(ContactAccessButton.Caption) -> some View](./view/contactaccessbuttoncaption%28_%29.md)
- [func contactAccessButtonStyle(ContactAccessButton.Style) -> some View](./view/contactaccessbuttonstyle%28_%29.md)
- [func contactAccessPicker(isPresented: Binding<Bool>, completionHandler: ([String]) -> Void) -> some View](./view/contactaccesspicker%28ispresented,completionhandler%29.md)
  Modally present UI which allows the user to select which contacts your app has access to.
### Syncing game saves
- [func gameSaveSyncingAlert(directory: Binding<GameSaveSyncedDirectory?>, finishedLoading: () -> Void) -> some View](./view/gamesavesyncingalert%28directory,finishedloading%29.md)
  Presents a modal view while the game synced directory loads.
### Handling game controller events
- [func handlesGameControllerEvents(matching: GCUIEventTypes) -> some View](./view/handlesgamecontrollerevents%28matching%29.md)
  Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.
### Creating a tabletop game
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool) -> some View](./view/tabletopgame%28_,parent,automaticupdate%29.md)
  Adds a tabletop game to a view.
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool, interaction: (TabletopInteraction.Value) -> any TabletopInteraction.Delegate) -> some View](./view/tabletopgame%28_,parent,automaticupdate,interaction%29.md)
  Supplies a closure which returns a new interaction whenever needed.
### Configuring camera controls
- [var realityViewCameraControls: CameraControls](./environmentvalues/realityviewcameracontrols.md)
  The camera controls for the reality view.
- [func realityViewCameraControls(CameraControls) -> some View](./view/realityviewcameracontrols%28_%29.md)
  Adds gestures that control the position and direction of a virtual camera.
- [func realityViewLayoutBehavior(RealityViewLayoutOption) -> some View](./view/realityviewlayoutbehavior%28_%29.md)
  A view modifier that controls the frame sizing and content alignment behavior for `RealityView`
### Interacting with transactions
- [func transactionPicker(isPresented: Binding<Bool>, selection: Binding<[Transaction]>) -> some View](./view/transactionpicker%28ispresented,selection%29.md)
  Presents a picker that selects a collection of transactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view-technology-modifiers)*