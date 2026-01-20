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

## See Also

- [verifyReceipt](verify-receipt.md)
  Send a receipt to the App Store for verification.
- [object requestBody](requestbody.md)
  The JSON contents you submit with the request to the App Store.
- [object error](error.md)
  Error information that returns in the response body when a request isn’t successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/responsebody)*