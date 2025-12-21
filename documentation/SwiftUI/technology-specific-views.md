# Technology-specific views

**Framework**: SwiftUI

Use SwiftUI views that other Apple frameworks provide.

#### Overview

To access SwiftUI views that another framework defines, import both SwiftUI and the other framework into the file where you use the view. You can find the framework to import by looking at the availability information on the view’s documentation page.

![None](https://docs-assets.developer.apple.com/published/dd13486d673485bcc02e34a3f2e756dd/technology-specific-views-hero%402x.png)

For example, to use the [`Map`](https://developer.apple.com/documentation/MapKit/Map) view in your app, import both SwiftUI and MapKit.

```swift
import SwiftUI
import MapKit

struct MyMapView: View {
    // Center the map on Joshua Tree National Park.
    var region = MKCoordinateRegion(
            center: CLLocationCoordinate2D(latitude: 34.011_286, longitude: -116.166_868),
            span: MKCoordinateSpan(latitudeDelta: 0.2, longitudeDelta: 0.2)
        )

    var body: some View {
        Map(initialPosition: .region(region))
    }
}
```

For design guidance, see [`Technologies`](https://developer.apple.com/design/Human-Interface-Guidelines/technologies) in the Human Interface Guidelines.

## Topics

### Displaying web content
- [struct WebView](../WebKit/WebView-swift.struct.md)
  A view that displays some web content.
- [class WebPage](../WebKit/WebPage.md)
  An object that controls and manages the behavior of interactive web content.
- [func webViewBackForwardNavigationGestures(WebView.BackForwardNavigationGesturesBehavior) -> some View](view/webviewbackforwardnavigationgestures(_:).md)
  Determines whether horizontal swipe gestures trigger backward and forward page navigation.
- [func webViewContentBackground(Visibility) -> some View](view/webviewcontentbackground(_:).md)
  Specifies the visibility of the webpage’s natural background color within this view.
- [func webViewContextMenu(menu: (WebView.ActivatedElementInfo) -> some View) -> some View](view/webviewcontextmenu(menu:).md)
  Adds an item-based context menu to a WebView, replacing the default set of context menu items.
- [func webViewElementFullscreenBehavior(WebView.ElementFullscreenBehavior) -> some View](view/webviewelementfullscreenbehavior(_:).md)
  Determines whether a web view can display content full screen.
- [func webViewLinkPreviews(WebView.LinkPreviewBehavior) -> some View](view/webviewlinkpreviews(_:).md)
  Determines whether pressing a link displays a preview of the destination for the link.
- [func webViewMagnificationGestures(WebView.MagnificationGesturesBehavior) -> some View](view/webviewmagnificationgestures(_:).md)
  Determines whether magnify gestures change the view’s magnification.
- [func webViewOnScrollGeometryChange<T>(for: T.Type, of: (ScrollGeometry) -> T, action: (T, T) -> Void) -> some View](view/webviewonscrollgeometrychange(for:of:action:).md)
  Adds an action to be performed when a value, created from a scroll geometry, changes.
- [func webViewScrollInputBehavior(ScrollInputBehavior, for: ScrollInputKind) -> some View](view/webviewscrollinputbehavior(_:for:).md)
  Enables or disables scrolling in web views when using particular inputs.
- [func webViewScrollPosition(Binding<ScrollPosition>) -> some View](view/webviewscrollposition(_:).md)
  Associates a binding to a scroll position with the web view.
- [func webViewTextSelection<S>(S) -> some View](view/webviewtextselection(_:).md)
  Determines whether to allow people to select or otherwise interact with text.
### Accessing Apple Pay and Wallet
- [struct PayWithApplePayButton](../PassKit/PayWithApplePayButton.md)
  A type that provides a button to pay with Apple pay.
- [struct AddPassToWalletButton](../PassKit/AddPassToWalletButton.md)
  A type that provides a button that enables people to add a new or existing pass to Apple Wallet.
- [struct VerifyIdentityWithWalletButton](../PassKit/VerifyIdentityWithWalletButton.md)
  A type that displays a button to present the identity verification flow.
- [func addOrderToWalletButtonStyle(AddOrderToWalletButtonStyle) -> some View](view/addordertowalletbuttonstyle(_:).md)
  Sets the button’s style.
- [func addPassToWalletButtonStyle(AddPassToWalletButtonStyle) -> some View](view/addpasstowalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKAddPassButtonStyle`).
- [func onApplePayCouponCodeChange(perform: (String) async -> PKPaymentRequestCouponCodeUpdate) -> some View](view/onapplepaycouponcodechange(perform:).md)
  Called when a user has entered or updated a coupon code. This is required if the user is being asked to provide a coupon code.
- [func onApplePayPaymentMethodChange(perform: (PKPaymentMethod) async -> PKPaymentRequestPaymentMethodUpdate) -> some View](view/onapplepaypaymentmethodchange(perform:).md)
  Called when a payment method has changed and asks for an update payment request. If this modifier isn’t provided Wallet will assume the payment method is valid.
- [func onApplePayShippingContactChange(perform: (PKContact) async -> PKPaymentRequestShippingContactUpdate) -> some View](view/onapplepayshippingcontactchange(perform:).md)
  Called when a user selected a shipping address. This is required if the user is being asked to provide a shipping contact.
- [func onApplePayShippingMethodChange(perform: (PKShippingMethod) async -> PKPaymentRequestShippingMethodUpdate) -> some View](view/onapplepayshippingmethodchange(perform:).md)
  Called when a user selected a shipping method. This is required if the user is being asked to provide a shipping method.
- [func payLaterViewAction(PayLaterViewAction) -> some View](view/paylaterviewaction(_:).md)
  Sets the action on the PayLaterView. See `PKPayLaterAction`.
- [func payLaterViewDisplayStyle(PayLaterViewDisplayStyle) -> some View](view/paylaterviewdisplaystyle(_:).md)
  Sets the display style on the PayLaterView. See `PKPayLaterDisplayStyle`.
- [func payWithApplePayButtonStyle(PayWithApplePayButtonStyle) -> some View](view/paywithapplepaybuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PayWithApplePayButtonStyle`).
- [func verifyIdentityWithWalletButtonStyle(VerifyIdentityWithWalletButtonStyle) -> some View](view/verifyidentitywithwalletbuttonstyle(_:).md)
  Sets the style to be used by the button. (see `PKIdentityButtonStyle`).
- [struct AsyncShareablePassConfiguration](../PassKit/AsyncShareablePassConfiguration.md)
- [func transactionTask(CredentialTransaction.Configuration?, action: (CredentialTransaction) async -> Void) -> some View](view/transactiontask(_:action:).md)
  Provides a task to perform before this view appears
### Authorizing and authenticating
- [struct LocalAuthenticationView](../LocalAuthentication/LocalAuthenticationView.md)
  A SwiftUI view that displays an authentication interface.
- [struct SignInWithAppleButton](../AuthenticationServices/SignInWithAppleButton.md)
  A SwiftUI view that creates the Sign in with Apple button for display.
- [func signInWithAppleButtonStyle(SignInWithAppleButton.Style) -> some View](view/signinwithapplebuttonstyle(_:).md)
  Sets the style used for displaying the control (see `SignInWithAppleButton.Style`).
- [var authorizationController: AuthorizationController](environmentvalues/authorizationcontroller.md)
  A value provided in the SwiftUI environment that views can use to perform authorization requests.
- [var webAuthenticationSession: WebAuthenticationSession](environmentvalues/webauthenticationsession.md)
  A value provided in the SwiftUI environment that views can use to authenticate a user through a web service.
### Configuring Family Sharing
- [struct FamilyActivityPicker](../FamilyControls/FamilyActivityPicker.md)
  A view in which users specify applications, web domains, and categories without revealing their choices to the app.
- [func familyActivityPicker(isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(ispresented:selection:).md)
  Presents an activity picker view as a sheet.
- [func familyActivityPicker(headerText: String?, footerText: String?, isPresented: Binding<Bool>, selection: Binding<FamilyActivitySelection>) -> some View](view/familyactivitypicker(headertext:footertext:ispresented:selection:).md)
  Presents an activity picker view as a sheet.
### Reporting on device activity
- [struct DeviceActivityReport](../DeviceActivity/DeviceActivityReport.md)
  A view that reports the user’s application, category, and web domain activity in a privacy-preserving way.
### Working with managed devices
- [func managedContentStyle(ManagedContentStyle) -> some View](view/managedcontentstyle(_:).md)
  Applies a managed content style to the view.
- [func automatedDeviceEnrollmentAddition(isPresented: Binding<Bool>) -> some View](view/automateddeviceenrollmentaddition(ispresented:).md)
  Presents a modal view that enables users to add devices to their organization.
### Creating graphics
- [struct Chart](../Charts/Chart.md)
  A SwiftUI view that displays a chart.
- [struct SceneView](../SceneKit/SceneView.md)
  A SwiftUI view for displaying 3D SceneKit content.
- [struct SpriteView](../SpriteKit/SpriteView.md)
  A SwiftUI view that renders a SpriteKit scene.
### Getting location information
- [struct LocationButton](../CoreLocationUI/LocationButton.md)
  A SwiftUI button that grants one-time location authorization.
- [struct Map](../MapKit/Map.md)
  A view that displays an embedded map interface.
- [func mapStyle(MapStyle) -> some View](view/mapstyle(_:).md)
  Specifies the map style to be used.
- [func mapScope(Namespace.ID) -> some View](view/mapscope(_:).md)
  Creates a mapScope that SwiftUI uses to connect map controls to an associated map.
- [func mapFeatureSelectionDisabled((MapFeature) -> Bool) -> some View](view/mapfeatureselectiondisabled(_:).md)
  Specifies which map features should have selection disabled.
- [func mapFeatureSelectionAccessory(MapItemDetailSelectionAccessoryStyle?) -> some View](view/mapfeatureselectionaccessory(_:).md)
  Specifies the selection accessory to display for a `MapFeature`
- [func mapFeatureSelectionContent(content: (MapFeature) -> some MapContent) -> some View](view/mapfeatureselectioncontent(content:).md)
  Specifies a custom presentation for the currently selected feature.
- [func mapControls(() -> some View) -> some View](view/mapcontrols(_:).md)
  Configures all `Map` views in the associated environment to have standard size and position controls
- [func mapControlVisibility(Visibility) -> some View](view/mapcontrolvisibility(_:).md)
  Configures all Map controls in the environment to have the specified visibility
- [func mapCameraKeyframeAnimator(trigger: some Equatable, keyframes: (MapCamera) -> some Keyframes<MapCamera>) -> some View](view/mapcamerakeyframeanimator(trigger:keyframes:).md)
  Uses the given keyframes to animate the camera of a `Map` when the given trigger value changes.
- [func lookAroundViewer(isPresented: Binding<Bool>, scene: Binding<MKLookAroundScene?>, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](view/lookaroundviewer(ispresented:scene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
- [func lookAroundViewer(isPresented: Binding<Bool>, initialScene: MKLookAroundScene?, allowsNavigation: Bool, showsRoadLabels: Bool, pointsOfInterest: PointOfInterestCategories, onDismiss: (() -> Void)?) -> some View](view/lookaroundviewer(ispresented:initialscene:allowsnavigation:showsroadlabels:pointsofinterest:ondismiss:).md)
- [func onMapCameraChange(frequency:_:)](view/onmapcamerachange(frequency:_:).md)
  Performs an action when Map camera framing changes
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](view/mapitemdetailpopover(ispresented:item:displaysmap:attachmentanchor:arrowedge:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor) -> some View](view/mapitemdetailpopover(item:displaysmap:attachmentanchor:).md)
  Presents a map item detail popover.
- [func mapItemDetailPopover(item: Binding<MKMapItem?>, displaysMap: Bool, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge) -> some View](view/mapitemdetailpopover(item:displaysmap:attachmentanchor:arrowedge:).md)
  Presents a map item detail popover.
- [func mapItemDetailSheet(isPresented: Binding<Bool>, item: MKMapItem?, displaysMap: Bool) -> some View](view/mapitemdetailsheet(ispresented:item:displaysmap:).md)
  Presents a map item detail sheet.
- [func mapItemDetailSheet(item: Binding<MKMapItem?>, displaysMap: Bool) -> some View](view/mapitemdetailsheet(item:displaysmap:).md)
  Presents a map item detail sheet.
### Displaying media
- [struct CameraView](../HomeKit/CameraView.md)
  A SwiftUI view into which a video stream or an image snapshot is rendered.
- [struct NowPlayingView](../WatchKit/NowPlayingView.md)
  A view that displays the system’s Now Playing interface so that the user can control audio.
- [struct VideoPlayer](../AVKit/VideoPlayer.md)
  A view that displays content from a player and a native user interface to control playback.
- [func continuityDevicePicker(isPresented: Binding<Bool>, onDidConnect: ((AVContinuityDevice?) -> Void)?) -> some View](view/continuitydevicepicker(ispresented:ondidconnect:).md)
  A `continuityDevicePicker` should be used to discover and connect nearby continuity device through a button interface or other form of activation. On tvOS, this presents a fullscreen continuity device picker experience when selected. The modal view covers as much the screen of `self` as possible when a given condition is true.
- [func cameraAnchor(isActive: Bool) -> some View](view/cameraanchor(isactive:).md)
  Specifies the view that should act as the virtual camera for Apple Vision Pro 2D Persona stream.
### Selecting photos
- [struct PhotosPicker](../PhotosUI/PhotosPicker.md)
  A view that displays a Photos picker for choosing assets from the photo library.
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
### Previewing content
- [func quickLookPreview(Binding<URL?>) -> some View](view/quicklookpreview(_:).md)
  Presents a Quick Look preview of the contents of a single URL.
- [func quickLookPreview<Items>(Binding<Items.Element?>, in: Items) -> some View](view/quicklookpreview(_:in:).md)
  Presents a Quick Look preview of the URLs you provide.
### Interacting with networked devices
- [struct DevicePicker](../DeviceDiscoveryUI/DevicePicker.md)
  A SwiftUI view that displays other devices on the network, and creates an encrypted connection to a copy of your app running on that device.
- [var devicePickerSupports: DevicePickerSupportedAction](environmentvalues/devicepickersupports.md)
  Checks for support to present a DevicePicker.
### Configuring a Live Activity
- [func activitySystemActionForegroundColor(Color?) -> some View](view/activitysystemactionforegroundcolor(_:).md)
  The text color for the auxiliary action button that the system shows next to a Live Activity on the Lock Screen.
- [func activityBackgroundTint(Color?) -> some View](view/activitybackgroundtint(_:).md)
  Sets the tint color for the background of a Live Activity that appears on the Lock Screen.
- [var isActivityFullscreen: Bool](environmentvalues/isactivityfullscreen.md)
  A Boolean value that indicates whether the Live Activity appears in a full-screen presentation.
- [var activityFamily: ActivityFamily](environmentvalues/activityfamily.md)
  The size family of the current Live Activity.
### Interacting with the App Store and Apple Music
- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](view/appstoreoverlay(ispresented:configuration:).md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](view/managesubscriptionssheet(ispresented:).md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](view/refundrequestsheet(for:ispresented:ondismiss:).md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](view/offercoderedemption(ispresented:oncompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
- [func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) -> some View](view/musicsubscriptionoffer(ispresented:options:onloadcompletion:).md)
  Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [func currentEntitlementTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View](view/currententitlementtask(for:priority:action:).md)
  Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?) -> some View](view/inapppurchaseoptions(_:).md)
  Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>, subscriptionGroupID: String) -> some View](view/managesubscriptionssheet(ispresented:subscriptiongroupid:).md)
- [func onInAppPurchaseCompletion(perform: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View](view/oninapppurchasecompletion(perform:).md)
  Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View](view/oninapppurchasestart(perform:).md)
  Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [func productIconBorder() -> some View](view/producticonborder.md)
  Adds a standard border to an in-app purchase product’s icon .
- [func productViewStyle(some ProductViewStyle) -> some View](view/productviewstyle(_:).md)
  Sets the style for In-App Purchase product views within a view.
- [func productDescription(Visibility) -> some View](view/productdescription(_:).md)
  Configure the visibility of labels displaying an in-app purchase product description within the view.
- [func storeButton(Visibility, for: StoreButtonKind...) -> some View](view/storebutton(_:for:).md)
  Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View](view/storeproducttask(for:priority:action:).md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [func storeProductsTask(for: some Collection<String> & Equatable & Sendable, priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) -> some View](view/storeproductstask(for:priority:action:).md)
  Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [func subscriptionStatusTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some View](view/subscriptionstatustask(for:priority:action:).md)
  Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View](view/subscriptionstorebuttonlabel(_:).md)
  Configures subscription store view instances within a view to use the provided button label.
- [func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo) -> some View) -> some View](view/subscriptionstorecontrolicon(icon:).md)
  Sets a view to use to decorate individual subscription options within a subscription store view.
