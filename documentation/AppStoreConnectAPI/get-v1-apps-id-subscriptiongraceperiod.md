# Read the Billing Grace Period Value for an App

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the Boolean value that represents the grace period opt-in state for your app.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/apps/6446671329/subscriptionGracePeriod
```

**Response**:

```json
  "data" : {
    "type" : "subscriptionGracePeriods",
    "id" : "6446671329",
    "attributes" : {
      "optIn" : true,
      "sandboxOptIn" : false,
      "duration" : SIXTEEN_DAYS,
      "renewalType" : ALL_RENEWALS
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionGracePeriods/6446671329"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/apps/6446671329/subscriptionGracePeriod"
  }
}
```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/apps/{id}/subscriptionGracePeriod`

## Parameters

- `fields[subscriptionGracePeriods]` ([string])

## See Also

- [List All Subscription Groups for an App](get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [GET /v1/apps/{id}/relationships/subscriptionGracePeriod](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [GET /v1/apps/{id}/relationships/subscriptionGroups](get-v1-apps-_id_-relationships-subscriptiongroups.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-subscriptiongraceperiod)*