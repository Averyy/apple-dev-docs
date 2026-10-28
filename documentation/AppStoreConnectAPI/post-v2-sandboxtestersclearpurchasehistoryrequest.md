# Clear purchase history for a sandbox tester

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Remove purchase history from a Sandbox Apple Account.

**Availability**:
- App Store Connect API 2.2+

## Discussion

### Example Request and Response

**Request**:

```
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

## Request Body

**Content-Type**: `application/json`  
**Type**: `SandboxTestersClearPurchaseHistoryRequestV2CreateRequest`

## Responses

- `201` Created (`SandboxTestersClearPurchaseHistoryRequestV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Sandbox Tester Lookup and Modification
- [List sandbox testers](./get-v2-sandboxtesters.md)
  Get a list of Sandbox Testers for your team.
- [Modify a sandbox tester](./patch-v2-sandboxtesters-_id_.md)
  Change the subscription renewal time rate, set interrupted purchases or change territory of Sandbox Apple Account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/post-v2-sandboxtestersclearpurchasehistoryrequest)*