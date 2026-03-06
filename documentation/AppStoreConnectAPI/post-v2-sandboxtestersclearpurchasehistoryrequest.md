# Clear Purchase History for a Sandbox Tester

**Framework**: App Store Connect API  
**Kind**: httpRequest

Remove purchase history from a Sandbox Apple Account.

**Availability**:
- App Store Connect API 2.2+

#### Discussion

##### Example Request and Response

**Request**:

```None
https://api.appstoreconnect.apple.com/v2/sandboxTestersClearPurchaseHistoryRequest 
-d
{
  "data": {
    "type": "sandboxTestersClearPurchaseHistoryRequest",
    "relationships": {
      "sandboxTesters": {
        "data": [
          {
            "id": "47be9e57-1a3f-49c2-8ce7-af27a977ebb0",
            "type": "sandboxTesters"
          }
        ]
      }
    }
  }
}

```

**Response**:

```json
{
  "data" : {
    "type" : "sandboxTestersClearPurchaseHistoryRequest",
    "id" : "c47f2eda-042e-4f4b-9bb9-ded24c507e41",
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/sandboxTestersClearPurchaseHistoryRequest/c47f2eda-042e-4f4b-9bb9-ded24c507e41"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v2/sandboxTestersClearPurchaseHistoryRequest"
  }
}
```

## Endpoint

`POST https://api.appstoreconnect.apple.com/v2/sandboxTestersClearPurchaseHistoryRequest`

## See Also

- [List Sandbox Testers](get-v2-sandboxtesters.md)
  Get a list of Sandbox Testers for your team.
- [Modify a Sandbox Tester](patch-v2-sandboxtesters-_id_.md)
  Change the subscription renewal time rate, set interrupted purchases or change territory of Sandbox Apple Account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-sandboxtestersclearpurchasehistoryrequest)*