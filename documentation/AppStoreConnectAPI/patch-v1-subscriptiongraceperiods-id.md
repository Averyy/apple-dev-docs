# Modify the Billing Grace Period Opt-In Status and Duration

**Framework**: App Store Connect API  
**Kind**: httpRequest

Change the Boolean value representing the billing grace period opt-in status.

**Availability**:
- App Store Connect API 2.0+

## Mentions

- [Managing auto-renewable subscriptions](managing-auto-renewable-subscriptions.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v1/subscriptionGracePeriods/6446671329     
-d $'{
  "data": {
    "type": "subscriptionGracePeriods",
    "id": "6446671329",
    "attributes": {
      "sandboxOptIn": true,
      "optIn": true,
      "renewalType": "PAID_TO_PAID_ONLY",
      "duration": "TWENTY_EIGHT_DAYS"
    }
  }
}'
```

**Response**:

```json
{
  "data" : {
    "type" : "subscriptionGracePeriods",
    "id" : "6446671329",
    "attributes" : {
      "optIn" : true,
      "sandboxOptIn" : true,
      "duration" : "TWENTY_EIGHT_DAYS",
      "renewalType" : "PAID_TO_PAID_ONLY"
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

`PATCH https://api.appstoreconnect.apple.com/v1/subscriptionGracePeriods/{id}`

## Parameters

- `id` (string) *(required)*

## Request Body

There are now new duration options that can be set by using [`SubscriptionGracePeriodDuration`](subscriptiongraceperiodduration.md)

## See Also

- [Read the Billing Grace Period Value for an App](get-v1-apps-_id_-subscriptiongraceperiod.md)
  Get the Boolean value that represents the grace period opt-in state for your app.
- [GET /v1/apps/{id}/relationships/subscriptionGracePeriod](get-v1-apps-_id_-relationships-subscriptiongraceperiod.md)
- [Read the Billing Grace Period Value](get-v1-subscriptiongraceperiods-_id_.md)
  Get the Boolean value that represents the billing grace period opt-in state and the duration of the billing grace period.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-subscriptiongraceperiods-_id_)*