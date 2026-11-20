# AddSeatsRequiresImmediateEffectiveError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates a request to add seats doesn’t take effect immediately.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object AddSeatsRequiresImmediateEffectiveError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

A [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md) returns this error if a change item raises the [`finalQuantity`](./finalquantity.md) to add seats, and the request’s [`effective`](./effective.md) value isn’t `IMMEDIATELY`. Seats you add take effect immediately.

## Properties

- `errorCode` (number): **Allowed Values**: `4000285`
- `errorMessage` (string): **Allowed Values**: `Invalid request. Adding seats must take effect immediately.`

## See Also

### Error codes
- [object ACAPriceIncreaseIsNotCurrentlySupportedInIndiaError](./acapriceincreaseisnotcurrentlysupportedinindiaerror.md)
- [object AddSeatsMustBeSoleChangeError](./addseatsmustbesolechangeerror.md)
  An error that indicates a request to add seats includes other changes.
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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/addseatsrequiresimmediateeffectiveerror)*