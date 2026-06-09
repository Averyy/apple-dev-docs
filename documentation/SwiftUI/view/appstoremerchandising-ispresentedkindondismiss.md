# appStoreMerchandising(isPresented:kind:onDismiss:)

**Framework**: SwiftUI  
**Kind**: method

Display a merchandising view.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.2+
- tvOS 26.0+

## Declaration

```swift
nonisolated
func appStoreMerchandising(isPresented: Binding<Bool>, kind: AppStoreMerchandisingKind, onDismiss: ((Result<AppStoreMerchandisingKind.PresentationResult, any Error>) async -> ())? = nil) -> some View
```

## Parameters

- `isPresented`: A binding to a Boolean value that determines whether the App Store merchandising view is presented.
- `kind`: The merchandising kind to merchandise.
- `onDismiss`: The closure to execute when the merchandising view is dismissed, with the presetation result of the App Store merchandising view provided as a parameter.

## See Also

- [func appStoreOverlay(isPresented: Binding<Bool>, configuration: () -> SKOverlay.Configuration) -> some View](view/appstoreoverlay(ispresented:configuration:).md)
  Presents a StoreKit overlay when a given condition is true.
- [func manageSubscriptionsSheet(isPresented: Binding<Bool>) -> some View](view/managesubscriptionssheet(ispresented:).md)
- [func refundRequestSheet(for: Transaction.ID, isPresented: Binding<Bool>, onDismiss: ((Result<Transaction.RefundRequestStatus, Transaction.RefundRequestError>) -> ())?) -> some View](view/refundrequestsheet(for:ispresented:ondismiss:).md)
  Display the refund request sheet for the given transaction.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View](view/offercoderedemption(options:ispresented:oncompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/view/appstoremerchandising(ispresented:kind:ondismiss:))*