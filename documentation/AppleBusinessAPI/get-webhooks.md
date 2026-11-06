# Get Webhooks

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of webhooks in an organization.

**Availability**:
- Apple Business API 2.8+

## Mentions

- [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md)

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/webhooks" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": [
    {
      "type": "webhooks",
      "id": "webhook-12345",
      "attributes": {
        "name": "Device change notifications",
        "enabled": true,
        "eventTypes": ["ORG_DEVICE_ATTRIBUTE_CHANGED", "ORG_DEVICE_RELATIONSHIP_ASSIGNED_SERVER_CHANGED"],
        "url": "https://example.com/webhooks/apple",
        "createdDateTime": "2026-10-01T10:30:00Z",
        "updatedDateTime": "2026-10-01T10:30:00Z"
      },
      "relationships": {
        "deliveries": {
          "links": {
            "related": "https://api-business.apple.com/v1/webhooks/webhook-12345/deliveries"
          }
        }
      },
      "links": {
        "self": "https://api-business.apple.com/v1/webhooks/webhook-12345"
      }
    }
  ],
  "links": {
    "self": "https://api-business.apple.com/v1/webhooks"
  },
  "meta": {
    "paging": {
      "limit": 100
    }
  }
}
```

## Topics

### Responses
- [object WebhooksResponse](./webhooksresponse.md)
  A response that contains a list of webhook resources.

## Endpoint

`GET https://api-business.apple.com/v1/webhooks`

## Parameters

### Query Parameters

- `fields[webhooks]` ([string]): The fields to return for included related types.

  **Allowed Values**: `name`, `enabled`, `eventTypes`, `url`, `createdDateTime`, `updatedDateTime`, `deliveries`
- `limit` (integer): The number of resources to return.

  **Maximum**: `1000`
- `cursor` (string): An opaque cursor value that you use to retrieve the next page of results.

## Responses

- `200` OK (`WebhooksResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Webhooks
- [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md)
  Learn how to authenticate and process webhook notifications from Apple Business and the data each event contains.
- [Get Webhook Information](./get-webhook-information.md)
  Get information about a specific webhook in an organization.
- [Create a Webhook](./create-a-webhook.md)
  Create a new webhook in an organization.
- [Update a Webhook](./update-a-webhook.md)
  Update an existing webhook in an organization.
- [Delete a Webhook](./delete-a-webhook.md)
  Delete a webhook from an organization.
- [Get All Deliveries for a Webhook](./get-all-deliveries-for-a-webhook.md)
  Get a list of deliveries for a webhook.
- [Create a WebhookDelivery](./create-a-webhookdelivery.md)
  Create a new webhook delivery based on an existing delivery.
- [Create a WebhookPing](./create-a-webhookping.md)
  Send a ping event to a webhook to test that it receives notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-webhooks)*