- [func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) -> some View](view/subscriptionstorecontrolstyle(_:).md)
  Sets the control style for subscription store views within a view.
- [func subscriptionStoreControlStyle<S>(S, placement: S.Placement) -> some View](view/subscriptionstorecontrolstyle(_:placement:).md)
  Sets the control style and control placement for subscription store views within a view.
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some View](view/subscriptionstoreoptiongroupstyle(_:).md)
  Sets the style subscription store views within this view use to display groups of subscription options.
- [func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View](view/subscriptionstorepickeritembackground(_:).md)
  Sets the background style for picker items of the subscription store view instances within a view.
- [func subscriptionStorePickerItemBackground(some ShapeStyle, in: some Shape) -> some View](view/subscriptionstorepickeritembackground(_:in:).md)
  Sets the background shape and style for subscription store view picker items within a view.
- [func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind, destination: () -> some View) -> some View](view/subscriptionstorepolicydestination(for:destination:).md)
  Configures a view as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyDestination(url: URL, for: SubscriptionStorePolicyKind) -> some View](view/subscriptionstorepolicydestination(url:for:).md)
  Configures a URL as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View](view/subscriptionstorepolicyforegroundstyle(_:).md)
  Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle) -> some View](view/subscriptionstorepolicyforegroundstyle(_:_:).md)
  Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStoreSignInAction((() -> ())?) -> some View](view/subscriptionstoresigninaction(_:).md)
  Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [func subscriptionStoreControlBackground(_:)](view/subscriptionstorecontrolbackground(_:).md)
  Set a standard effect to use for the background of subscription store view controls within the view.
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View](view/subscriptionpromotionaloffer(offer:signature:).md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [func preferredSubscriptionOffer((Product, Product.SubscriptionInfo, [Product.SubscriptionOffer]) -> Product.SubscriptionOffer?) -> some View](view/preferredsubscriptionoffer(_:).md)
  Selects a subscription offer to apply to a purchase that a customer makes from a subscription store view, a store view, or a product view.
### Accessing health data
- [func healthDataAccessRequest(store: HKHealthStore, objectType: HKObjectType, predicate: NSPredicate?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:objecttype:predicate:trigger:completion:).md)
  Asynchronously requests permission to read a data type that requires per-object authorization (such as vision prescriptions).
- [func healthDataAccessRequest(store: HKHealthStore, readTypes: Set<HKObjectType>, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:readtypes:trigger:completion:).md)
  Requests permission to read the specified HealthKit data types.
- [func healthDataAccessRequest(store: HKHealthStore, shareTypes: Set<HKSampleType>, readTypes: Set<HKObjectType>?, trigger: some Equatable, completion: (Result<Bool, any Error>) -> Void) -> some View](view/healthdataaccessrequest(store:sharetypes:readtypes:trigger:completion:).md)
  Requests permission to save and read the specified HealthKit data types.
- [func workoutPreview(WorkoutPlan, isPresented: Binding<Bool>) -> some View](view/workoutpreview(_:ispresented:).md)
  Presents a preview of the workout contents as a modal sheet
### Providing tips
- [func popoverTip((any Tip)?, arrowEdge: Edge?, action: (Tips.Action) -> Void) -> some View](view/popovertip(_:arrowedge:action:).md)
  Presents a popover tip on the modified view.
- [func tipBackground<S>(S) -> some View](view/tipbackground(_:).md)
  Sets the tip’s view background to a style. Currently this only applies to inline tips, not popover tips.
- [func tipCornerRadius(CGFloat, antialiased: Bool) -> some View](view/tipcornerradius(_:antialiased:).md)
  Sets the corner radius for an inline tip view.
- [func tipImageSize(CGSize) -> some View](view/tipimagesize(_:).md)
  Sets the size for a tip’s image.
- [func tipViewStyle(some TipViewStyle) -> some View](view/tipviewstyle(_:).md)
  Sets the given style for TipView within the view hierarchy.
- [func tipImageStyle<S>(S) -> some View](view/tipimagestyle(_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2>(S1, S2) -> some View](view/tipimagestyle(_:_:).md)
  Sets the style for a tip’s image.
- [func tipImageStyle<S1, S2, S3>(S1, S2, S3) -> some View](view/tipimagestyle(_:_:_:).md)
  Sets the style for a tip’s image.
### Showing a translation
- [func translationPresentation(isPresented: Binding<Bool>, text: String, attachmentAnchor: PopoverAttachmentAnchor, arrowEdge: Edge, replacementAction: ((String) -> Void)?) -> some View](view/translationpresentation(ispresented:text:attachmentanchor:arrowedge:replacementaction:).md)
  Presents a translation popover when a given condition is true.
- [func translationTask(TranslationSession.Configuration?, action: (TranslationSession) async -> Void) -> some View](view/translationtask(_:action:).md)
  Adds a task to perform before this view appears or when the translation configuration changes.
- [func translationTask(source: Locale.Language?, target: Locale.Language?, action: (TranslationSession) async -> Void) -> some View](view/translationtask(source:target:action:).md)
  Adds a task to perform before this view appears or when the specified source or target languages change.
### Presenting journaling suggestions
- [func journalingSuggestionsPicker(isPresented: Binding<Bool>, onCompletion: (JournalingSuggestion) async -> Void) -> some View](view/journalingsuggestionspicker(ispresented:oncompletion:).md)
  Presents a visual picker interface that contains events and images that a person can select to retrieve more information.
### Managing contact access
- [func contactAccessButtonCaption(ContactAccessButton.Caption) -> some View](view/contactaccessbuttoncaption(_:).md)
- [func contactAccessButtonStyle(ContactAccessButton.Style) -> some View](view/contactaccessbuttonstyle(_:).md)
- [func contactAccessPicker(isPresented: Binding<Bool>, completionHandler: ([String]) -> ()) -> some View](view/contactaccesspicker(ispresented:completionhandler:).md)
  Modally present UI which allows the user to select which contacts your app has access to.
### Handling game controller events
- [func handlesGameControllerEvents(matching: GCUIEventTypes) -> some View](view/handlesgamecontrollerevents(matching:).md)
  Specifies the game controllers events which should be delivered through the GameController framework when the view, or one of its descendants has focus.
### Creating a tabletop game
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool) -> some View](view/tabletopgame(_:parent:automaticupdate:).md)
  Adds a tabletop game to a view.
