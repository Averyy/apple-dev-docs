# List the territory availability of a subscription

**Framework**: App Store Connect API  
**Kind**: httpRequest

List the territory availability and currency of a specific subscription.

**Availability**:
- App Store Connect API 2.3+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/availableTerritories?limit=5
```

**Response**:

```json
{
  "data" : [ {
    "type" : "territories",
    "id" : "SLV",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/SLV"
    }
  }, {
    "type" : "territories",
    "id" : "BRB",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/BRB"
    }
  }, {
    "type" : "territories",
    "id" : "CYM",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/CYM"
    }
  }, {
    "type" : "territories",
    "id" : "NIC",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/NIC"
    }
  }, {
    "type" : "territories",
    "id" : "NAM",
    "attributes" : {
      "currency" : "USD"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/territories/NAM"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/availableTerritories?limit=5",
    "next" : "https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/6447589418/availableTerritories?cursor=BQ.AO4JFxQ&limit=5"
  },
  "meta" : {
    "paging" : {
      "total" : 175,
      "limit" : 5
    }
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionAvailabilities/{id}/availableTerritories`

## Parameters

- `fields[territories]` ([string])
- `limit` (integer)

## See Also

- [Read the availability of a subscription](get-v1-subscriptionavailabilities-_id_.md)
  Get information about the territory availability for a subscription.
- [GET /v1/subscriptionAvailabilities/{id}/relationships/availableTerritories](get-v1-subscriptionavailabilities-_id_-relationships-availableterritories.md)
- [Modify the territory availability of a subscription](post-v1-subscriptionavailabilities.md)
  Update the territory availability of a specific subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptionavailabilities-_id_-availableterritories)*