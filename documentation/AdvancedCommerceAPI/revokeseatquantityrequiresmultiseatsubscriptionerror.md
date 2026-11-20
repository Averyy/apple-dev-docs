# RevokeSeatQuantityRequiresMultiSeatSubscriptionError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the request includes a number of seats to revoke for a subscription that isn’t a multiseat purchase.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object RevokeSeatQuantityRequiresMultiSeatSubscriptionError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

The [`Revoke Subscription`](./revoke-subscription.md) endpoint returns this error if you provide a [`revokeSeatQuantity`](./revokeseatquantity.md) for a subscription that a customer doesn’t buy as a multiseat purchase. Omit `revokeSeatQuantity` to revoke the entire subscription.

## Properties

- `errorCode` (number): **Allowed Values**: `4000290`
- `errorMessage` (string): **Allowed Values**: `Invalid request. revokeSeatQuantity is only supported for a multiseat subscription.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/revokeseatquantityrequiresmultiseatsubscriptionerror)*