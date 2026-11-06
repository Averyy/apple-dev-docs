# AppStore

**Framework**: StoreKit  
**Kind**: enum  
**Role**: Enumeration

Interactions with the App Store, such as managing subscriptions, verifying devices, authorizing payments, synchronizing transactions, getting the environment, and more.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
enum AppStore
```

## Overview

Use these static functions and variables to perform tasks like showing the manage subscriptions sheet, getting the device verification ID, determining whether users can make purchases, and more.

## Topics

### Checking the environment
- [AppStore.Environment](./appstore/environment.md)
  Constants that represent the App Store server environment.
### Checking payment setup
- [static var canMakePayments: Bool](./appstore/canmakepayments.md)
  A Boolean value that indicates whether the person can make purchases.
### Checking current age rating
- [static var ageRatingCode: Int?](./appstore/ageratingcode.md)
  The current age rating code for your app.
### Verifying devices
- [static var deviceVerificationID: UUID?](./appstore/deviceverificationid.md)
  The device verification identifier to use to verify whether signed information is valid for the current device.
### Getting the platform
- [AppStore.Platform](./appstore/platform.md)
  Values that represent Apple platforms.
### Managing subscriptions
- [static func showManageSubscriptions(in: UIWindowScene) async throws](./appstore/showmanagesubscriptions%28in%29.md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(in: UIWindowScene, subscriptionGroupID: String) async throws](./appstore/showmanagesubscriptions%28in,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.
- [static func showManageSubscriptions(from: NSWindow) async throws](./appstore/showmanagesubscriptions%28from%29.md)
  Presents the App Store sheet for managing subscriptions.
- [static func showManageSubscriptions(from: NSWindow, subscriptionGroupID: String) async throws](./appstore/showmanagesubscriptions%28from,subscriptiongroupid%29.md)
  Presents the App Store sheet for managing subscriptions for a subscription group.
### Inviting people to a group
- [static func presentMultiSeatInvitationSheet(from: UIViewController, subscriptionGroupID: String) async throws](./appstore/presentmultiseatinvitationsheet%28from,subscriptiongroupid%29-5cmtd.md)
  Presents the invitation sheet that the group purchaser uses to invite people to join a multiseat subscription.
- [static func presentMultiSeatInvitationSheet(from: NSWindow, subscriptionGroupID: String) async throws](./appstore/presentmultiseatinvitationsheet%28from,subscriptiongroupid%29-ni0z.md)
  Presents the invitation sheet that the group purchaser uses to invite people to join a multiseat subscription.
- [func multiSeatInvitationSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../SwiftUI/view/multiseatinvitationsheet%28ispresented,subscriptiongroupid,oncompletion%29.md)
  Presents the Apple-owned multi-seat invitation sheet, allowing the subscriber to invite others to join their multi-seat subscription.
### Requesting data sharing consent
- [static func presentMultiSeatDataSharingConsentSheet(from: UIViewController, subscriptionGroupID: String) async throws](./appstore/presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-9gr5s.md)
  Presents the sheet in which the group purchaser decides whether to share group information with you.
- [static func presentMultiSeatDataSharingConsentSheet(from: NSWindow, subscriptionGroupID: String) async throws](./appstore/presentmultiseatdatasharingconsentsheet%28from,subscriptiongroupid%29-3j1t4.md)
  Presents the sheet in which the group purchaser decides whether to share group information with you.
- [var multiSeatDataSharingConsentEligibility: Product.SubscriptionInfo.MultiSeatDataSharingConsentEligibility](./product/subscriptioninfo/multiseatdatasharingconsenteligibility-swift.property.md)
  A value that indicates whether you can request consent to share group information for this subscription’s subscription group.
- [func multiSeatDataSharingConsentSheet(isPresented: Binding<Bool>, subscriptionGroupID: String, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../SwiftUI/view/multiseatdatasharingconsentsheet%28ispresented,subscriptiongroupid,oncompletion%29.md)
  Presents the data sharing consent sheet, where a subscriber decides whether to share account-level data with you.
### Requesting reviews
- [struct RequestReviewAction](./requestreviewaction.md)
  An instance that tells StoreKit to request an App Store rating or review, if appropriate.
- [static func requestReview(in: UIWindowScene)](./appstore/requestreview%28in%29-1q8qs.md)
  Tells StoreKit to request an App Store rating or review from the user, if appropriate, using the specified scene.
- [static func requestReview(in: NSViewController)](./appstore/requestreview%28in%29-4r0y9.md)
  Tells StoreKit to request an App Store rating or review from the user, if appropriate, using the specified view controller.
### Presenting the offer code redemption sheet
- [Supporting offer codes in your app](./supporting-offer-codes-in-your-app.md)
  Enable customers to redeem offer codes through the App Store or within your app.
- [static func presentOfferCodeRedeemSheet(from: UIViewController, options: Set<RedeemOption>) async throws -> VerificationResult<Transaction>](./appstore/presentoffercoderedeemsheet%28from,options%29-89agc.md)
  Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.
- [func offerCodeRedemption(options: Set<RedeemOption>, isPresented: Binding<Bool>, onCompletion: (Result<VerificationResult<Transaction>, any Error>) -> Void) -> some View
](../SwiftUI/view/offercoderedemption%28options,ispresented,oncompletion%29.md)
  Presents a sheet that enables customers to redeem offer codes that you configure in App Store Connect.
### Restoring purchases
- [static func sync() async throws](./appstore/sync%28%29.md)
  Synchronizes your app’s transaction information and subscription status with information from the App Store.
### Merchandising
- [struct AppStoreMerchandisingKind](./appstoremerchandisingkind.md)
### Deprecated
- [static func presentOfferCodeRedeemSheet(in: UIWindowScene) async throws](./appstore/presentoffercoderedeemsheet%28in%29.md)
  Displays a sheet in the window scene that enables customers to redeem an offer code that you configure in App Store Connect.
- [func offerCodeRedemption(isPresented: Binding<Bool>, onCompletion: (Result<Void, any Error>) -> Void) -> some View
](../SwiftUI/view/offercoderedemption%28ispresented,oncompletion%29.md)
- [static func presentOfferCodeRedeemSheet(from: NSViewController) async throws](./appstore/presentoffercoderedeemsheet%28from%29.md)
  Displays a sheet in the view that enables customers to redeem an offer code that you configure in App Store Connect.
### Type Methods
- [static func presentMerchandising(AppStoreMerchandisingKind, from: NSWindow) async throws -> AppStoreMerchandisingKind.PresentationResult](./appstore/presentmerchandising%28_,from%29-8bblo.md)
  Display a merchandising view.
- [static func presentMerchandising(AppStoreMerchandisingKind, from: UIViewController) async throws -> AppStoreMerchandisingKind.PresentationResult](./appstore/presentmerchandising%28_,from%29-hkrd.md)
  Display a merchandising view.
- [static func presentOfferCodeRedeemSheet(from: NSWindow, options: Set<RedeemOption>) async throws -> VerificationResult<Transaction>](./appstore/presentoffercoderedeemsheet%28from,options%29-gj8m.md)
  Presents a sheet that enables users to redeem subscription offer codes that you configure in App Store Connect.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### App Store interactions
- [struct AppTransaction](./apptransaction.md)
  Information that represents the customer’s purchase of the app, cryptographically signed by the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/appstore)*