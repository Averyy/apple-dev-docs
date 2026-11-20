# PartialSimulateRefundDeclineError

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- Advanced Commerce API 1.1+

## Declaration

```
object PartialSimulateRefundDeclineError
```

## Properties

- `errorCode` (number): **Allowed Values**: `4000184`
- `errorMessage` (string): **Allowed Values**: `If one item has a refundReason value of SIMULATE_REFUND_DECLINE, all items must have a refundReason value of SIMULATE_REFUND_DECLINE.`

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

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/partialsimulaterefunddeclineerror)*