# UsageInformation

**Framework**: Apple Pay Merchant Token Usage Information API  
**Kind**: dictionary

Information about the usage of a merchant token, such as past and upcoming payments.

## Declaration

```swift
object UsageInformation
```

## Properties

- `expirationDate` (date-time): The date and time when the usage information is considered expired. This value can be at most one year in the future.
- `merchantLogoName` (string): The name of an image that represents the `merchant—their` logo.
- `merchantName` (string) *(required)*
- `merchantTokenIdentifier` (string) *(required)*: The merchant token identifier. This value must match the identifier of the merchant token for which you provided the usage information.
- `modificationDate` (date-time) *(required)*: The date and time when the usage information was last modified.
- `otherUsageDescription` (string): A localized description of other usage, such as being a fallback payment method with the merchant.
- `pastPayments` ([PastPayment]): A list of past payments.
- `paymentIssueRecoveryURL` (string): A URL the merchant provides that lets the person fix a payment problem, such as updating their card or resolving a declined payment.
- `schemaVersion` (number) *(required)*: A name representing the bank and the card used for the transaction.
- `upcomingPayments` ([UpcomingPayment]): A list of upcoming payments to display in the order provided.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation/usageinformation)*