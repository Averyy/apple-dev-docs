# Modify an end user license agreement

**Framework**: App Store Connect API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Update the text or territories for your custom end user license agreement.

**Availability**:
- App Store Connect API 1.2+

## Discussion

Use this endpoint to change the license agreement text or associate the agreement with different App Store territories.

In the following example the request contains a blank value for the `agreementText` attribute. Replace that attribute value with your actual agreement text.

If you change the territories relationship, the new territories replace the original territories.

### Change the Text of a License Agreement

**Request**:

```
PATCH /v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a

{
  "data": {
    "type": "endUserLicenseAgreements",
    "attributes": {
      "agreementText": "..."
    }
  }
}
```

**Response**:

```json
{
  "data" : {
    "type" : "endUserLicenseAgreements",
    "id" : "b25d1669-d6b1-4e9b-8679-02863557222a",
    "attributes" : {
      "agreementText" : "..."
    },
    "relationships" : {
      "app" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/relationships/app",
          "related" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/app"
        }
      },
      "territories" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/relationships/territories",
          "related" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/territories"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements"
  }
}
```

### Replace the Territories of a License Agreement with Japan and Canada

**Request**:

```
PATCH https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a

{
  "data": {
    "type": "endUserLicenseAgreements",
    "relationships": {
      "territories": {
        "data": [
          {
            "type": "territories",
            "id": "JPN"
          },
          {
            "type": "territories",
            "id": "CAN"
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
    "type" : "endUserLicenseAgreements",
    "id" : "b25d1669-d6b1-4e9b-8679-02863557222a",
    "attributes" : {
      "agreementText" : "..."
    },
    "relationships" : {
      "app" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/relationships/app",
          "related" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/app"
        }
      },
      "territories" : {
        "links" : {
          "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/relationships/territories",
          "related" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a/territories"
        }
      }
    },
    "links" : {
      "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/b25d1669-d6b1-4e9b-8679-02863557222a"
    }
  },
  "links" : {
    "self" : "https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements"
  }
}
```

## Endpoint

`PATCH https://api.appstoreconnect.apple.com/v1/endUserLicenseAgreements/{id}`

## Parameters

### Path Parameters

- `id` (string) *(required)*

## Request Body

**Content-Type**: `application/json`  
**Type**: `EndUserLicenseAgreementUpdateRequest`

## Responses

- `200` OK (`EndUserLicenseAgreementResponse`, `application/json`)
- `400` Bad Request (`ErrorResponse`, `application/json`): An error occurred with your request.
- `401` Unauthorized (`ErrorResponse`, `application/json`)
- `403` Forbidden (`ErrorResponse`, `application/json`): Request not authorized.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): The provided resource data is not valid.
- `422` (`ErrorResponse`, `application/json`)
- `429` (`ErrorResponse`, `application/json`)

## See Also

### Creating, Modifying, and Deleting an EULA
- [Create an end user license agreement](./post-v1-enduserlicenseagreements.md)
  Add a custom end user license agreement (EULA) to an app and configure the territories to which it applies.
- [Delete an end user license agreement](./delete-v1-enduserlicenseagreements-_id_.md)
  Delete the custom end user license agreement that is associated with an app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/patch-v1-enduserlicenseagreements-_id_)*