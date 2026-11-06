# Get All Deliveries for a Webhook

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get a list of deliveries for a webhook.

**Availability**:
- Apple Business API 2.8+

## Mentions

- [Understanding webhook events](../apple-school-and-business-manager-api/understanding-apple-business-api-webhook-events.md)

### Example

**Request**:

```
curl "https://api-business.apple.com/v1/webhooks/{id}/deliveries" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```json
{
  "data": [
    {
      "type": "webhookDeliveries",
      "id": "delivery-67890",
      "attributes": {
        "createdDateTime": "2026-10-02T08:15:00Z",
        "deliveryState": "SUCCEEDED",
        "redelivery": false,
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
            "related": "https://api-business.apple.com/v1/webhookDeliveries/delivery-67890/event"
          },
          "data": {
            "type": "webhookEvents",
            "id": "event-24680"
          }
        }
      }
    }
  ],
  "links": {
    "self": "https://api-business.apple.com/v1/webhooks/webhook-12345/deliveries"
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
- [object WebhookDeliveriesResponse](./webhookdeliveriesresponse.md)
  A response that contains a list of webhook delivery resources.

## Endpoint

`GET https://api-business.apple.com/v1/webhooks/{id}/deliveries`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

### Query Parameters

- `filter[deliveryState]` ([string]): Filter the deliveries by delivery state. Possible values: `SUCCEEDED`, `FAILED`, `PENDING`.

  **Allowed Values**: `SUCCEEDED`, `FAILED`, `PENDING`
- `filter[createdDateTimeAtOrAfter]` ([string]): Return only deliveries created at or after this date and time.
- `filter[createdDateTimeAtBefore]` ([string]): Return only deliveries created before this date and time.
- `fields[webhookDeliveries]` ([string]): The fields to return for webhook deliveries.

  **Allowed Values**: `createdDateTime`, `deliveryState`, `errorMessage`, `redelivery`, `sentDateTime`, `request`, `response`, `event`
- `fields[webhookEvents]` ([string]): The fields to return for included webhook events.

  **Allowed Values**: `eventType`, `payload`, `isPingEvent`, `createdDateTime`
- `limit` (integer): The number of resources to return.

  **Maximum**: `1000`
- `cursor` (string): An opaque cursor value that you use to retrieve the next page of results.
- `include` ([string]): Related resources to include in the response. Possible value: `event`.

  **Allowed Values**: `event`

## Responses

- `200` OK (`WebhookDeliveriesResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`)
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
- [Create a WebhookDelivery](./create-a-webhookdelivery.md)
  Create a new webhook delivery based on an existing delivery.
- [Create a WebhookPing](./create-a-webhookping.md)
  Send a ping event to a webhook to test that it receives notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/get-all-deliveries-for-a-webhook)*