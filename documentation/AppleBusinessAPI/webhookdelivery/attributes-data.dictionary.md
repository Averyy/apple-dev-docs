# WebhookDelivery.Attributes

**Framework**: AppleBusinessAPI  
**Kind**: dictionary  
**Role**: Object

Attributes that describe a webhook delivery resource.

**Availability**:
- Apple Business API 2.8+

## Declaration

```
object WebhookDelivery.Attributes
```

## Topics

### Dictionaries
- [object WebhookDelivery.Attributes.Request](./attributes-data.dictionary/request-data.dictionary.md)
  Information about the request that was sent to the webhook URL.
- [object WebhookDelivery.Attributes.Response](./attributes-data.dictionary/response-data.dictionary.md)
  Information about the response that the webhook URL returned.

## Properties

- `createdDateTime` (date-time): The date and time that the delivery was created.
- `deliveryState` (string): The state of the delivery. Possible values: `SUCCEEDED`, `FAILED`, `PENDING`.

  **Allowed Values**: `SUCCEEDED`, `FAILED`, `PENDING`
- `errorMessage` (string): A message that describes the error if the delivery failed.
- `redelivery` (boolean): A Boolean value that indicates whether the delivery is a redelivery.
- `sentDateTime` (date-time): The date and time that the delivery was sent.
- `request` (WebhookDelivery.Attributes.Request): Information about the request that was sent to the webhook URL.
- `response` (WebhookDelivery.Attributes.Response): Information about the response that the webhook URL returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/webhookdelivery/attributes-data.dictionary)*