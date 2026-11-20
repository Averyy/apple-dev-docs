# SeatPriceTiersNotAllowedForBundleError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the request includes volume price tiers for a bundle.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SeatPriceTiersNotAllowedForBundleError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

A request returns this error if it includes `seatPriceTiers` for a bundle or a suite. You can use `seatPriceTiers` only for a subscription that contains a single item with no `bundleItems`.

## Properties

- `errorCode` (number): **Allowed Values**: `4000269`
- `errorMessage` (string): **Allowed Values**: `Invalid request. seatPriceTiers isn't supported for bundles.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/seatpricetiersnotallowedforbundleerror)*