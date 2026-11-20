# SubsForGroupsRequiresLatestVersionError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the request uses a version of the API that doesn’t support multiseat purchases.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubsForGroupsRequiresLatestVersionError
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)
- [Creating multiseat purchases](./creating-multiseat-purchases.md)

## Discussion

Multiseat purchases require version 2 of the Advanced Commerce API. A version 1 in-app request, or a version 1 endpoint such as [`Change Subscription Price V1`](./change-subscription-price-v1.md) or [`Migrate Subscription to Advanced Commerce API V1`](./migrate-subscription-to-advanced-commerce-api-v1.md), returns this error for a subscription that a customer buys as a multiseat purchase. Use the version 2 request or endpoint instead. For more information, see [Creating multiseat purchases](./creating-multiseat-purchases.md).

## Properties

- `errorCode` (int64): **Allowed Values**: `4000298`
- `errorMessage` (string): **Allowed Values**: `Invalid request. Multi-seat subscriptions are not supported for this version of the endpoint, use a newer version.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subsforgroupsrequireslatestversionerror)*