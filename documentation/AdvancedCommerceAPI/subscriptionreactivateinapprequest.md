# SubscriptionReactivateInAppRequest

**Framework**: Advanced Commerce API  
**Kind**: dictionary  
**Role**: Object

The request your app provides to reactivate a subscription that has automatic renewal turned off.

**Availability**:
- Advanced Commerce API 1.3+

## Declaration

```
object SubscriptionReactivateInAppRequest
```

## Mentions

- [Advanced Commerce API changelog](./changelog.md)

### Example: Reactivate a subscription that has automatic renewal turned off

```json
{
    "operation": "REACTIVATE_SUBSCRIPTION",
    "version": "2", 
    "transactionId": "12345",
    "requestInfo": {
        "requestReferenceId": "e2a88501-25ba-403a-9c46-d7b8eecc56ba"
    },
    "storefront": "USA"
}
```

## Properties

- `operation` (string) *(required)*: **Allowed Values**: `REACTIVATE_SUBSCRIPTION`
- `requestInfo` (RequestInfo) *(required)*
- `storefront` (storefront)
- `transactionId` (transactionId) *(required)*
- `version` (version) *(required)*

## See Also

### Subscription reactivation in the app
- [object SubscriptionReactivateItem](./subscriptionreactivateitem.md)
  An item in a subscription to reactivate.
- [object SubscriptionReactivateInAppRequestV1](./subscriptionreactivateinapprequestv1.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/advancedcommerceapi/subscriptionreactivateinapprequest)*