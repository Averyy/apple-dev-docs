# Delete a marketplace webhook configuration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Delete a specific marketplace notifcation endpoint URL.

**Availability**:
- App Store Connect API 3.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
DELETE https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/c74970b8-6be0-40fa-8f51-8e1532005635
```

**Response**:

```json
204
```

## Endpoint

`DELETE https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/{id}`

## Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the `marketplaceWebhooks` resource ID from the [`Read marketplace webhook information`](get-v1-marketplacewebhooks.md) response.

## See Also

- [Read marketplace webhook information](get-v1-marketplacewebhooks.md)
  Get the endpoint URL for alternative distribution package notifications.
- [Add a marketplace webhook configuration](post-v1-marketplacewebhooks.md)
  Add a new endpoint URL and secret for alternative distribution package notifications.
- [Modify a marketplace webhook configuration](patch-v1-marketplacewebhooks-_id_.md)
  Update the endpoint URL and secret for alternative distribution package notifications.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/delete-v1-marketplacewebhooks-_id_)*