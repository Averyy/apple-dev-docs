# status

**Framework**: App Store Receipts  
**Kind**: typealias  
**Role**: Type

The status of the app receipt.

**Availability**:
- App Store Receipts 1.0+ - Deprecated in 1.7

## Declaration

```
int status
```

## Possible Values

- `21000`: The request to the App Store didn’t use the HTTP POST request method.
- `21001`: The App Store no longer sends this status code.
- `21002`: The data in the `receipt-data` property is malformed or the service experienced a temporary issue. Try again.
- `21003`: The system couldn’t authenticate the receipt.
- `21004`: The shared secret you provided doesn’t match the shared secret on file for your account.
- `21005`: The receipt server was temporarily unable to provide the receipt. Try again.
- `21006`: This receipt is valid, but the subscription is in an expired state. When your server receives this status code, the system also decodes and returns receipt data as part of the response. This status only returns for iOS 6-style transaction receipts for auto-renewable subscriptions.
- `21007`: This receipt is from the test environment, but you sent it to the production environment for verification.
- `21008`: This receipt is from the production environment, but you sent it to the test environment for verification.
- `21009`: Internal data access error. Try again later.
- `21010`: The system can’t find the user account or the user account has been deleted.

## Discussion

The [`verifyReceipt`](./verify-receipt.md) endpoint returns this field in the JSON response, [`responseBody`](./responsebody.md).

The value for `status` is `0` if the receipt is valid, or a status code if there’s an error. The status code reflects the status of the app receipt as a whole. For example, if you send a valid app receipt that contains an expired subscription, the response is `0` because the receipt is valid.

Status codes `21100–21199` are various internal data access errors.

## See Also

### Receipt and subscription status
- [type auto_renew_status](./auto_renew_status.md)
  The renewal status for the auto-renewable subscription.
- [type is_in_billing_retry_period](./is_in_billing_retry_period.md)
  An indicator of whether an auto-renewable subscription is in the billing retry period.
- [type is_in_intro_offer_period](./is_in_intro_offer_period.md)
  An indicator of whether an auto-renewable subscription is in the introductory price period.
- [type is_trial_period](./is_trial_period.md)
  An indicator of whether an auto-renewable subscription is in the free trial period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/status)*