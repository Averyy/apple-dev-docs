# BundleItemRemovalRequiresNextBillCycleError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object BundleItemRemovalRequiresNextBillCycleError
```

## Properties

- `errorCode` (number): **Allowed Values**: `4000242`
- `errorMessage` (string): **Allowed Values**: `Invalid request. Removing a bundleItem is a downgrade and must be effective at NEXT_BILL_CYCLE; an IMMEDIATELY modify cannot drop existing bundleItems.`

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
- [object BundleItemsOnNonBundleParentError](./bundleitemsonnonbundleparenterror.md)
- [object BundleMigrateNotSupportedError](./bundlemigratenotsupportederror.md)
- [object BundleMigrateSkuMismatchError](./bundlemigrateskumismatcherror.md)
- [object BundleTransactionIdNotSupportedError](./bundletransactionidnotsupportederror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/bundleitemremovalrequiresnextbillcycleerror)*