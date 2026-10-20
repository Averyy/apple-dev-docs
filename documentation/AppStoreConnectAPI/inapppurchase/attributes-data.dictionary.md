# InAppPurchase.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe an In-App Purchases resource.

**Availability**:
- App Store Connect API 1.2+ - Deprecated in 3.0

> **Deprecated**: This object is deprecated.

## Declaration

```
object InAppPurchase.Attributes
```

## Properties

- `inAppPurchaseType` (string): **Allowed Values**: `AUTOMATICALLY_RENEWABLE_SUBSCRIPTION`, `NON_CONSUMABLE`, `CONSUMABLE`, `NON_RENEWING_SUBSCRIPTION`, `FREE_SUBSCRIPTION`
- `productId` (string)
- `referenceName` (string)
- `state` (string): **Allowed Values**: `CREATED`, `DEVELOPER_SIGNED_OFF`, `DEVELOPER_ACTION_NEEDED`, `DELETION_IN_PROGRESS`, `APPROVED`, `DELETED`, `REMOVED_FROM_SALE`, `DEVELOPER_REMOVED_FROM_SALE`, `WAITING_FOR_UPLOAD`, `PROCESSING_CONTENT`, `REPLACED`, `REJECTED`, `WAITING_FOR_SCREENSHOT`, `PREPARE_FOR_SUBMISSION`, `MISSING_METADATA`, `READY_TO_SUBMIT`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `PENDING_DEVELOPER_RELEASE`

## See Also

### Objects
- [object InAppPurchase.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchase/attributes-data.dictionary)*