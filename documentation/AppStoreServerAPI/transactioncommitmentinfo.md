# TransactionCommitmentInfo

**Framework**: App Store Server API  
**Kind**: dictionary  
**Role**: Object

**Availability**:
- App Store Server API 1.21+

## Declaration

```
object TransactionCommitmentInfo
```

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)

## Properties

- `billingPeriodNumber` (billingPeriodNumber): **Minimum**: `1`; **Maximum**: `12`
- `commitmentExpiresDate` (commitmentExpiresDate)
- `commitmentPrice` (commitmentPrice)
- `totalBillingPeriods` (totalBillingPeriods)

## See Also

### Monthly subscriptions with 12-month commitments
- [type billingPeriodNumber](./billingperiodnumber.md)
- [type commitmentExpiresDate](./commitmentexpiresdate.md)
- [type commitmentPrice](./commitmentprice.md)
- [type totalBillingPeriods](./totalbillingperiods.md)
- [object RenewalCommitmentInfo](./renewalcommitmentinfo.md)
- [type commitmentAutoRenewProductId](./commitmentautorenewproductid.md)
- [type commitmentAutoRenewStatus](./commitmentautorenewstatus.md)
- [type commitmentRenewalBillingPlanType](./commitmentrenewalbillingplantype.md)
- [type commitmentRenewalDate](./commitmentrenewaldate.md)
- [type commitmentRenewalPrice](./commitmentrenewalprice.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/transactioncommitmentinfo)*