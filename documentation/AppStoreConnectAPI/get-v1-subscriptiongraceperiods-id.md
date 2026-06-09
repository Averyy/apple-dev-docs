# Read the billing grace period value

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get the Boolean value that represents the billing grace period opt-in state and the duration of the billing grace period.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/subscriptionGracePeriods/6446671329
```

**Response**:

```json
{
  "data" : {
    "type" : "subscriptionGracePeriods",
    "id" : "6446671329",
    "attributes" : {
      "optIn" : true,
      "sandboxOptIn" : false,
      "duration" : "THREE_DAYS",
      "renewalType" : "ALL_RENEWALS"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionGracePeriods/6446671329"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/subscriptionGracePeriods/6446671329"
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v1/subscriptionGracePeriods/{id}`

## Parameters

- `fields[subscriptionGracePeriods]` ([string])

## See Also

- [Read the billing grace period value for an app](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [Get the subscription grace period ID for an app](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [Modify the billing grace period opt-in status and duration](patch-v1-subscriptiongraceperiods-_id_.md)
  Change the Boolean value representing the billing grace period opt-in status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptiongraceperiods-_id_)*