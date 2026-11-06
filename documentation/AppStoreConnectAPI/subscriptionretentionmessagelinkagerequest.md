# SubscriptionRetentionMessageLinkageRequest

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The request body you use to assign a retention message to an auto-renewable subscription.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object SubscriptionRetentionMessageLinkageRequest
```

## Topics

### Objects
- [object SubscriptionRetentionMessageLinkageRequest.Data](./subscriptionretentionmessagelinkagerequest/data-data.dictionary.md)
  The type and ID of the retention message to assign to the subscription.

## Properties

- `data` (SubscriptionRetentionMessageLinkageRequest.Data) *(required)*: The type and ID of the related resource.

## See Also

### Objects and types
- [object RetentionMessage](./retentionmessage.md)
  A message shown to people who start to cancel an auto-renewable subscription.
- [object RetentionMessageCreateRequest](./retentionmessagecreaterequest.md)
  The request body you use to create a retention message.
- [object RetentionMessageResponse](./retentionmessageresponse.md)
  The response body for endpoints that create or read a single retention message.
- [object RetentionMessagesResponse](./retentionmessagesresponse.md)
  The response body for endpoints that list retention messages.
- [object RetentionMessageVersionsResponse](./retentionmessageversionsresponse.md)
  The response body for endpoints that list retention message versions.
- [object RetentionMessageVersionsLinkagesResponse](./retentionmessageversionslinkagesresponse.md)
  A response containing the resource identifiers of versions for a retention message.
- [object RetentionMessageSubscriptionsLinkagesResponse](./retentionmessagesubscriptionslinkagesresponse.md)
  A response containing the resource identifiers of subscriptions that use a retention message.
- [object AppRetentionMessagesLinkagesResponse](./appretentionmessageslinkagesresponse.md)
  A response containing the resource identifiers of retention messages for an app.
- [object SubscriptionRetentionMessageLinkageResponse](./subscriptionretentionmessagelinkageresponse.md)
  A response containing the resource identifier of the retention message for a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionretentionmessagelinkagerequest)*