# StoreKit views

**Framework**: StoreKit

Display a customizable In-App Purchase store using StoreKit views for SwiftUI.

#### Overview

The StoreKit views APIs provide UI to help you build a store for your In-App Purchases, and provide a way for customers to complete the purchase. The views support localization, so your customers see the product names, descriptions, and prices appropriate to their App Store storefront.

> **Note**:  Session 10013: [`Meet StoreKit for SwiftUI`](https://developer.apple.comhttps://developer.apple.com/videos/play/wwdc2023/10013)

StoreKit manages the layouts across all platforms, so the views look great on any device. You can use SwiftUI APIs to customize how the views integrate with your app.

To use StoreKit views, configure your In-App Purchase metadata in App Store Connect, or in a StoreKit configuration file in Xcode if you’re testing your app. Next, create the views using [`StoreView`](storeview.md), [`ProductView`](productview.md), or [`SubscriptionStoreView`](subscriptionstoreview.md). Finally, customize the default views to match your app by using your own icons, backgrounds, and other styling. Use [`Previews in Xcode`](https://developer.apple.com/documentation/SwiftUI/Previews-in-Xcode) to see your progress as you iterate on your design.

For more information on configuring your In-App Purchase metadata, see [`Manage In-App Purchases`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devae49fb316). For more information on StoreKit configuration files in Xcode, see [`Setting up StoreKit Testing in Xcode`](https://developer.apple.com/documentation/Xcode/setting-up-storekit-testing-in-xcode).

## Topics

### Merchandising In-App Purchases, subscriptions, and offers
- [struct ProductView](productview.md)
  A view that merchandises an individual In-App Purchase product.
- [struct StoreView](storeview.md)
  A view that merchandises a collection of In-App Purchase products.
- [struct SubscriptionStoreView](subscriptionstoreview.md)
  A view that merchandises a collection of auto-renewable subscription options that belong to the same subscription group.
- [struct SubscriptionOfferView](subscriptionofferview.md)
- [Backyard Birds: Building an app with SwiftData and widgets](../SwiftUI/Backyard-birds-sample.md)
  Create an app with persistent data, interactive widgets, and an all new in-app purchase experience.
### Styling product views
- [func productViewStyle(some ProductViewStyle) -> some View](../SwiftUI/View/productViewStyle(_:).md)
  Sets the style for In-App Purchase product views within a view.
- [func productIconBorder() -> some View](../SwiftUI/View/productIconBorder.md)
  Adds a standard border to an in-app purchase product’s icon .
- [protocol ProductViewStyle](productviewstyle.md)
  A type that specifies the appearance and interaction of In-App Purchase products within the view hierarchy.
- [struct ProductViewStyleConfiguration](productviewstyleconfiguration.md)
  The properties of an In-App Purchase product for use by custom product view styles.
### Styling subscription store controls
- [func subscriptionStoreControlStyle(some SubscriptionStoreControlStyle) -> some View](../SwiftUI/View/subscriptionStoreControlStyle(_:).md)
  Sets the control style for subscription store views within a view.
- [func subscriptionStoreControlStyle<S>(S, placement: S.Placement) -> some View](../SwiftUI/View/subscriptionStoreControlStyle(_:placement:).md)
  Sets the control style and control placement for subscription store views within a view.
- [protocol SubscriptionStoreControlStyle](subscriptionstorecontrolstyle.md)
  A type that specifies the appearance and interaction of controls in the subscription store view instances within the view hierarchy.
- [struct SubscriptionStoreControlStyleConfiguration](subscriptionstorecontrolstyleconfiguration.md)
  The properties of a subscription store control that includes the list of auto-renewable subscriptions to merchandise.
- [protocol SubscriptionStoreControlPlacement](subscriptionstorecontrolplacement.md)
  A type that specifies the placement of a subscription control in a subscription store view.
### Styling subscription offer views
- [struct AutomaticSubscriptionOfferViewStyle](automaticsubscriptionofferviewstyle.md)
- [struct CompactSubscriptionOfferViewStyle](compactsubscriptionofferviewstyle.md)
- [struct SubscriptionOfferViewStyleConfiguration](subscriptionofferviewstyleconfiguration.md)
- [protocol SubscriptionOfferViewStyle](subscriptionofferviewstyle.md)
### Configuring subscription store controls
- [func subscriptionStoreControlIcon(icon: (Product, Product.SubscriptionInfo) -> some View) -> some View](../SwiftUI/View/subscriptionStoreControlIcon(icon:).md)
  Sets a view to use to decorate individual subscription options within a subscription store view.
- [func subscriptionStorePickerItemBackground(some ShapeStyle) -> some View](../SwiftUI/View/subscriptionStorePickerItemBackground(_:).md)
  Sets the background style for picker items of the subscription store view instances within a view.
- [func subscriptionStorePickerItemBackground(some ShapeStyle, in: some Shape) -> some View](../SwiftUI/View/subscriptionStorePickerItemBackground(_:in:).md)
  Sets the background shape and style for subscription store view picker items within a view.
- [func subscriptionStoreButtonLabel(SubscriptionStoreButtonLabel) -> some View](../SwiftUI/View/subscriptionStoreButtonLabel(_:).md)
  Configures subscription store view instances within a view to use the provided button label.
- [struct SubscriptionStoreButtonLabel](subscriptionstorebuttonlabel.md)
  The label of the subscribe button that a subscription store view uses.
### Creating custom subscription store control styles
- [struct SubscriptionStoreButton](subscriptionstorebutton.md)
  A button for subscribing to an in-app subscription with a localized label and optional caption.
- [struct SubscriptionStorePicker](subscriptionstorepicker.md)
  A composite control with a picker for selecting a subscription option and a button for confirming the subscription.
- [struct SubscriptionStorePickerOption](subscriptionstorepickeroption.md)
  A subscription option within a subscription picker control.
### Declaring the structure of a subscription store
- [struct SubscriptionOptionGroup](subscriptionoptiongroup.md)
  A group of subscription options that includes optional views for labels and marketing content.
- [struct SubscriptionOptionGroupSet](subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [struct SubscriptionOptionSection](subscriptionoptionsection.md)
- [protocol StoreContent](storecontent.md)
  A type that represents the content of a store.
- [struct StoreContentBuilder](storecontentbuilder.md)
  A result builder that creates store content from closures that you provide.
### Styling subscription option groups
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some View](../SwiftUI/View/subscriptionStoreOptionGroupStyle(_:).md)
  Sets the style subscription store views within this view use to display groups of subscription options.
- [func subscriptionStoreOptionGroupStyle(some SubscriptionOptionGroupStyle) -> some StoreContent](storecontent/subscriptionstoreoptiongroupstyle(_:).md)
- [protocol SubscriptionOptionGroupStyle](subscriptionoptiongroupstyle.md)
### Adding backgrounds to subscription stores
- [func containerBackground<S>(S, for: ContainerBackgroundPlacement) -> some View](../SwiftUI/View/containerBackground(_:for:).md)
  Sets the container background of the enclosing container using a view.
- [func containerBackground<V>(for: ContainerBackgroundPlacement, alignment: Alignment, content: () -> V) -> some View](../SwiftUI/View/containerBackground(for:alignment:content:).md)
  Sets the container background of the enclosing container using a view.
- [func subscriptionStoreControlBackground(some ShapeStyle) -> some View](../SwiftUI/View/subscriptionStoreControlBackground(_:)-7jxa9.md)
  Set a shape style to use for the background of subscription store view controls within the view.
- [func subscriptionStoreControlBackground(SubscriptionStoreControlBackground) -> some View](../SwiftUI/View/subscriptionStoreControlBackground(_:)-7ev89.md)
  Set a standard effect to use for the background of subscription store view controls within the view.
- [static var subscriptionStore: ContainerBackgroundPlacement](../SwiftUI/ContainerBackgroundPlacement/subscriptionStore.md)
  An automatic placement within a subscription store view, based on the view’s context.
- [static var subscriptionStoreHeader: ContainerBackgroundPlacement](../SwiftUI/ContainerBackgroundPlacement/subscriptionStoreHeader.md)
  A background placement behind the marketing content of a subscription store view.
- [static var subscriptionStoreFullHeight: ContainerBackgroundPlacement](../SwiftUI/ContainerBackgroundPlacement/subscriptionStoreFullHeight.md)
  A background placement that spans the full height of a subscription store view.
- [struct SubscriptionStoreControlBackground](subscriptionstorecontrolbackground.md)
### Configuring accessory buttons
- [func storeButton(Visibility, for: StoreButtonKind...) -> some View](../SwiftUI/View/storeButton(_:for:).md)
  Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [func subscriptionStoreSignInAction((() -> ())?) -> some View](../SwiftUI/View/subscriptionStoreSignInAction(_:).md)
  Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [struct StoreButtonKind](storebuttonkind.md)
  A button to display in a store view or subscription store view.
- [struct SubscriptionOfferViewButtonKind](subscriptionofferviewbuttonkind.md)
### Configuring the subscription store policies
- [func subscriptionStorePolicyDestination(for: SubscriptionStorePolicyKind, destination: () -> some View) -> some View](../SwiftUI/View/subscriptionStorePolicyDestination(for:destination:).md)
  Configures a view as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyDestination(url: URL, for: SubscriptionStorePolicyKind) -> some View](../SwiftUI/View/subscriptionStorePolicyDestination(url:for:).md)
  Configures a URL as the destination for a policy button action in subscription store views.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle) -> some View](../SwiftUI/View/subscriptionStorePolicyForegroundStyle(_:).md)
  Sets the style for the terms of service and privacy policy buttons within a subscription store view.
