# unified_receipt

**Framework**: App Store Server Notifications  
**Kind**: dictionary

An object that contains information about the most recent in-app purchase transactions for the app.

**Availability**:
- App Store Server Notifications 1.0+

## Declaration

```swift
object unified_receipt
```

## Mentions

- [Receiving App Store Server Notifications](receiving-app-store-server-notifications.md)

## Topics

### Objects
- [object unified_receipt.Latest_receipt_info](unified_receipt/latest_receipt_info-data.dictionary.md)
  An object that contains information about the latest in-app subscription transaction.
- [object unified_receipt.Pending_renewal_info](unified_receipt/pending_renewal_info-data.dictionary.md)
  An array of elements that refers to open auto-renewable subscription renewals or ones that failed in the past.

## Properties

- `environment` (string): The environment for which the App Store generated the receipt.
- `latest_receipt` (byte): The latest Base64-encoded app receipt.
- `latest_receipt_info` ([unified_receipt.Latest_receipt_info]): An array that contains the latest 100 in-app purchase transactions of the decoded value in `latest_receipt`. This array excludes transactions for consumable products your app has marked as finished. The contents of this array are identical to those in [`responseBody.Latest_receipt_info`](https://developer.apple.com/documentation/AppStoreReceipts/responseBody/Latest_receipt_info-data.dictionary) in the [`verifyReceipt`](https://developer.apple.com/documentation/AppStoreReceipts/Verify-Receipt) endpoint response for receipt validation.
- `pending_renewal_info` ([unified_receipt.Pending_renewal_info]): An array in which each element contains the pending renewal information for each auto-renewable subscription identified in `product_id`. The contents of this array are identical to those in [`responseBody.Pending_renewal_info`](https://developer.apple.com/documentation/AppStoreReceipts/responseBody/Pending_renewal_info-data.dictionary) in the [`verifyReceipt`](https://developer.apple.com/documentation/AppStoreReceipts/Verify-Receipt) endpoint response for receipt validation.
- `status` (integer): The status code, where `0` indicates that the notification is valid.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreservernotifications/unified_receipt)*