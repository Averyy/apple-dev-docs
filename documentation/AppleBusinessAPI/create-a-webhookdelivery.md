# Create a WebhookDelivery

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Create a new webhook delivery based on an existing delivery.

**Availability**:
- Apple Business API 2.8+

## Mentions

- [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md)

### Example

**Request**:

```
curl -X POST "https://api-business.apple.com/v1/webhookDeliveries" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
      "data": {
        "type": "webhookDeliveries",
        "relationships": {
          "template": {
            "data": {
              "type": "webhookDeliveries",
              "id": "delivery-67890"
            }
          }
        }
      }
    }'
```

**Response**:

```json
{
  "data": {
    "type": "webhookDeliveries",
    "id": "delivery-new-123",
    "attributes": {
      "createdDateTime": "2026-10-02T08:15:00Z",
      "deliveryState": "SUCCEEDED",
      "redelivery": true,
      "sentDateTime": "2026-10-02T08:15:01Z",
      "request": {
        "url": "https://example.com/webhooks/apple"
      },
      "response": {
        "httpStatusCode": 200,
        "body": "OK"
      }
    },
    "relationships": {
      "event": {
        "links": {
          "related": "https://api-business.apple.com/v1/webhookDeliveries/delivery-new-123/event"
        },
        "data": {
          "type": "webhookEvents",
          "id": "event-24680"
        }
      }
    }
  },
  "links": {
    "self": "https://api-business.apple.com/v1/webhookDeliveries/delivery-new-123"
  }
}
```

## Topics

### Responses
- [object WebhookDeliveryResponse](./webhookdeliveryresponse.md)
  A response that contains information about a webhook delivery resource.

## Endpoint

`POST https://api-business.apple.com/v1/webhookDeliveries`

## Request Body

**Content-Type**: `application/json`  
**Type**: `WebhookDeliveryCreateRequest`

## Responses

- `201` Created (`WebhookDeliveryResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `409` Conflict (`ErrorResponse`, `application/json`): Request entity error(s).
- `422` (`ErrorResponse`, `application/json`): Unprocessable request entity error(s).
- `429` (`ErrorResponse`, `application/json`): **Too Many Requests**

## See Also

### Webhooks
- [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md)
  Learn how to authenticate and process webhook notifications from Apple Business and the data each event contains.
- [Get Webhooks](./get-webhooks.md)
  Get a list of webhooks in an organization.
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
- [Create a WebhookPing](./create-a-webhookping.md)
  Send a ping event to a webhook to test that it receives notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/create-a-webhookdelivery)*