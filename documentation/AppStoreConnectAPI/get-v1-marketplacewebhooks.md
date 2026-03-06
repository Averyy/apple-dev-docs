# Read marketplace webhook information

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the endpoint URL for alternative distribution package notifications.

**Availability**:
- App Store Connect API 3.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
GET https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks
```

**Response**:

```json
{
  "data": [
    {
      "type": "marketplaceWebhooks",
      "id": "c74970b8-6be0-40fa-8f51-8e1532005635",
      "attributes": {
        "endpointUrl": "https://example.com/api/ingest/notifications"
      },
      "links": {
        "self": "https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks/c74970b8-6be0-40fa-8f51-8e1532005635"
      }
    }
  ],
  "links": {
    "self": "https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks"
  },
  "meta": {
    "paging": {
      "total": 1,
      "limit": 50
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/marketplaceWebhooks`

## Parameters

- `fields[marketplaceWebhooks]` ([string])
- `limit` (integer)

## See Also

- [Add a marketplace webhook configuration](post-v1-marketplacewebhooks.md)
  Add a new endpoint URL and secret for alternative distribution package notifications.
- [Modify a marketplace webhook configuration](patch-v1-marketplacewebhooks-_id_.md)
  Update the endpoint URL and secret for alternative distribution package notifications.
- [Delete a marketplace webhook configuration](delete-v1-marketplacewebhooks-_id_.md)
  Delete a specific marketplace notifcation endpoint URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-marketplacewebhooks)*