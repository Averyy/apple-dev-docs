# SeatDecreaseNotAllowedError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the request would reduce the number of seats.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SeatDecreaseNotAllowedError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)

## Discussion

A [`SubscriptionModifyInAppRequest`](./subscriptionmodifyinapprequest.md) returns this error if the [`finalQuantity`](./finalquantity.md) in its [`SubscriptionModifyChangeItem`](./subscriptionmodifychangeitem.md) is lower than the item’s current number of seats. The `finalQuantity` is the total number of seats after the change.

A change item can’t reduce the number of seats. The group purchaser reduces the number of seats in their subscription settings, and the change takes effect at the next renewal date. To revoke unclaimed seats, call the [`Revoke Subscription`](./revoke-subscription.md) endpoint with a [`revokeSeatQuantity`](./revokeseatquantity.md).

## Properties

- `errorCode` (number): **Allowed Values**: `4000281`
- `errorMessage` (string): **Allowed Values**: `Invalid request. finalQuantity can't be lower than the subscription's current seat quantity.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/seatdecreasenotallowederror)*