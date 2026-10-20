# SubscriptionVersion.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a SubscriptionVersion resource.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```
object SubscriptionVersion.Attributes
```

## Properties

- `version` (integer)
- `state` (string): **Allowed Values**: `PREPARE_FOR_SUBMISSION`, `READY_FOR_REVIEW`, `WAITING_FOR_REVIEW`, `IN_REVIEW`, `ACCEPTED`, `APPROVED`, `REPLACED_WITH_NEW_VERSION`, `REJECTED`, `DEVELOPER_REJECTED`

## See Also

### Objects and types
- [object SubscriptionVersion.Relationships](./relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionversion/attributes-data.dictionary)*