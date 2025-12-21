# musicSubscriptionOffer(isPresented:options:onLoadCompletion:)

**Framework**: SwiftUI  
**Kind**: method

Initiates the process of presenting a sheet with subscription offers for Apple Music when the `isPresented` binding is `true`.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+

## Declaration

```swift
nonisolated
func musicSubscriptionOffer(isPresented: Binding<Bool>, options: MusicSubscriptionOffer.Options = .default, onLoadCompletion: @escaping ((any Error)?) -> Void = { _ in }) -> some View
```

#### Discussion

The example below displays a simple button that the user can activate to begin presenting subscription offers for Apple Music. The action handler of this button initiates the presentation of those offers by setting the `isShowingOffer` variable to `true`.

```swift
struct MusicSubscriptionOfferButton: View {
    @State var isShowingOffer = false
    var body: some View {
        Button("Apple Music Subscription Offer") {
            isShowingOffer = true
        }
        .musicSubscriptionOffer(isPresented: $isShowingOffer)
    }
}
```

You can also configure the Apple Music subscription offer by creating an instance of `MusicSubscriptionOffer.Options`, setting relevant properties on it, and passing it to `.musicSubscriptionOffer(…)`. For example, to present contextual offers that highlight a specific album, you can configure the subscription offer like the following:

```swift
struct MusicSubscriptionOfferButton: View {
    var album: Album
    @State var isShowingOffer = false
    @State var offerOptions = MusicSubscriptionOffer.Options(
        affiliateToken: "<affiliate_token>", 
        campaignToken: "<campaign_token>"
    )

    var body: some View {
        Button("Apple Music Subscription Offer") {
            offerOptions.itemID = album.id
            isShowingOffer = true
        }
        .musicSubscriptionOffer(
            isPresented: $isShowingOffer, 
            options: offerOptions
        )
    }
}
```

The initial value of `offerOptions` includes relevant tokens (affiliate and campaign tokens) that allow you to receive compensation for referring new Apple Music subscribers. For more information, see this presentation of the [`Apple Services Performance Partners Program`](https://developer.apple.comhttps://affiliate.itunes.apple.com/resources/).

You may also set `isShowingOffer` to `false` to programmatically dismiss the subscription offer (or to abort its loading process).

## Parameters

- `isPresented`: A binding to a Boolean value that you can set to    to show a sheet with subscription offers for Apple Music.
- `options`: Options to use for loading the subscription offer for   Apple Music.
- `onLoadCompletion`: The function to call upon completing the initial   loading process for this subscription offer. The subscription   offer UI becomes visible when it calls this function with the   error argument as  . If there is an error in the   loading process, the subscription offer calls this function with   a non-  error, and it resets the   binding   to  .

## See Also

- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](view/appstoreoverlay(ispresented:configuration:).md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](view/managesubscriptionssheet(ispresented:).md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](view/refundrequestsheet(for:ispresented:ondismiss:).md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](view/offercoderedemption(ispresented:oncompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/musicsubscriptionoffer(ispresented:options:onloadcompletion:))*