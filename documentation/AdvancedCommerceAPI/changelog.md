# Advanced Commerce API changelog

**Framework**: Advanced Commerce API

Learn about new features and updates in the Advanced Commerce API.

#### Overview

Use this changelog to learn about feature updates, deprecations, and removals for the Advanced Commerce API.

#### 12 December 10 2025

- Added the `dependentSKUs` field to the [`Change Subscription Price`](change-subscription-price.md) endpoint payload for managing subscription price changes. For more information, see [`Handling subscription price changes`](handling-subscription-price-changes.md).
- Added the following error codes: [`ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError`](acapriceincreaseisnotcurrentlysupportedinindiaerror.md), [`DependentSKUsCannotBeChainedError`](dependentskuscannotbechainederror.md), [`DependentSKUsCannotBeSharedError`](dependentskuscannotbesharederror.md), [`InvalidPriceForChangeItemInPriceIncreaseError`](invalidpriceforchangeiteminpriceincreaseerror.md), [`InvalidSKUProvidedMustBeCurrentSKUSetToRenewError`](invalidskuprovidedmustbecurrentskusettorenewerror.md), [`ItemCannotBeSpecifiedMultipleTimesError`](itemcannotbespecifiedmultipletimeserror.md), and [`PriceChangeCannotBeIssuedWhenAlreadyCommunicatedError`](pricechangecannotbeissuedwhenalreadycommunicatederror.md).

#### Server Update November 13 2025

Added support for the [`Mini Apps Partner Program`](https://developer.apple.comhttps://developer.apple.com/programs/mini-apps-partner/).

#### Server Update July 2 2025

Added tax codes for games in [`Choosing tax codes for your SKUs`](taxcodes.md).

#### Server Update May 5 2025

- Added the error code [`TransactionCannotBeRefundedContactSupportError`](transactioncannotberefundedcontactsupporterror.md).
- Removed the unused error code `TransactionNotFoundError`.

#### 11 March 24 2025

Added the endpoints [`Change Subscription Metadata`](change-subscription-metadata.md), [`Migrate a Subscription to Advanced Commerce API`](migrate-subscription-to-advanced-commerce-api.md), [`Request Transaction Refund`](request-transaction-refund.md), and [`Revoke Subscription`](revoke-subscription.md), and the related data types and error codes.

#### 10 January 23 2025

Initial release.

## See Also

- [Setting up your project for Advanced Commerce API](setting-up-your-project-for-advanced-commerce.md)
  Configure your app in App Store Connect, set up your server, and prepare your SKUs.
- [Setting up a link to manage subscriptions](setupmanagesubscriptions.md)
  Create a deep link to a subscription-management page for your app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/changelog)*