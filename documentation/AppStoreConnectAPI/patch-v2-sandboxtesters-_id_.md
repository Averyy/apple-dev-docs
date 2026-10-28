# Modify a sandbox tester

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Change the subscription renewal time rate, set interrupted purchases or change territory of Sandbox Apple Account.

**Availability**:
- App Store Connect API 2.2+

## Discussion

> **Note**:  Changes that you make to product metadata with the App Store Connect API can take up to 1 hour to appear in the sandbox environment.

### Example Request and Response

**Request**:

```
https://api.appstoreconnect.apple.com/v2/sandboxTesters/47be9e57-1a3f-49c2-8ce7-af27a977ebb0
```

**Response**:

```json
{
  "data" : {
    "type" : "sandboxTesters",
    "id" : "47be9e57-1a3f-49c2-8ce7-af27a977ebb0",
    "attributes" : {
      "firstName" : "Anne",
      "lastName" : "Johnson",
      "acAccountName" : "annejohnson1@icloud.com",
      "territory" : "CAN",
      "applePayCompatible" : true,
      "interruptPurchases" : false,
      "subscriptionRenewalRate" : "MONTHLY_RENEWAL_EVERY_THIRTY_MINUTES"
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v2/sandboxTesters/47be9e57-1a3f-49c2-8ce7-af27a977ebb0"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v2/sandboxTesters/47be9e57-1a3f-49c2-8ce7-af27a977ebb0"
  }
}

```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v2/sandboxTesters/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource. Obtain the Sandbox Tester resource ID from the [`List sandbox testers`](./get-v2-sandboxtesters.md) response

## Request Body

**Content-Type**: `application/json`  
**Type**: `SandboxTesterV2UpdateRequest`

## Responses

- `200` OK (`SandboxTesterV2Response`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`)
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`)
- `404` Not Found (`ErrorResponse`, `application/json`)
- `409` Conflict (`ErrorResponse`, `application/json`)
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Sandbox Tester Lookup and Modification
- [List sandbox testers](./get-v2-sandboxtesters.md)
  Get a list of Sandbox Testers for your team.
- [Clear purchase history for a sandbox tester](./post-v2-sandboxtestersclearpurchasehistoryrequest.md)
  Remove purchase history from a Sandbox Apple Account.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v2-sandboxtesters-_id_)*