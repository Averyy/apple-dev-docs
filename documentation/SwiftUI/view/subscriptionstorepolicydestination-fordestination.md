# subscriptionStorePolicyDestination(for:destination:)

**Framework**: SwiftUI  
**Kind**: method

Configures a view as the destination for a policy button action in subscription store views.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
nonisolated
func subscriptionStorePolicyDestination(for button: SubscriptionStorePolicyKind, @ViewBuilder destination: () -> some View) -> some View
```

#### Discussion

Except on tvOS, you can also set a URL as the destination using [`subscriptionStorePolicyDestination(url:for:)`](view/subscriptionstorepolicydestination(url:for:).md). If you do not set a destination, the system will use the automatic behavior. Check the documentation for the value you provide for `button` to understand the automatic behavior.

By default, the subscription store shows the terms of service & privacy policy buttons if you set a destination for at least one policy. The policy that is not explicitly set will use the automatic behavior. You can override this behavior using the [`storeButton(_:for:)`](view/storebutton(_:for:).md) modifier, with [`policies`](https://developer.apple.com/documentation/StoreKit/StoreButtonKind/policies) as the second parameter.

## Parameters

- `button`: The policy button to associate the URL with.
- `destination`: The view to present when someone chooses to view the policy.

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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/subscriptionstorepolicydestination(for:destination:))*