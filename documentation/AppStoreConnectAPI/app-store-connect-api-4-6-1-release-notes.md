# App Store Connect API 4.6.1 release notes

**Framework**: App Store Connect API  
**Role**: Article

Update your server-side code to use new features, and test your code against API changes.

## Overview

App Store Connect API version 4.6.1 provides resources that enable you to automate actions you take in App Store Connect.

## Added

- Choose who hosts seat invitations for multiseat purchases. Use the `groupPurchaseInvitationMode` attribute with [`Modify an app`](./patch-v1-apps-_id_.md) to choose whether Apple or your app hosts seat invitations for multiseat purchases on the App Store. For more information, see [Configuring multiseat subscriptions for organizations](./configuring-multi-seat-subscriptions-for-organizations.md).
- Offer lower per-seat prices when people buy more seats. Add up to four additional volume pricing tiers to a price when you create it with [`Create a subscription price change`](./post-v1-subscriptionprices.md), use [`Create a subscription price tier equalization`](./post-v1-subscriptionpricetierequalizations.md) to calculate equivalent tier prices for every territory, and read a subscription’s tiers with [`List subscription price tiers`](./get-v1-subscriptionpricetiers.md), a price’s tiers with [`List additional price tiers for a subscription price`](./get-v1-subscriptionprices-_id_-additionalpricetiers.md), and a price’s tier IDs with [`List additional price tier IDs for a subscription price`](./get-v1-subscriptionprices-_id_-relationships-additionalpricetiers.md). For more information, see [Configuring volume pricing for multiseat subscriptions](./configuring-volume-pricing-for-multi-seat-subscriptions.md). To unpreserve earlier prices after a price with tiers takes effect, see [Unpreserving prices after volume pricing takes effect](./removing-price-preservation-after-volume-pricing-takes-effect.md).
- Check how a price change affects existing subscribers before you schedule it. Use [`Create a subscription price change preview`](./post-v1-subscriptionpricechangepreviews.md) to see how a proposed price, including its tiers, changes the price for existing subscribers in each territory, before you decide whether to set `preserveCurrentPrice` on [`Create a subscription price change`](./post-v1-subscriptionprices.md). For more information, see [Understanding subscription price increase notice and consent](./understanding-price-increase-notice-and-consent.md).
- Declare whether your app lets people share their location with others and whether it offers dating or relationship features. Added the `sharedLocation` and `datingAndRelationships` Boolean attributes to [`AgeRatingDeclaration`](./ageratingdeclaration.md) and [`AgeRatingDeclarationUpdateRequest`](./ageratingdeclarationupdaterequest.md). Set them with [`Modify an age rating declaration`](./patch-v1-ageratingdeclarations-_id_.md). The answers currently affect only the age rating in Brazil.

## See Also

### Versions
- [App Store Connect API 4.6 release notes](./app-store-connect-api-4-6-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.5.1 release notes](./app-store-connect-api-4-5-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.5 release notes](./app-store-connect-api-4-5-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.4.1 release notes](./app-store-connect-api-4-4-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.4 release notes](./app-store-connect-api-4-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.3.1 release notes](./app-store-connect-api-4-3-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.3 release notes](./app-store-connect-api-4-3-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.2 release notes](./app-store-connect-api-4-2-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.1 release notes](./app-store-connect-api-4-1-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 4.0 release notes](./app-store-connect-api-4-0-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.8 release notes](./app-store-connect-api-3-8-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.7 release notes](./app-store-connect-api-3-7-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.6 release notes](./app-store-connect-api-3-6-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.5 release notes](./app-store-connect-api-3-5-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.
- [App Store Connect API 3.4 release notes](./app-store-connect-api-3-4-release-notes.md)
  Update your server-side code to use new features, and test your code against API changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/app-store-connect-api-4-6-1-release-notes)*