# offerCodeRedemption(options:isPresented:onCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: @escaping @MainActor (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View
```

#### Discussion

The [`offerCodeRedemption(options:isPresented:onCompletion:)`](view/offercoderedemption(options:ispresented:oncompletion:).md) method displays a system sheet where customers can enter and redeem offer codes. If you generate offer codes in App Store Connect, call this method to enable customers to redeem the offer. To display the sheet using UIKit, see `presentOfferCodeRedeemSheet(from:options:)`.

> ❗ **Important**: Set up offer codes in App Store Connect before calling this API. Customers can only redeem these offers in your app through the redemption sheet; don’t use a custom UI. For more information, see [`Supporting offer codes in your app`](https://developer.apple.com/documentation/StoreKit/supporting-offer-codes-in-your-app).

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

When the customer successfully redeems an offer code, the system delivers the resulting transaction through `onCompletion`, as a `VerificationResult` that wraps the [`Transaction`](transaction.md).

## Parameters

- `options`: A set of `AppStore/RedeemOption` values that configure the code redemption.
- `isPresented`: A binding to a Boolean value that determines whether the system displays the sheet. You set the Boolean value to `true` to cause the system to display the sheet. The system sets it to `false` when it dismisses the sheet.
- `onCompletion`: A closure the system calls with the result of the redemption. On success, the closure receives a `VerificationResult` containing the [`Transaction`](transaction.md) that the redemption produces. On failure, it receives the error that caused the redemption to fail.

## See Also

- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](view/appstoreoverlay(ispresented:configuration:).md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](view/managesubscriptionssheet(ispresented:).md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](view/refundrequestsheet(for:ispresented:ondismiss:).md)
  Display the refund request sheet for the given transaction.
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
- [func storeProductTask(for: Product.ID, priority: TaskPriority, action: (Product.TaskState) async -> ()) -> some View](view/storeproducttask(for:priority:action:).md)
  Declares the view as dependent on an In-App Purchase product and returns a modified view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/offercoderedemption(options:ispresented:oncompletion:))*