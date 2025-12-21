# AppStore

**Framework**: StoreKit  
**Kind**: enum

Interactions with the App Store, such as managing subscriptions, verifying devices, authorizing payments, synchronizing transactions, getting the environment, and more.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum AppStore
```

#### Overview

Use these static functions and variables to perform tasks like showing the manage subscriptions sheet, getting the device verification ID, determining whether users can make purchases, and more.

## Topics

### Checking the environment
- [AppStore.Environment](appstore/environment.md)
  Constants that represent the App Store server environment.
### Checking payment setup
- [static var canMakePayments: Bool](appstore/canmakepayments.md)
  A Boolean value that indicates whether the person can make purchases.
### Checking current age rating
- [static var ageRatingCode: Int?](appstore/ageratingcode.md)
  The current age rating code for your app.
### Verifying devices
- [static var deviceVerificationID: UUID?](appstore/deviceverificationid.md)
  The device verification identifier to use to verify whether signed information is valid for the current device.
### Getting the platform
- [AppStore.Platform](appstore/platform.md)
  Values that represent Apple platforms.
### Managing subscriptions
- [static func showManageSubscriptions(in: UIWindowScene) async throws](appstore/showmanagesubscriptions(in:).md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(in: UIWindowScene, subscriptionGroupID: String) async throws](appstore/showmanagesubscriptions(in:subscriptiongroupid:).md)
  Presents the App Store sheet for managing subscriptions for a subscription group.
### Requesting reviews
- [struct RequestReviewAction](requestreviewaction.md)
  An instance that tells StoreKit to request an App Store rating or review, if appropriate.
- [static func requestReview(in: UIWindowScene)](appstore/requestreview(in:)-1q8qs.md)
  Tells StoreKit to request an App Store rating or review from the user, if appropriate, using the specified scene.
- [static func requestReview(in: NSViewController)](appstore/requestreview(in:)-4r0y9.md)
  Tells StoreKit to request an App Store rating or review from the user, if appropriate, using the specified view controller.
### Presenting the offer code redemption sheet
- [Supporting offer codes in your app](supporting-offer-codes-in-your-app.md)
  Enable customers to redeem offer codes through the App Store or within your app.
- [static func presentOfferCodeRedeemSheet(in: UIWindowScene) async throws](appstore/presentoffercoderedeemsheet(in:).md)
  Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View](../SwiftUI/View/offerCodeRedemption(isPresented:onCompletion:).md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
- [static func presentOfferCodeRedeemSheet(from: NSViewController) async throws](appstore/presentoffercoderedeemsheet(from:).md)
  Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect.
### Restoring purchases
- [static func sync() async throws](appstore/sync.md)
  Synchronizes your app’s transaction information and subscription status with information from the App Store.
### Merchandising
- [struct AppStoreMerchandisingKind](appstoremerchandisingkind.md)
### Type Methods
- [static func presentMerchandising(AppStoreMerchandisingKind, from: NSWindow) async throws -> AppStoreMerchandisingKind.PresentationResult](appstore/presentmerchandising(_:from:)-8bblo.md)
- [static func presentMerchandising(AppStoreMerchandisingKind, from: UIViewController) async throws -> AppStoreMerchandisingKind.PresentationResult](appstore/presentmerchandising(_:from:)-hkrd.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AppTransaction](apptransaction.md)
  Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore)*