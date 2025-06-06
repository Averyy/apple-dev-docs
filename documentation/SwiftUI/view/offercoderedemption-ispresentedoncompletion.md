# offerCodeRedemption(isPresented:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
nonisolated
func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: @escaping @MainActor (Result<Void, any Error>) -> Void = { _ in }) -> some View
```

#### Discussion

The [`offerCodeRedemption(isPresented:onCompletion:)`](view/offercoderedemption(ispresented:oncompletion:).md) method displays a system sheet where customers can enter and redeem subscription offer codes. If you generate subscription offer codes in App Store Connect, call this function to enable users to redeem the offer. To display the sheet using UIKit, see `presentOfferCodeRedeemSheet(in:)`.

> ❗ **Important**: Set up subscription offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For more information, see [`Supporting subscription offer codes in your app`](https://developer.apple.com/documentation/StoreKit/supporting-subscription-offer-codes-in-your-app).

Set up subscription offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For more information, see [`Supporting subscription offer codes in your app`](https://developer.apple.com/documentation/StoreKit/supporting-subscription-offer-codes-in-your-app).

The following code example shows a view that displays the offer code redemption sheet upon a button press:

```swift
import SwiftUI
import StoreKit

struct ContentView: View {
    @State private var redeemSheetIsPresented = false

    var body: some View {
        Button("Present offer code redemption sheet.") {
            redeemSheetIsPresented = true
        }
        .offerCodeRedemption(isPresented: $redeemSheetIsPresented) { result in
            // Handle result
        }
    }
}
```

When customers redeem an offer code, StoreKit emits the resulting transaction in [`updates`](https://developer.apple.com/documentation/StoreKit/Transaction/updates). Set up a transaction listener as soon as your app launches to receive new transactions while the app is running.

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether the system   displays the sheet. You set the Boolean value to true to cause the   system to display the sheet. The system sets it to false when it   dismisses the sheet.
- `onCompletion`: A closure that returns the result of the presentation.   In Mac apps built with Mac Catalyst, the completion handler returns   a failure with an error prior to macOS 15.

## See Also

- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](view/appstoreoverlay(ispresented:configuration:).md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](view/managesubscriptionssheet(ispresented:).md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](view/refundrequestsheet(for:ispresented:ondismiss:).md)
  Display the refund request sheet for the given transaction.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/offercoderedemption(ispresented:oncompletion:))*