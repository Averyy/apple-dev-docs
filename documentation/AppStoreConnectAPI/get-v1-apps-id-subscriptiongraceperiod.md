# Read the billing grace period value for an app

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

- `fields[subscriptionGracePeriods]` ([string]): Additional fields to include for each subscription grace period resource returned by the response.

## See Also

- [List all subscription groups for an app](get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [Get the subscription grace period ID for an app](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [List subscription group IDs for an app](get-v1-apps-_id_-relationships-subscriptiongroups.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-subscriptiongraceperiod)*