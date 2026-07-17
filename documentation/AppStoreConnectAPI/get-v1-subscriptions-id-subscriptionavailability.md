# Read information about the availability of a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get information about the territory availability for a subscription.

**Availability**:
- App Store Connect API 2.4+

## Mentions

- [App Store Connect API 2.4 release notes](app-store-connect-api-2-4-release-notes.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/subscriptions/6448262369/subscriptionAvailability
```

**Response**:

```json
{
  “data”: {
    “type”: “subscriptionAvailabilities”,
    “id”: “6448262369”,
    “attributes”: {
      “availableInNewTerritories”: false
    },
    “relationships”: {
      “availableTerritories”: {
        “links”: {
          “self”: “https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6448262369/relationships/availableTerritories”,
          “related”: “https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6448262369/availableTerritories”
        }
      }
    },
    “links”: {
      “self”: “https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6448262369”
    }
  },
  “links”: {
    “self”: “https://api.appstoreconnect.apple.com/v1/subscriptions/6448262369/subscriptionAvailability”
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptions/{id}/subscriptionAvailability`

## Parameters

- `fields[subscriptionAvailabilities]` ([string])
- `fields[territories]` ([string])
- `include` ([string])
- `limit[availableTerritories]` (integer)

## See Also

- [Get the subscription availability ID for an auto-renewable subscription](get-v1-subscriptions-_id_-relationships-subscriptionavailability.md)
- [List plan availabilities for a subscription](get-v1-subscriptions-_id_-planavailabilities.md)
  List all plan availabilities for a specific auto-renewable subscription.
- [List plan availability IDs for a subscription](get-v1-subscriptions-_id_-relationships-planavailabilities.md)
  Get a list of plan availability resource IDs for a specific auto-renewable subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptions-_id_-subscriptionavailability)*