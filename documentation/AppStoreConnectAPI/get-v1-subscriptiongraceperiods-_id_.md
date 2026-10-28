# Read the billing grace period value

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the Boolean value that represents the billing grace period opt-in state and the duration of the billing grace period.

**Availability**:
- App Store Connect API 2.0+

## Discussion

### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*

### Query Parameters

- `fields[subscriptionGracePeriods]` ([string]): **Allowed Values**: `optIn`, `sandboxOptIn`, `duration`, `renewalType`

## Responses

- `200` OK (`SubscriptionGracePeriodResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Endpoints
- [Read the billing grace period value for an app](./get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [Get the subscription grace period ID for an app](./get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [Modify the billing grace period opt-in status and duration](./patch-v1-subscriptiongraceperiods-_id_.md)
  Change the Boolean value representing the billing grace period opt-in status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-subscriptiongraceperiods-_id_)*