- [func tabletopGame(TabletopGame, parent: Entity, automaticUpdate: Bool, interaction: (TabletopInteraction.Value) -> any TabletopInteraction.Delegate) -> some View](view/tabletopgame(_:parent:automaticupdate:interaction:).md)
  Supplies a closure which returns a new interaction whenever needed.
### Configuring camera controls
- [var realityViewCameraControls: CameraControls](environmentvalues/realityviewcameracontrols.md)
  The camera controls for the reality view.
- [func realityViewCameraControls(CameraControls) -> some View](view/realityviewcameracontrols(_:).md)
  Adds gestures that control the position and direction of a virtual camera.
### Interacting with transactions
- [func transactionPicker(isPresented: Binding<Bool>, selection: Binding<[Transaction]>) -> some View](view/transactionpicker(ispresented:selection:).md)
  Presents a picker that selects a collection of transactions.

## See Also

- [AppKit integration](appkit-integration.md)
  Add AppKit views to your SwiftUI app, or use SwiftUI views in your AppKit app.
- [UIKit integration](uikit-integration.md)
  Add UIKit views to your SwiftUI app, or use SwiftUI views in your UIKit app.
- [WatchKit integration](watchkit-integration.md)
  Add WatchKit views to your SwiftUI app, or use SwiftUI views in your WatchKit app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/technology-specific-views)*