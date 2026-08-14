# subscriptionIntroductoryOffer(applyOffer:compactJWS:)

**Framework**: SwiftUI  
**Kind**: method

Selects the introductory offer eligibility preference to apply to a purchase a customer makes from a subscription store view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
nonisolated
func subscriptionIntroductoryOffer(applyOffer: @escaping (Product, Product.SubscriptionInfo) -> Bool, compactJWS: @escaping (Product, Product.SubscriptionInfo) async throws -> String) -> some View
```

#### Discussion

Subscription stores within this view uses the introductory subscription offers to configure the appearance of the subscription plans displayed, when you use a system-provided [`SubscriptionStoreControlStyle`](https://developer.apple.com/documentation/storekit/subscriptionstorecontrolstyle) to style the in-app subscription store. Standard [`ProductViewStyle`](https://developer.apple.com/documentation/storekit/productviewstyle) instances don’t show introductory or promotional offers in UI, instead use [`SubscriptionStoreView`](https://developer.apple.com/documentation/storekit/subscriptionstoreview).

Determine if the introductory offer should be displayed in the view and applied to the purchase using the `applyOffer`. If the signature passes validation, the system applies or removes the offer to the purchases according to the offer eligibility preference. If the signature fails validation, the purchase will fail with [`Product.PurchaseError.invalidOfferSignature`](https://developer.apple.com/documentation/storekit/product/purchaseerror/invalidoffersignature).

## Parameters

- `applyOffer`: The system calls this function before drawing the given subscription product on the subscription store view. Return if the introductory offer should be applied to a given product, if any, to have system-provided UI reflect the discounted terms under the selected offer.
- `compactJWS`: The system calls this function before processing a purchase, with the product to be purchased provided as a parameter. Return a compact JWS signature you generate on your server that validates the selected offer eligibility preference. Errors thrown from this closure will be surfaced via the [`onInAppPurchaseCompletion(perform:)`](view/oninapppurchasecompletion(perform:).md) modifier. For information about generating the JWS signature, see [`Generating JWS to sign App Store requests`](https://developer.apple.com/documentation/storekit/generating-jws-to-sign-app-store-requests).

## See Also

- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](view/appstoreoverlay(ispresented:configuration:).md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](view/managesubscriptionssheet(ispresented:).md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](view/refundrequestsheet(for:ispresented:ondismiss:).md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View](view/offercoderedemption(options:ispresented:oncompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
- [func musicPicker(isPresented:title:selection:)](view/musicpicker(ispresented:title:selection:).md)
  Presents a music picker to select items from the Apple Music catalog and the user’s music library.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionintroductoryoffer(applyoffer:compactjws:))*