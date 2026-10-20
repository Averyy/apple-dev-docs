# StoreButtonKind

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

A button to display in a store view or subscription store view.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct StoreButtonKind
```

#### Overview

Use the [`storeButton(_:for:)`](../SwiftUI/view/storebutton%28_,for%29.md) modifier on a view to set the visibility of the buttons.

## Topics

### Getting button types for store views
- [static var cancellation: StoreButtonKind](./storebuttonkind/cancellation.md)
  A type of button that people use to dismiss the current store presentation.
- [static var restorePurchases: StoreButtonKind](./storebuttonkind/restorepurchases.md)
  A type of button that people use to restore purchases.
### Getting additional button types for subscription store views
- [static var signIn: StoreButtonKind](./storebuttonkind/signin.md)
  A type of button that people use to sign in.
- [static var redeemCode: StoreButtonKind](./storebuttonkind/redeemcode.md)
  A type of button that people use to redeem an offer code.
- [static var policies: StoreButtonKind](./storebuttonkind/policies.md)
  A type of button that people use to display store policies.

## See Also

### Configuring accessory buttons
- [func storeButton(Visibility, for: StoreButtonKind...) -> some View
](../SwiftUI/view/storebutton%28_,for%29.md)
  Specifies the visibility of auxiliary buttons that store view and subscription store view instances may use.
- [func subscriptionStoreSignInAction((() -> ())?) -> some View
](../SwiftUI/view/subscriptionstoresigninaction%28_%29.md)
  Adds an action to perform when a person uses the sign-in button on a subscription store view within a view.
- [struct SubscriptionOfferViewButtonKind](./subscriptionofferviewbuttonkind.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storebuttonkind)*