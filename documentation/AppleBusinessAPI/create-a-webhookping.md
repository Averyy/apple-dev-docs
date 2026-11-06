# Create a WebhookPing

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Send a ping event to a webhook to test that it receives notifications.

**Availability**:
- Apple Business API 2.8+

## Mentions

- [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md)

### Example

**Request**:

```
curl -X POST "https://api-business.apple.com/v1/webhookPings" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}" \
    -H "Content-Type: application/json" \
    -d '{
      "data": {
        "type": "webhookPings",
        "relationships": {
          "webhook": {
            "data": {
              "type": "webhooks",
              "id": "webhook-12345"
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
    "type": "webhookPings",
    "id": "ping-13579"
  },
  "links": {
    "self": "https://api-business.apple.com/v1/webhookPings/ping-13579"
  }
}
```

## Topics

### Responses
- [object WebhookPingResponse](./webhookpingresponse.md)
  A response that contains information about a webhook ping resource.

## Endpoint

`POST https://api-business.apple.com/v1/webhookPings`

## Request Body

**Content-Type**: `application/json`  
**Type**: `WebhookPingCreateRequest`

## Responses

- `201` Created (`WebhookPingResponse`, `application/json`)
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
- [Create a WebhookDelivery](./create-a-webhookdelivery.md)
  Create a new webhook delivery based on an existing delivery.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/create-a-webhookping)*