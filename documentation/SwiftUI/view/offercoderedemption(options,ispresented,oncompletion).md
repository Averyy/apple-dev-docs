# offerCodeRedemption(options:isPresented:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated
func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: @escaping @MainActor (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View
```

#### Discussion

The [`offerCodeRedemption(options:isPresented:onCompletion:)`](./offercoderedemption%28options,ispresented,oncompletion%29.md) method displays a system sheet where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this method to enable customers to redeem the offer. To display the sheet using UIKit, see `presentOfferCodeRedeemSheet(from:options:)`.

> ❗ **Important**: Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For more information, see [Supporting offer codes in your app](../../StoreKit/supporting-offer-codes-in-your-app.md).

The following code example shows a view that displays the offer code redemption sheet when the customer taps a button:

```swift
import SwiftUI
import StoreKit

struct ContentView: View {
    @State private var redeemSheetIsPresented = false

    var body: some View {
        Button("Present offer code redemption sheet.") {
            redeemSheetIsPresented = true
        }
        .offerCodeRedemption(
            options: [],
            isPresented: $redeemSheetIsPresented
        ) { result in
            // Handle result
        }
    }
}
```

When the customer successfully redeems an offer code, the system delivers the resulting transaction through `onCompletion`, as a `VerificationResult` that wraps the [`Transaction`](../transaction.md).

## Parameters

- `options`: A set of `AppStore/RedeemOption` values that configure the code redemption.
- `isPresented`: A binding to a Boolean value that determines whether the system displays the sheet. You set the Boolean value to `true` to cause the system to display the sheet. The system sets it to `false` when it dismisses the sheet.
- `onCompletion`: A closure the system calls with the result of the redemption. On success, the closure receives a `VerificationResult` containing the [`Transaction`](../transaction.md) that the redemption produces. On failure, it receives the error that caused the redemption to fail.

## See Also

### Interacting with the App Store and Apple Music
- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](./appstoreoverlay%28ispresented,configuration%29.md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](./managesubscriptionssheet%28ispresented%29.md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](./refundrequestsheet%28for,ispresented,ondismiss%29.md)
  Display the refund request sheet for the given transaction.
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
- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View](./storeproducttask%28for,priority,action%29.md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/offercoderedemption(options:ispresented:oncompletion:))*