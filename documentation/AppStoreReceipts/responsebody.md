# responseBody

**Framework**: App Store Receipts  
**Kind**: dictionary

The JSON data that returns in the response from the App Store.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
object responseBody
```

#### Discussion

The [`verifyReceipt`](verify-receipt.md) endpoint returns this response.

## Topics

### Objects
- [object responseBody.Pending_renewal_info](responsebody/pending_renewal_info-data.dictionary.md)
  An array of elements that refers to open or failed auto-renewable subscription renewals.
- [object responseBody.Latest_receipt_info](responsebody/latest_receipt_info-data.dictionary.md)
  An array that contains all in-app purchase transactions.
- [object responseBody.Receipt](responsebody/receipt-data.dictionary.md)
  The decoded version of the encoded receipt data that you send with the request to the App Store.

## Properties

- `environment` (string): The environment the system generates the receipt for.
- `is_retryable` (boolean): An indicator when an error occurs during the request. A value of `1` indicates a temporary issue; retry validation for this receipt at a later time. A value of `0` indicates an unresolvable issue; don’t retry validation for this receipt. This is applicable only to status codes `21100–21199`.
- `latest_receipt` (byte): The latest Base64-encoded app receipt. This only returns for receipts that contain auto-renewable subscriptions.
- `latest_receipt_info` ([responseBody.Latest_receipt_info]): An array that contains all in-app purchase transactions. This excludes transactions for consumable products that your app marks as finished.
- `pending_renewal_info` ([responseBody.Pending_renewal_info]): In the JSON file, an array where each element contains the pending renewal information for each auto-renewable subscription the `product_id` identifies. This only returns for app receipts that contain auto-renewable subscriptions.
- `receipt` (responseBody.Receipt): A JSON representation of the receipt that you send for verification.
- `status` (status): Either `0` if the receipt is valid, or a status code if there’s an error. The status code reflects the status of the app receipt as a whole. See [`status`](responsebody/status.md) for possible status codes and descriptions.

## See Also

- [verifyReceipt](verify-receipt.md)
  Send a receipt to the App Store for verification.
- [object requestBody](requestbody.md)
  The JSON contents you submit with the request to the App Store.
- [object error](error.md)
  Error information that returns in the response body when a request isn’t successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody)*