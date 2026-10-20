# Read the billing grace period value for an app

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the Boolean value that represents the grace period opt-in state for your app.

**Availability**:
- App Store Connect API 2.0+

#### Discussion

##### Example Request and Response

**Request**:

```
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

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the app resource ID from the [`List apps`](./get-v1-apps.md) response.

### Query Parameters

- `fields[subscriptionGracePeriods]` ([string]): Additional fields to include for each subscription grace period resource returned by the response.

  **Allowed Values**: `optIn`, `sandboxOptIn`, `duration`, `renewalType`

## Responses

- `200` OK (`SubscriptionGracePeriodResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Getting subscription group and subscription grace period information
- [List all subscription groups for an app](./get-v1-apps-_id_-subscriptiongroups.md)
  Get a list of subscription groups for a specific app.
- [Get the subscription grace period ID for an app](./get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [List subscription group IDs for an app](./get-v1-apps-_id_-relationships-subscriptiongroups.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v1-apps-_id_-subscriptiongraceperiod)*