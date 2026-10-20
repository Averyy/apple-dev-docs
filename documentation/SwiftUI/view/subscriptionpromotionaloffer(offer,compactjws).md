# subscriptionPromotionalOffer(offer:compactJWS:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Selects a promotional offer to apply to a purchase a customer makes from a subscription store view.

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
func subscriptionPromotionalOffer(offer: @escaping (Product, Product.SubscriptionInfo) -> Product.SubscriptionOffer?, compactJWS: @escaping (Product, Product.SubscriptionInfo, Product.SubscriptionOffer) async throws -> String) -> some View
```

#### Discussion

Subscription stores within this view uses the specified subscription offer to configure the appearance of the subscription plans displayed, when you use a system-provided [`SubscriptionStoreControlStyle`](../../StoreKit/subscriptionstorecontrolstyle.md) to style the in-app subscription store. Standard [`ProductViewStyle`](../../StoreKit/productviewstyle.md) instances don’t show introductory or promotional offers in UI. Use the [`SubscriptionStoreView`](../../StoreKit/subscriptionstoreview.md) instead to show these offers in the UI.

If the signature passes validation for the offer you select, the system applies the offer to the purchase. If the signature fails validation for the offer you select, the purchase fails with [`Product.PurchaseError.invalidOfferSignature`](../../StoreKit/product/purchaseerror/invalidoffersignature.md).

Promotional offers you select in this modifier overwrite any offers you specified in ancestor views.

## Parameters

- `offer`: The system calls this function before drawing the given subscription product on the subscription store view. Return the promotional offer to apply to the product, if any, to have system-provided UI reflect the discounted terms under the selected offer.
- `compactJWS`: The system calls this function before processing a purchase, with the product to be purchased provided as a parameter, along with the selected subscription offer to be applied to the purchase. Return a compact JWS signature you generate on your server that validates the selected offer. Errors thrown from this closure will be surfaced via the [`onInAppPurchaseCompletion(perform:)`](./oninapppurchasecompletion%28perform%29.md) modifier. For information about generating the JWS signature, see [Generating JWS to sign App Store requests](../../StoreKit/generating-jws-to-sign-app-store-requests.md)..

## See Also

### Interacting with the App Store and Apple Music
- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](./appstoreoverlay%28ispresented,configuration%29.md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](./managesubscriptionssheet%28ispresented%29.md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](./refundrequestsheet%28for,ispresented,ondismiss%29.md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View](./offercoderedemption%28options,ispresented,oncompletion%29.md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
- [func musicPicker(isPresented:title:selection:)](./musicpicker%28ispresented,title,selection%29.md)
  Presents a music picker to select items from the Apple Music catalog and the user’s music library.
- [func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options, onLoadCompletion: ((any Error)?) -> Void) -> some View](./musicsubscriptionoffer%28ispresented,options,onloadcompletion%29.md)
  Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.
- [func currentEntitlementTask(for: String, priority: TaskPriority, action: (EntitlementTaskState<VerificationResult<Transaction>?>) async -> ()) -> some View](./currententitlementtask%28for,priority,action%29.md)
  Declares the view as dependent on the entitlement of an In-App Purchase product, and returns a modified view.
- [func inAppPurchaseOptions(((Product) async -> Set<Product.PurchaseOption>)?) -> some View](./inapppurchaseoptions%28_%29.md)
  Add a function to call before initiating a purchase from StoreKit view within this view, providing a set of options for the purchase.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>, subscriptionGroupID: String) -> some View](./managesubscriptionssheet%28ispresented,subscriptiongroupid%29.md)
- [func onInAppPurchaseCompletion(perform: ((Product, Result<Product.PurchaseResult, any Error>) async -> ())?) -> some View](./oninapppurchasecompletion%28perform%29.md)
  Add an action to perform when a purchase initiated from a StoreKit view within this view completes.
- [func onInAppPurchaseStart(perform: ((Product) async -> ())?) -> some View](./oninapppurchasestart%28perform%29.md)
  Add an action to perform when a user triggers the purchase button on a StoreKit view within this view.
- [func productIconBorder() -> some View](./producticonborder%28%29.md)
  Adds a standard border to an in-app purchase product’s icon .
- [func productViewStyle(some ProductViewStyle) -> some View](./productviewstyle%28_%29.md)
  Sets the style for In-App Purchase product views within a view.
- [func productDescription(Visibility) -> some View](./productdescription%28_%29.md)
  Configure the visibility of labels displaying an in-app purchase product description within the view.
- [func storeButton(Visibility, for: StoreButtonKind...) -> some View](./storebutton%28_,for%29.md)
  Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionpromotionaloffer(offer:compactjws:))*