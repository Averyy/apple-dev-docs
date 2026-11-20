# AddSeatsMustBeSoleChangeError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates a request to add seats includes other changes.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object AddSeatsMustBeSoleChangeError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

A [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md) returns this error if a change item raises the [`finalQuantity`](./finalquantity.md) to add seats, and the request also makes another change, such as a new SKU, different `seatPriceTiers`, or a different period. Submit other changes in a separate request.

## Properties

- `errorCode` (number): **Allowed Values**: `4000282`
- `errorMessage` (string): **Allowed Values**: `Invalid request. Adding seats must be the only change in the request. Submit any other changes separately.`

## See Also

### Error codes
- [object ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](./acapriceincreaseisnotcurrentlysupportedinindiaerror.md)
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
- [object BundleTransactionIdNotSupportedError](./bundletransactionidnotsupportederror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/addseatsmustbesolechangeerror)*