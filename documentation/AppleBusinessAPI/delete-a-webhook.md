# Delete a Webhook

**Framework**: AppleBusinessAPI  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Delete a webhook from an organization.

**Availability**:
- Apple Business API 2.8+

### Example

**Request**:

```
curl -X DELETE "https://api-business.apple.com/v1/webhooks/{id}" \
    -H "Authorization: Bearer ${ACCESS_TOKEN}"
```

**Response**:

```
HTTP/1.1 204 No Content
```

## Endpoint

`DELETE https://api-business.apple.com/v1/webhooks/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: The unique identifier for the resource.

## Responses

- `204` No Content
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
- [Get All Deliveries for a Webhook](./get-all-deliveries-for-a-webhook.md)
  Get a list of deliveries for a webhook.
- [Create a WebhookDelivery](./create-a-webhookdelivery.md)
  Create a new webhook delivery based on an existing delivery.
- [Create a WebhookPing](./create-a-webhookping.md)
  Send a ping event to a webhook to test that it receives notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applebusinessapi/delete-a-webhook)*