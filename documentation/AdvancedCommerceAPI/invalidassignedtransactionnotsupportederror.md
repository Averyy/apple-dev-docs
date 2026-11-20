# InvalidAssignedTransactionNotSupportedError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

An error that indicates the transaction is one that an organization or group assigns to the customer, which the endpoint doesn’t support.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object InvalidAssignedTransactionNotSupportedError
```

## Discussion

The [`Migrate a Subscription to Advanced Commerce API`](./migrate-subscription-to-advanced-commerce-api.md) endpoint returns this error if you provide the identifier of a transaction with an [`inAppOwnershipType`](../AppStoreServerAPI/inappownershiptype.md) of `ASSIGNED`. Provide the transaction identifier of the purchaser’s subscription instead.

## Properties

- `errorCode` (number): **Allowed Values**: `4000227`
- `errorMessage` (string): **Allowed Values**: `Invalid request. Assigned transactions aren't supported by this endpoint.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/invalidassignedtransactionnotsupportederror)*