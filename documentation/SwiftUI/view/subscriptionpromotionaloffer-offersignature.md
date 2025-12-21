# subscriptionPromotionalOffer(offer:signature:)

**Framework**: SwiftUI  
**Kind**: method

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+
- macOS 14.4+
- tvOS 17.4+
- visionOS 1.1+
- watchOS 10.4+

## Declaration

```swift
nonisolated
func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, signature: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> Product.SubscriptionOffer.Signature) -> some View
```

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:signature:))*