- [func subscriptionStorePolicyForegroundStyle(some ShapeStyle, some ShapeStyle) -> some View](../SwiftUI/View/subscriptionStorePolicyForegroundStyle(_:_:).md)
  Sets the primary and secondary style for the terms of service and privacy policy buttons within a subscription store view.
- [struct SubscriptionStorePolicyKind](subscriptionstorepolicykind.md)
  The type of policy, such as the terms of service or privacy policies.
### Selecting subscription offers
- [func subscriptionPromotionalOffer(offer: (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View](../SwiftUI/View/subscriptionPromotionalOffer(offer:signature:).md)
  Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.
- [func preferredSubscriptionOffer((Product, Product.SubscriptionInfo, [Product.SubscriptionOffer]) -> Product.SubscriptionOffer?) -> some View](../SwiftUI/View/preferredSubscriptionOffer(_:).md)
  Selects a subscription offer to apply to a purchase that a customer makes from a subscription store view, a store view, or a product view.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](../SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
### Configuring purchase options and product descriptions
- [func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?) -> some View](../SwiftUI/View/inAppPurchaseOptions(_:).md)
  Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [func productDescription(Visibility) -> some View](../SwiftUI/View/productDescription(_:).md)
  Configure the visibility of labels displaying an in-app purchase product description within the view.
### Responding to store events
- [func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View](../SwiftUI/View/onInAppPurchaseStart(perform:).md)
  Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [func onInAppPurchaseCompletion(perform: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View](../SwiftUI/View/onInAppPurchaseCompletion(perform:).md)
  Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
### Loading StoreKit data
- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View](../SwiftUI/View/storeProductTask(for:priority:action:).md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.
- [func storeProductsTask(for: some Collection<String> & Equatable & Sendable, priority: TaskPriority, action: (Product.CollectionTaskState) async -> ()) -> some View](../SwiftUI/View/storeProductsTask(for:priority:action:).md)
  Declares the view as dependent on a collection of In-App Purchase products and returns a modified view.
- [func currentEntitlementTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View](../SwiftUI/View/currentEntitlementTask(for:priority:action:).md)
  Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [func subscriptionStatusTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<[Product.SubscriptionInfo.Status]>) async -> ()) -> some View](../SwiftUI/View/subscriptionStatusTask(for:priority:action:).md)
  Declares the view as dependent on the status of an auto-renewable subscription group, and returns a modified view.
- [Product.CollectionTaskState](product/collectiontaskstate.md)
  The state of a task that loads a collection of products in the background.
- [Product.TaskState](product/taskstate.md)
  The state of a task that loads a product in the background.
- [enum EntitlementTaskState](entitlementtaskstate.md)
  The state of an entitlement task.
### Requesting a refund
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](../SwiftUI/View/refundRequestSheet(for:isPresented:onDismiss:).md)
  Display the refund request sheet for the given transaction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storekit-views)*