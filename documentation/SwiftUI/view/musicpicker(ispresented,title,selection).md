# musicPicker(isPresented:title:selection:)

**Framework**: SwiftUI  
**Kind**: method  
**Role**: Instance Method

Presents a music picker to select items from the Apple Music catalog and the user’s music library.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- visionOS 27.0+

## Declaration

```swift
@MainActor
@preconcurrency func musicPicker<Selection>(isPresented: Binding<Bool>, title: Text? = nil, selection: Binding<MusicItemCollection<Selection>>) -> some View where Selection : PickableMusicItem
```

**Other overloads**:

```swift
@MainActor
@preconcurrency func musicPicker<Selection>(isPresented: Binding<Bool>, title: Text? = nil, selection: Binding<Selection?>) -> some View where Selection : PickableMusicItem
```

```swift
@MainActor
@preconcurrency func musicPicker<Selection>(isPresented: Binding<Bool>, title: Text? = nil, selection: Binding<[Selection]>) -> some View where Selection : PickableMusicItem
```

## Discussion

Example:

```swift
struct MusicPickerButton: View {
    @State private var isShowingMusicPicker = false
    @State private var selectedSongs: MusicItemCollection<Song> = []
    private var title = "Add to Playlist"

    var body: some View {
        Button("Pick one or more songs") {
            isShowingMusicPicker = true
        }
        .musicPicker(
            isPresented: $isShowingMusicPicker,
            title: Text(title), 
            selection: $selectedSongs
        )
        .onChange(of: selectedSongs) { oldValue, newValue in
            let delta = newValue.count - oldValue.count
            print("You selected \(delta) new tracks!")
        }
    }
}
```

## Parameters

- `isPresented`: The binding to whether the music picker should be shown.
- `title`: The title to be shown in the navigation bar.
- `selection`: The selected music items.

## See Also

### Interacting with the App Store and Apple Music
- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](./appstoreoverlay%28ispresented,configuration%29.md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](./managesubscriptionssheet%28ispresented%29.md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](./refundrequestsheet%28for,ispresented,ondismiss%29.md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View](./offercoderedemption%28options,ispresented,oncompletion%29.md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/musicpicker(ispresented:title:selection:))*