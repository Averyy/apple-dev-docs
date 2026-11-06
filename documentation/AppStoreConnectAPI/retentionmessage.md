# RetentionMessage

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A message shown to people who start to cancel an auto-renewable subscription.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessage
```

## Topics

### Objects
- [object RetentionMessage.Attributes](./retentionmessage/attributes-data.dictionary.md)
  Attributes that describe a retention message resource.
- [object RetentionMessage.Relationships](./retentionmessage/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionMessages`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (RetentionMessage.Attributes): The resource’s attributes.
- `relationships` (RetentionMessage.Relationships): Navigational links to related data and included resource types and IDs.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

### Objects and types
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
- [object SubscriptionRetentionMessageLinkageRequest](./subscriptionretentionmessagelinkagerequest.md)
  The request body you use to assign a retention message to an auto-renewable subscription.
- [object SubscriptionRetentionMessageLinkageResponse](./subscriptionretentionmessagelinkageresponse.md)
  A response containing the resource identifier of the retention message for a subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessage)*