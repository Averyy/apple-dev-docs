# WebhookDelivery.Attributes

**Framework**: App Store Connect API  
**Kind**: dictionary

Attributes that describe a webhook delivery resource.

**Availability**:
- App Store Connect API 4.0+

## Declaration

```swift
object WebhookDelivery.Attributes
```

## Topics

### Dictionaries
- [object WebhookDelivery.Attributes.Request](webhookdelivery/attributes-data.dictionary/request-data.dictionary.md)
  The HTTP request details of a webhook delivery attempt, including headers and body.
- [object WebhookDelivery.Attributes.Response](webhookdelivery/attributes-data.dictionary/response-data.dictionary.md)
  The HTTP response received from the webhook endpoint during a delivery attempt.

## Properties

- `createdDate` (date-time)
- `deliveryState` (string)
- `errorMessage` (string)
- `redelivery` (boolean)
- `request` (WebhookDelivery.Attributes.Request)
- `response` (WebhookDelivery.Attributes.Response)
- `sentDate` (date-time)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/webhookdelivery/attributes-data.dictionary)*