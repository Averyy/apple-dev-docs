# Advanced Commerce API changelog

**Framework**: Advanced Commerce API  
**Role**: Article

Learn about new features and updates in the Advanced Commerce API.

## Overview

Use this changelog to learn about feature updates, deprecations, and removals for the Advanced Commerce API.

## 1.3 – November 17, 2026

- Added V2 of the following requests:  [`OneTimeChargeCreateRequest`](./onetimechargecreaterequest.md), [`SubscriptionCreateRequest`](./subscriptioncreaterequest.md), [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md), [`SubscriptionReactivateInAppRequest`](./subscriptionreactivateinapprequest.md), [`Change Subscription Price`](./change-subscription-price.md), [`Change Subscription Metadata`](./change-subscription-metadata.md), [`Migrate a Subscription to Advanced Commerce API`](./migrate-subscription-to-advanced-commerce-api.md) and [`Request Transaction Refund`](./request-transaction-refund.md).
- Added [`SeatPriceTier`](./seatpricetier.md), and added `seatPriceTiers` and [`finalQuantity`](./finalquantity.md) to [`SubscriptionCreateItem`](./subscriptioncreateitem.md) and [`SubscriptionModifyChangeItem`](./subscriptionmodifychangeitem.md), `seatPriceTiers` to [`SubscriptionPriceChangeItem`](./subscriptionpricechangeitem.md), and [`revokeSeatQuantity`](./revokeseatquantity.md) to [`SubscriptionRevokeRequest`](./subscriptionrevokerequest.md), to support multiseat purchases. For more information, see [Creating multiseat purchases](./creating-multiseat-purchases.md).
- Added the following error codes: [`TooManySeatPriceTiersError`](./toomanyseatpricetierserror.md), [`InvalidMaximumSeatQuantityError`](./invalidmaximumseatquantityerror.md), [`SeatPriceTiersNotDecreasingError`](./seatpricetiersnotdecreasingerror.md), [`SeatPriceTiersNotAllowedForBundleError`](./seatpricetiersnotallowedforbundleerror.md), [`PriceNotAllowedWithSeatPriceTiersError`](./pricenotallowedwithseatpricetierserror.md), [`FinalQuantityAndSeatPriceTiersNotPairedError`](./finalquantityandseatpricetiersnotpairederror.md), [`InvalidFinalQuantityError`](./invalidfinalquantityerror.md), [`SeatDecreaseNotAllowedError`](./seatdecreasenotallowederror.md), [`AddSeatsMustBeSoleChangeError`](./addseatsmustbesolechangeerror.md), [`AddSeatsRequiresImmediateEffectiveError`](./addseatsrequiresimmediateeffectiveerror.md), [`SeatPriceTiersRequiredError`](./seatpricetiersrequirederror.md), [`CustomRefundWithRevokeNotAllowedForMultiSeatSubscriptionError`](./customrefundwithrevokenotallowedformultiseatsubscriptionerror.md), [`InvalidRevokeSeatQuantityError`](./invalidrevokeseatquantityerror.md), [`RevokeSeatQuantityRequiresMultiSeatSubscriptionError`](./revokeseatquantityrequiresmultiseatsubscriptionerror.md), and [`SubsForGroupsRequiresLatestVersionError`](./subsforgroupsrequireslatestversionerror.md).

## Server update – April 22, 2026

- For subscribers in South Korea, if the price increase meets the criteria that requires communication with the customer, the App Store notifies subscribers via email, price increase sheet, and push notification. Previously, developers needed to implement the price-increase communications for South Korea. For more information, see [Handling subscription price changes](./handling-subscription-price-changes.md).

## Server update – March 26, 2026

- Added the following error code: [`MigrationNotAllowedWhenPriceIncreaseCommunicatedError`](./migrationnotallowedwhenpriceincreasecommunicatederror.md).

## Server update — March 5, 2026

- Added additional tax codes for books in [Choosing tax codes for your SKUs](./taxcodes.md).

## Server update – January 23, 2026

- Added the following error codes: [`InvalidProratedPriceForChangeItemWithEffectiveLaterError`](./invalidproratedpriceforchangeitemwitheffectivelatererror.md) and [`FreeTrialOfferMustUsePeriodCountOfOneError`](./freetrialoffermustuseperiodcountofoneerror.md).

## 1.2 – December 10, 2025

- Added the `dependentSKUs` field to the [`Change Subscription Price`](./change-subscription-price.md) endpoint payload for managing subscription price changes. For more information, see [Handling subscription price changes](./handling-subscription-price-changes.md).
- Added the following error codes: [`ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError`](./acapriceincreaseisnotcurrentlysupportedinindiaerror.md), [`DependentSKUsCannotBeChainedError`](./dependentskuscannotbechainederror.md), [`DependentSKUsCannotBeSharedError`](./dependentskuscannotbesharederror.md), [`InvalidPriceForChangeItemInPriceIncreaseError`](./invalidpriceforchangeiteminpriceincreaseerror.md), [`InvalidSKUProvidedMustBeCurrentSKUSetToRenewError`](./invalidskuprovidedmustbecurrentskusettorenewerror.md), [`ItemCannotBeSpecifiedMultipleTimesError`](./itemcannotbespecifiedmultipletimeserror.md), and [`PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError`](./pricechangecannotbeissuedwhenalreadycommunicatederror.md).

## Server update - November 13, 2025

- Added support for the [Mini Apps Partner Program](https://developer.apple.com/programs/mini-apps-partner/).

## Server update — July 2, 2025

- Added tax codes for games in [Choosing tax codes for your SKUs](./taxcodes.md).

## Server update – May 5, 2025

- Added the error code [`TransactionCannotBeRefundedContactSupportError`](./transactioncannotberefundedcontactsupporterror.md).
- Removed the unused error code `TransactionNotFoundError`.

## 1.1 — March 24, 2025

- Added the endpoints [`Change Subscription Metadata`](./change-subscription-metadata.md), [`Migrate a Subscription to Advanced Commerce API`](./migrate-subscription-to-advanced-commerce-api.md), [`Request Transaction Refund`](./request-transaction-refund.md), and [`Revoke Subscription`](./revoke-subscription.md), and the related data types and error codes.

## 1.0 — January 23, 2025

- Initial release.

## See Also

### Essentials
- [Setting up your project for Advanced Commerce API](./setting-up-your-project-for-advanced-commerce.md)
  Configure your app in App Store Connect, set up your server, and prepare your SKUs.
- [Setting up a link to manage subscriptions](./setupmanagesubscriptions.md)
  Create a deep link to a subscription-management page for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/changelog)*