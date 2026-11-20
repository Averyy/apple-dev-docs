# FinalQuantityAndSeatPriceTiersNotPairedError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the request includes a final quantity or volume price tiers without the other.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object FinalQuantityAndSeatPriceTiersNotPairedError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

A request returns this error if a [`SubscriptionCreateItem`](./subscriptioncreateitem.md) or [`SubscriptionModifyChangeItem`](./subscriptionmodifychangeitem.md) includes a [`finalQuantity`](./finalquantity.md) without `seatPriceTiers`, or `seatPriceTiers` without a `finalQuantity`. Provide both values together.

## Properties

- `errorCode` (number): **Allowed Values**: `4000279`
- `errorMessage` (string): **Allowed Values**: `Invalid request. finalQuantity and seatPriceTiers must be provided together.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/finalquantityandseatpricetiersnotpairederror)*