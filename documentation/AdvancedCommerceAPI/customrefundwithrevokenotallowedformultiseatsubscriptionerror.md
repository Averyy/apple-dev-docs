# CustomRefundWithRevokeNotAllowedForMultiSeatSubscriptionError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the request combines a custom refund with a revocation for a multiseat purchase.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object CustomRefundWithRevokeNotAllowedForMultiSeatSubscriptionError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

## Discussion

The [`Request Transaction Refund`](./request-transaction-refund.md) endpoint returns this error if the [`RefundItem`](./refunditem.md) has a `refundType` of `CUSTOM` and a `revoke` value of `true`, for a subscription that a customer buys as a multiseat purchase. Use a `refundType` of `FULL` or `PRORATED` instead.

## Properties

- `errorCode` (number): **Allowed Values**: `4000288`
- `errorMessage` (string): **Allowed Values**: `Invalid request. A CUSTOM refundType can't be combined with revoke on a multiseat subscription. Use FULL or PRORATED.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/customrefundwithrevokenotallowedformultiseatsubscriptionerror)*