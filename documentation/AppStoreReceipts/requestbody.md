# requestBody

**Framework**: App Store Receipts  
**Kind**: dictionary

The JSON contents you submit with the request to the App Store.

**Availability**:
- App Store Receipts 1.0+

## Declaration

```swift
object requestBody
```

#### Discussion

To receive a decoded receipt for validation, send a request with the encoded receipt data and app password to the App Store. For receipts that contain auto-renewable subscriptions, optionally include an exclusion flag. Send this JSON data using the HTTP POST request method.

## Properties

- `receipt-data` (byte) *(required)*: The Base64-encoded receipt data.
- `password` (string): Your app’s shared secret, which is a hexadecimal string. The password is required for receipts that include subscriptions, and strongly recommended otherwise. For more information about the shared secret, see [`Generate a shared secret to verify receipts`](https://developer.apple.comhttps://help.apple.com/app-store-connect/#/devf341c0f01).
- `exclude-old-transactions` (boolean): Set this value to `true` for the response to include only the latest renewal transaction for any subscriptions. Use this field only for app receipts that contain auto-renewable subscriptions.

## See Also

- [verifyReceipt](verify-receipt.md)
  Send a receipt to the App Store for verification.
- [object responseBody](responsebody.md)
  The JSON data that returns in the response from the App Store.
- [object error](error.md)
  Error information that returns in the response body when a request isn’t successful.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/requestbody)*