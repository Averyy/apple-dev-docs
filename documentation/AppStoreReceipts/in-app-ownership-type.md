# in_app_ownership_type

**Framework**: App Store Receipts  
**Kind**: typealias

The relationship of the user with the family-shared purchase to which they have access.

**Availability**:
- App Store Receipts 1.4+

## Declaration

```swift
string in_app_ownership_type
```

#### Discussion

When family members benefit from a shared subscription, App Store updates their receipt to include the family-shared purchase. Use the value of [`in_app_ownership_type`](in_app_ownership_type.md) to understand whether a transaction belongs to the purchaser or a family member who benefits.

This field appears in the App Store server notifications unified receipt ([`unified_receipt.Latest_receipt_info`](https://developer.apple.com/documentation/AppStoreServerNotifications/unified_receipt/Latest_receipt_info-data.dictionary)) and in transaction receipts ([`responseBody.Latest_receipt_info`](responsebody/latest_receipt_info-data.dictionary.md)).

For more information about Family Sharing, see [`Supporting Family Sharing in your app`](https://developer.apple.com/documentation/StoreKit/supporting-family-sharing-in-your-app).


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstorereceipts/in_app_ownership_type)*