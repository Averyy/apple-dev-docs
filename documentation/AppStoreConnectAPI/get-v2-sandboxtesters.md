# List Sandbox Testers

**Framework**: App Store Connect API  
**Kind**: httpRequest

Get a list of Sandbox Testers for your team.

**Availability**:
- App Store Connect API 2.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v2/sandboxTesters
```

**Response**:

```json
{
  "data" : [ {
    "type" : "sandboxTesters",
    "id" : "47be9e57-1a3f-49c2-8ce7-af27a977ebb0",
    "attributes" : {
      "firstName" : "Anne",
      "lastName" : "Johnson",
      "acAccountName" : "annejohnson1@icloud.com",
      "territory" : "USA",
      "applePayCompatible" : true,
      "interruptPurchases" : false,
      "subscriptionRenewalRate" : "MONTHLY_RENEWAL_EVERY_FIVE_MINUTES"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/sandboxTesters/47be9e57-1a3f-49c2-8ce7-af27a977ebb0"
    }
  } ],
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v2/sandboxTesters"
  },
  "meta" : {
    "paging" : {
      "total" : 1,
      "limit" : 50
    }
  }
}

```

## Endpoint

`GET https://api.appstoreconnect.apple.com/v2/sandboxTesters`

## Parameters

- `fields[sandboxTesters]` ([string])
- `limit` (integer)

## See Also

- [Modify a Sandbox Tester](patch-v2-sandboxtesters-_id_.md)
  Change the subscription renewal time rate, set interrupted purchases or change territory of Sandbox Apple Account.
- [Clear Purchase History for a Sandbox Tester](post-v2-sandboxtestersclearpurchasehistoryrequest.md)
  Remove purchase history from a Sandbox Apple Account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/get-v2-sandboxtesters)*