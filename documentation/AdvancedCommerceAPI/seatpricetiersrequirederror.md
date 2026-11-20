# SeatPriceTiersRequiredError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the request doesn’t include volume price tiers for an item that requires them.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SeatPriceTiersRequiredError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

The [`Change Subscription Price`](./change-subscription-price.md) endpoint and [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md) requests return this error if a request for a subscription item that a customer buys as a multiseat purchase provides a `price` instead of `seatPriceTiers`. A multiseat subscription keeps its tiers, so provide the complete set of tiers in the request.

## Properties

- `errorCode` (number): **Allowed Values**: `4000287`
- `errorMessage` (string): **Allowed Values**: `Invalid request. seatPriceTiers must be provided when the subscription is priced by volume bands.`

## See Also

### Error codes
- [object ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](./acapriceincreaseisnotcurrentlysupportedinindiaerror.md)
- [object AddSeatsMustBeSoleChangeError](./addseatsmustbesolechangeerror.md)
  An error that indicates a request to add seats includes other changes.
- [object AddSeatsRequiresImmediateEffectiveError](./addseatsrequiresimmediateeffectiveerror.md)
  An error that indicates a request to add seats doesn’t take effect immediately.
- [object AlreadyRefundedError](./alreadyrefundederror.md)
- [object AppAppleIdRequiresAppleProductIdError](./appappleidrequiresappleproductiderror.md)
- [object AppTransactionIdNotSupportedError](./apptransactionidnotsupportederror.md)
  An error that indicates the endpoint doesn’t support an app transaction identifier.
- [object AtLeastOneItemError](./atleastoneitemerror.md)
- [object AtLeastOneOfDisplayNameOrDescriptionError](./atleastoneofdisplaynameordescriptionerror.md)
- [object BillingCycleResetWithEffectiveLaterError](./billingcycleresetwitheffectivelatererror.md)
- [object BundleItemAdditionRequiresImmediatelyError](./bundleitemadditionrequiresimmediatelyerror.md)
- [object BundleItemPreviousTransactionIdIsBundleError](./bundleitemprevioustransactionidisbundleerror.md)
- [object BundleItemRemovalRequiresNextBillCycleError](./bundleitemremovalrequiresnextbillcycleerror.md)
- [object BundleItemsOnNonBundleParentError](./bundleitemsonnonbundleparenterror.md)
- [object BundleMigrateNotSupportedError](./bundlemigratenotsupportederror.md)
- [object BundleMigrateSkuMismatchError](./bundlemigrateskumismatcherror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/seatpricetiersrequirederror)*